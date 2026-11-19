"""Independent expected answers exercising the actual provenance functions."""
import copy
import io
import random
import unittest
from contextlib import redirect_stdout
import asof


class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.rows = asof.read_records()

    def test_known_funnel_and_panel(self):
        panel, funnel = asof.asof_panel(self.rows, '2026-03-31')
        self.assertEqual([s['removed'] for s in funnel], [[11], [7], [3, 8, 10], [2]])
        self.assertEqual([s['before'] for s in funnel], [12, 11, 10, 7])
        self.assertEqual([s['after'] for s in funnel], [11, 10, 7, 6])
        self.assertEqual([r['row_id'] for r in panel], [1, 4, 5, 6, 9, 12])

    def test_both_signals_months_and_rounding(self):
        panel, _ = asof.asof_panel(self.rows, '2026-03-31')
        expected = [(panel, {'AAA': (103/101-1, '+1.98%, February 2026'),
                             'BBB': (97/98-1, '-1.02%, February 2026'),
                             'CCC': (111/110-1, '+0.91%, February 2026')}),
                    (asof.naive_panel(self.rows),
                     {'AAA': (109/103-1, '+5.83%, March 2026'),
                      'BBB': (92/97-1, '-5.15%, March 2026'),
                      'CCC': (112/110-1, '+1.82%, February 2026')})]
        for data, answers in expected:
            actual = asof.signals(data)
            for ticker, (value, display) in answers.items():
                with self.subTest(ticker=ticker, display=display):
                    self.assertAlmostEqual(actual[ticker]['percent'], value*100, places=10)
                    self.assertEqual(asof.format_signal(actual[ticker]), display)

    def test_april_convergence(self):
        panel, funnel = asof.asof_panel(self.rows, '2026-04-15')
        self.assertEqual(funnel[2]['removed'], [])
        self.assertEqual(panel, asof.naive_panel(self.rows))
        self.assertEqual(asof.signals(panel), asof.signals(asof.naive_panel(self.rows)))

    def test_inclusive_cutoff(self):
        row = dict(self.rows[0], published_on='2026-03-31')
        self.assertEqual(asof.asof_panel([row], '2026-03-31')[0], [row])
        self.assertEqual(asof.asof_panel([row], '2026-03-30')[0], [])

    def test_missing_ticker(self):
        for ticker in (None, '', '   ', '\t'):
            self.assertEqual(asof.quarantine([dict(self.rows[0], ticker=ticker)]), [])
        row = dict(self.rows[0])
        del row['ticker']
        self.assertEqual(asof.quarantine([row]), [])

    def test_duplicate_fields_and_original_id(self):
        row = self.rows[5]
        duplicate = dict(row, row_id=100)
        changed = dict(row, row_id=101, price=96.0)
        self.assertEqual([r['row_id'] for r in asof.deduplicate([duplicate, changed, row])], [6, 101])

    def test_revision_and_tie(self):
        original, revised = self.rows[1], self.rows[3]
        tied = dict(revised, row_id=99, price=900.0)
        for rows in ([tied, original, revised], [revised, original, tied]):
            self.assertEqual(asof.latest_vintages(rows), [revised])

    def test_order_independence_and_no_mutation(self):
        saved = copy.deepcopy(self.rows)
        expected = asof.asof_panel(self.rows, '2026-03-31')
        naive = asof.naive_panel(self.rows)
        for seed in range(10):
            shuffled = copy.deepcopy(self.rows)
            random.Random(seed).shuffle(shuffled)
            before = copy.deepcopy(shuffled)
            self.assertEqual(asof.asof_panel(shuffled, '2026-03-31'), expected)
            self.assertEqual(asof.naive_panel(shuffled), naive)
            asof.signals(shuffled)
            self.assertEqual(shuffled, before)
        self.assertEqual(self.rows, saved)

    def test_insufficient_history_and_zero(self):
        self.assertIsNone(asof.signals(self.rows[:1])['AAA']['percent'])
        rows = [dict(self.rows[0], price=0), self.rows[1]]
        self.assertEqual(asof.signals(rows)['AAA']['reason'], 'previous price is zero')
        self.assertEqual(asof.signals([]), {})
        self.assertIn('no available', asof.format_signal(None))

    def test_previous_available_month(self):
        rows = [dict(self.rows[0], price=100), dict(self.rows[2], price=105)]
        self.assertAlmostEqual(asof.signals(rows)['AAA']['percent'], 5.0)
        self.assertEqual(asof.signals(rows)['AAA']['month'], '2026-03')

    def test_default_and_printed_output(self):
        self.assertEqual(asof.DECISION_DATE, '2026-03-31')
        output = io.StringIO()
        with redirect_stdout(output):
            asof.main()
        for text in ('+1.98%', '-1.02%', '+0.91%', '+5.83%', '-5.15%', '+1.82%'):
            self.assertIn(text, output.getvalue())


if __name__ == '__main__':
    unittest.main()
