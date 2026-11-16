# FIN 43900 Lab 15

Use [Lab15_Checkout.md](Lab15_Checkout.md) for the checkout checklist, including the portfolio Mermaid flowcharts in the report.

Read [Lab15_Portfolio_Stability.md](Lab15_Portfolio_Stability.md) for results, limitations, provenance, and the student-only completion fields.

Use Python 3.13 (the tested interpreter). From this folder:

```powershell
python -m pip install -r requirements.txt
python portfolio.py
python verify_submission.py
python -m streamlit run app.py
```

Open the local URL printed by Streamlit; stop with Ctrl+C. The validation session used port 8515. In the app select Meridian, Cedar, or Upload CSV. Upload mode requires an uploaded CSV and an explicit choice of reserve-eligible assets. Select Cedar to load the included data. Cedar's 5.5% default is an illustration pending confirmation of CPI and costs, not a replacement for its CPI + 3% after-cost mandate.

## Files to submit

Keep this folder together: `portfolio.py`, `app.py`, `Lab15_Portfolio_Stability.md`, `prices.csv`, `requirements.txt`, `README.md`, `.gitignore`, `test_lab15.py`, `verify_submission.py`, `verification.txt`, `portfolio_results.txt`, `original_output.txt`, `project2_results.json`, `Project2_Mandate_Source.md`, `Lab14_Source_Report.md`, and `sources/` (original prices and download metadata). Do not include `.venv` or `__pycache__`.

## GitHub and Brightspace handoff

Nothing has been published. First fill in the student-only partner activity, decision, and reflection and resolve/acknowledge the missing mandate assumptions. Rerun verification after any code or data edits.

1. Choose your course GitHub repository. Upload this entire `Lab15` folder, retaining the relative paths and `sources/`, or copy it into your existing local repository and review `git diff` before committing. Do not initialize or push the whole course workspace accidentally.
2. Commit with a clear message such as `Complete Lab 15 portfolio stability dashboard`. Push only when you approve publication. Review the resulting GitHub files and make sure the instructor has access.
3. Copy the GitHub URL for this folder and the report. In the Lab 15 Brightspace assignment, follow the instructor's actual requested submission format: paste the links and attach files if requested. No assignment-specific deadline, rubric, or required attachment format was independently located or verified in this task.
4. Submit in Brightspace and verify the submission receipt/status. Neither the GitHub push nor Brightspace submission has been performed here.

Testing limitations: the server and automated Streamlit AppTest paths were tested; visual browser inspection and a real file-picker upload remain unverified because browser control was unavailable.
