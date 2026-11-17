from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
doc = Document()
sec = doc.sections[0]
sec.top_margin = sec.bottom_margin = Inches(0.65)
sec.left_margin = sec.right_margin = Inches(0.75)
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
normal = doc.styles['Normal']
normal.font.name = 'Calibri'
normal.font.size = Pt(11)
normal.paragraph_format.space_after = Pt(5)
normal.paragraph_format.line_spacing = 1.05
for name in ['Title', 'Heading 1', 'Heading 2']:
    doc.styles[name].font.name = 'Calibri'
    doc.styles[name].font.color.rgb = RGBColor(0, 0, 0)
doc.styles['Title'].font.size = Pt(24)
doc.styles['Heading 1'].font.size = Pt(16)
doc.styles['Heading 2'].font.size = Pt(12)
doc.core_properties.title = 'FIN 439 Project 2 Review and Submission Checklist'
doc.core_properties.author = 'OpenAI Codex'

def item(n, title, action, location):
    doc.add_heading(f'[ ]  {n}  {title}', level=2)
    doc.add_paragraph(action)
    p = doc.add_paragraph()
    r = p.add_run('Open: ')
    r.bold = True
    p.add_run(location).italic = True

doc.add_heading('FIN 439 Project 2 Checklist', 0)
doc.add_paragraph('Review first, then verify, record, and submit. Check each box only after you personally finish the task. Prepared November 17, 2026.')
doc.add_paragraph('Project: Cedar Scholarship Foundation. Decide how its $20 million portfolio can support scholarships and preserve purchasing power. The current draft rejects deployment until missing evidence is resolved.')
doc.add_heading('First understand and review the project', 1)
item(1, 'Read the investment results',
     'Explain the objective, three portfolio alternatives, returns, risks, and reason for the draft recommendation.',
     'docs/checkout-results.md')
item(2, 'Run and explore the application',
     'Follow the README. Review the executive dashboard, comparison, and stress tabs. Try the already-tested 60-to-36-month window and restore 60. This demonstration is not the locked exercise.',
     'README.md and app.py')
doc.add_paragraph('Run from the project folder after installation:')
p = doc.add_paragraph(r'.venv\Scripts\python.exe -m streamlit run app.py')
p.runs[0].font.name = 'Consolas'
p.runs[0].font.size = Pt(10)
item(3, 'Confirm the mandate and assumptions',
     'Confirm Cedar and BIL, IEF, LQD, and VT match your coursework. Resolve or explicitly retain unknowns for the benchmark, BIL reserve proxy, risk limit, actual holdings/costs, and proposed CPI signal.',
     'config/mandate.json and docs/signal-data-card.md')
item(4, 'Practice explaining the calculations',
     'Explain how weights, expected returns, covariance, and constraints produce the portfolio. Practice the three questions without AI.',
     'docs/code-explanation-study-guide.md')
item(5, 'Review the recommendation and AI disclosure',
     'Read the memo and validation document. Make your own final judgment and identify what would reverse it. Acknowledge substantial AI assistance; record only checks you actually performed.',
     'docs/decision-memo.md and docs/validation-and-ai-use.md')

doc.add_page_break()
doc.add_heading('Verify and finish the submission', 0)
doc.add_paragraph('Existing evidence: 66 tests passed in the main environment and a fresh copied environment on the same computer. A real partner run, final publication, locked record, and recordings remain pending.')
item(6, 'Publish and complete the partner cold run',
     'Authorize the final commit and GitHub push. Have a partner download into their own folder on another computer and follow only the README. Record commands, failures, elapsed time, result location, and success. Fix and retest any problems.',
     'docs/partner-cold-run-template.md')
item(7, 'Complete the genuine locked exercise',
     'With AI closed, write your prediction and reasoning. Commit and push them BEFORE running the changed scenario. Then run with AI closed, record before/after results, and explain the difference. Do not overwrite an existing locked record or treat an ordinary stress as this exercise.',
     'docs/changed-input-record.md; separate class template: docs/tuesday-changed-input-template.md')
item(8, 'Record three videos and correct transcripts',
     'Video 1: system and thinking, maximum 3 minutes. Video 2: code walkthrough, maximum 5 minutes. Video 3: committee presentation, maximum 5 minutes, opening with the live app. Include AI-use and student-responsibility disclosures. Upload to YouTube; correct actual transcripts. Scripts are not transcripts.',
     'videos/video-1-script.md, video-2-script.md, video-3-script.md, and recording-checklist.md')
item(9, 'Finish and verify the submission manifest',
     'Add real GitHub links for the repository, visible output, memo, validation, and transcripts; add the three YouTube links. Record actual durations, access checks, and final revision. Test reviewer access. Review any newer Brightspace instructions.',
     'docs/submission-manifest.md')
item(10, 'Submit the final materials',
     'Submit the completed manifest and required links through Brightspace. Attach the actual decision-memo.md and validation-and-ai-use.md files as well as linking their GitHub versions. Confirm receipt. This checklist is a personal guide, not a replacement for those deliverables.',
     'docs/decision-memo.md and docs/validation-and-ai-use.md')
doc.add_heading('Where everything lives', 1)
doc.add_paragraph('Keep the existing fin439_project2_investment_management folder together. README.md explains setup; docs/ contains results and submission documents; videos/ contains scripts; data/ and config/ support the app; src/ and tests/ contain code and validation.')
doc.add_paragraph('Personal completion date: ____________________')
out = ROOT / 'START_HERE_Project_2_Checklist.docx'
doc.save(out)
print(out)
