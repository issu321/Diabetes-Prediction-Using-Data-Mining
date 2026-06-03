@echo off
REM =============================================================================
REM Diabetes Prediction Using Data Mining - Start Script (Windows)
REM Project ID: EDUFYPML007
REM Developed By: EduPhonix-Solution
REM GitHub: https://github.com/issu321
REM Repository: https://github.com/issu321/Diabetes-Prediction-Using-Data-Mining
REM =============================================================================

title Diabetes Prediction - Streamlit App
color 0B

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Check if venv exists
if not exist "venv" (
    echo [WARNING] Virtual environment not found. Running installer first...
    call install.bat
    exit /b
)

call venv\Scriptsctivate.bat

echo.
echo =============================================================================
echo   🚀 Starting Diabetes Prediction Application
echo   Project ID: EDUFYPML007
echo =============================================================================
echo.
echo 📱 Open your browser and navigate to: http://localhost:8501
echo 🛑 Press Ctrl+C to stop the server
echo.

streamlit run app.py
