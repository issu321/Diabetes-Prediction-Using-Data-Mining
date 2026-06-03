@echo off
REM =============================================================================
REM Diabetes Prediction Using Data Mining - Installation Script (Windows)
REM Project ID: EDUFYPML007
REM Developed By: EduPhonix-Solution
REM GitHub: https://github.com/issu321
REM Repository: https://github.com/issu321/Diabetes-Prediction-Using-Data-Mining
REM =============================================================================

title Diabetes Prediction - Installer
color 0A

echo.
echo =============================================================================
echo   🩺 DIABETES PREDICTION USING DATA MINING - INSTALLER
echo   Project ID: EDUFYPML007
echo   Developed By: EduPhonix-Solution
echo =============================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python is installed.

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not installed.
    pause
    exit /b 1
)

echo [OK] pip is available.

REM Get script directory
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

echo [INFO] Project directory: %SCRIPT_DIR%

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo [INFO] Creating virtual environment...
    python -m venv venv
    echo [OK] Virtual environment created.
) else (
    echo [OK] Virtual environment already exists.
)

REM Activate virtual environment
echo [INFO] Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo [INFO] Upgrading pip...
pip install --upgrade pip

REM Install requirements
echo [INFO] Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo [OK] All dependencies installed successfully!

REM Train models
echo [INFO] Training machine learning models...
python train_model.py

echo [OK] Models trained and saved successfully!

REM Create start.bat
echo @echo off > start.bat
echo title Diabetes Prediction - Streamlit App >> start.bat
echo color 0B >> start.bat
echo cd /d "%%~dp0" >> start.bat
echo call venv\Scripts\activate.bat >> start.bat
echo echo. >> start.bat
echo echo ============================================================================= >> start.bat
echo echo   🚀 Starting Diabetes Prediction Application... >> start.bat
echo echo   📱 Open your browser and navigate to: http://localhost:8501 >> start.bat
echo echo   🛑 Press Ctrl+C to stop the server >> start.bat
echo echo ============================================================================= >> start.bat
echo echo. >> start.bat
echo streamlit run app.py >> start.bat

echo [OK] Start script created: start.bat

echo.
echo =============================================================================
echo   ✅ INSTALLATION COMPLETED SUCCESSFULLY!
echo =============================================================================
echo.
echo 🚀 To start the application, run:
echo    start.bat
echo.
echo 📱 The application will be available at:
echo    http://localhost:8501
echo.
echo 📝 Or manually activate and run:
echo    venv\Scripts\activate.bat
echo    streamlit run app.py
echo.
echo 👨‍💻 Developer: EduPhonix-Solution
echo 🐙 GitHub: https://github.com/issu321
echo 📁 Repository: https://github.com/issu321/Diabetes-Prediction-Using-Data-Mining
echo.

pause
