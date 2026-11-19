@echo off
setlocal
cd /d "%~dp0"
if errorlevel 1 goto fail

echo Cedar Investment Committee - FIN 439 Project 2
echo Project folder: %CD%
echo.

if not exist ".venv\Scripts\python.exe" (
    echo First run: creating a Python 3.13 environment...
    py -3.13 -m venv .venv
    if errorlevel 1 (
        echo Python 3.13 was not found. Install it, then run OPEN_APP.cmd again.
        goto fail
    )
    echo Installing the pinned requirements. This may take a few minutes...
    ".venv\Scripts\python.exe" -m pip install -r requirements-lock.txt
    if errorlevel 1 goto fail
)

echo Starting the app. Your browser should open automatically.
echo If it does not, open the Local URL printed below.
echo Keep this window open while using the app. Press Ctrl+C to stop it.
echo.
".venv\Scripts\python.exe" -m streamlit run app.py
if errorlevel 1 goto fail
exit /b 0

:fail
echo.
echo The app did not start. Read the error above, then see README.md.
pause
exit /b 1
