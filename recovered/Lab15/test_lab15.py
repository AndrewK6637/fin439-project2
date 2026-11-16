"""Executable regression and Streamlit AppTest checks; no market downloads."""
import io
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
from streamlit.testing.v1 import AppTest
import portfolio as p

HERE = Path(__file__).resolve().parent


class Lab15Tests(unittest.TestCase):
    def optimize(self, sleeves=None, correlations=None, objective=.065, reserve=.03):
        return p.optimize_portfolio(sleeves or p.SLEEVES, correlations or p.CORRELATIONS,
                                    objective, reserve, p.RESERVE_ELIGIBLE)

    def test_original_output(self):
        run = subprocess.run([sys.executable, str(HERE / 'portfolio.py')], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0)
        self.assertEqual(run.stdout.strip(), (HERE / 'original_output.txt').read_text().strip())

    def test_meridian(self):
        base = self.optimize()
        stress_inputs = dict(p.SLEEVES)
        stress_inputs['Global equity index fund'] = (.07, .16)
        stress = self.optimize(stress_inputs)
        corr = [row[:] for row in p.CORRELATIONS]
        corr[2][3] = corr[3][2] = .50
        connection = self.optimize(correlations=corr)
        for result, weights, ret, vol in [
            (base, [0,.20,.25,.55], '6.51%', '9.44%'),
            (stress, [0,.10,.10,.80], '6.53%', '12.94%'),
            (connection, [0,.40,0,.60], '6.52%', '9.73%')]:
            self.assertEqual(result['weights'], weights)
            self.assertEqual(f"{result['expected_return']:.2%}", ret)
            self.assertEqual(f"{result['volatility']:.2%}", vol)
        self.assertAlmostEqual(p.largest_weight_change(base['weights'],stress['weights']),25)
        self.assertIsNone(self.optimize(objective=.20))
        self.assertIsNone(self.optimize(reserve=1))

    def test_grid_and_validation(self):
        grid = list(p.weight_grid(4))
        self.assertEqual(len(grid), math.comb(23,3))
        self.assertEqual(len(set(grid)),len(grid))
        self.assertTrue(all(abs(sum(w)-1)<1e-12 and min(w)>=0 for w in grid))
        with self.assertRaises(ValueError):
            self.optimize(reserve=-.01)
        corr = [row[:] for row in p.CORRELATIONS]
        corr[2][3] = 1.3
        with self.assertRaises(ValueError):
            self.optimize(correlations=corr)

    def test_estimates_and_bad_csv(self):
        frame = pd.read_csv(HERE/'prices.csv',index_col=0)
        monthly = frame.pct_change().iloc[1:]
        for last, count in [(False,60),(True,36)]:
            estimates = p.estimate_prices(HERE/'prices.csv',last)
            sample = monthly.tail(36) if last else monthly
            self.assertEqual(estimates['months'],count)
            np.testing.assert_allclose(list(estimates['sleeves'].values()),
                                       np.column_stack([sample.mean()*12,sample.std(ddof=1)*np.sqrt(12)]))
            np.testing.assert_allclose(estimates['correlations'],sample.corr())
        for csv in ['Date,A\n2024-01-31,1\n2024-01-15,2\n2024-03-31,3',
                    'Date,A\n2024-01-31,1\n2024-03-31,2\n2024-04-30,3',
                    'Date,A\n2024-01-31,1\n2024-02-29,0\n2024-03-31,3']:
            with self.assertRaises(ValueError):
                p.estimate_prices(io.StringIO(csv))
        with self.assertRaises(ValueError):
            p.estimate_prices(io.StringIO('Date,A\n2024-01-31,1\n2024-02-29,2\n2024-03-31,3'),True)

    def test_dashboard_controls(self):
        app = AppTest.from_file(str(HERE/'app.py'),default_timeout=30).run()
        self.assertFalse(app.exception)
        self.assertEqual(app.metric[0].value,'6.51%')
        equity = next(x for x in app.number_input if x.label == 'Global equity index fund expected return (%)')
        equity.set_value(7.0).run()
        self.assertFalse(app.exception)
        self.assertEqual(app.metric[3].value,'6.53%')
        self.assertEqual(app.metric[4].value,'12.94%')
        self.assertEqual(app.metric[6].value,'25.00 percentage points')
        next(x for x in app.number_input if x.label=='Annual objective (%)').set_value(20.0).run()
        self.assertIn('No feasible portfolio',app.error[0].value)
        next(x for x in app.number_input if x.label=='Annual objective (%)').set_value(6.5).run()
        for box in app.checkbox:
            box.set_value(False)
        app.run()
        self.assertIn('No feasible portfolio',app.error[0].value)
        app.selectbox[0].set_value('Cedar prices.csv').run()
        self.assertFalse(app.exception)
        self.assertTrue(any('60 returns' in x.value for x in app.info))
        app.toggle[0].set_value(True).run()
        self.assertTrue(any('36 returns' in x.value for x in app.info))
        self.assertFalse(app.exception)

    def test_upload_integration(self):
        # AppTest has no file-uploader setter: supply the UploadedFile-compatible
        # byte stream at the widget boundary, then execute the complete app path.
        app = AppTest.from_file(str(HERE/'app.py'),default_timeout=30).run()
        with patch('streamlit.delta_generator.DeltaGenerator.file_uploader',return_value=io.BytesIO((HERE/'prices.csv').read_bytes())):
            app.selectbox[0].set_value('Upload CSV').run()
            self.assertFalse(app.exception)
            next(x for x in app.checkbox if x.label=='BIL reserve eligible').set_value(True).run()
            self.assertFalse(app.error)
            self.assertTrue(any('60 returns' in x.value for x in app.info))
            app.toggle[0].set_value(True).run()
            self.assertTrue(any('36 returns' in x.value for x in app.info))
        with patch('streamlit.delta_generator.DeltaGenerator.file_uploader',return_value=io.BytesIO(b'Date,A\n2024-01-31,-1')):
            app.run()
            self.assertTrue(app.error)
            self.assertFalse(app.exception)

    def test_source_correlation_connection(self):
        # Change both cells in a temporary portfolio.py, execute the actual app
        # in a fresh interpreter, and verify the delivered source is untouched.
        original = (HERE/'portfolio.py').read_text()
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            (folder/'portfolio.py').write_text(original.replace('0.25','0.50'))
            (folder/'app.py').write_text((HERE/'app.py').read_text())
            check = "from streamlit.testing.v1 import AppTest; a=AppTest.from_file('app.py',default_timeout=30).run(); assert not a.exception; assert a.metric[3].value=='6.52%'; assert a.metric[4].value=='9.73%'; assert a.dataframe[1].value['Weight (%)'].tolist()==[0,40,0,60]; print('Source-file correlation app connection PASS')"
            run = subprocess.run([sys.executable,'-c',check],cwd=folder,capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stdout+run.stderr)
        self.assertEqual((HERE/'portfolio.py').read_text(),original)
        self.assertEqual(p.CORRELATIONS[2][3],.25)


if __name__ == '__main__':
    unittest.main(verbosity=2)
