@echo off
echo ================================================
echo Stock Fundamentals Analyzer - Git Setup
echo ================================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo Git is installed. Proceeding with setup...
echo.

REM Initialize git repository
echo [Step 1/3] Initializing Git repository...
git init
if errorlevel 1 (
    echo ERROR: Failed to initialize Git repository
    pause
    exit /b 1
)
echo ✓ Git repository initialized
echo.

REM Add all files
echo [Step 2/3] Adding files to Git...
git add .
if errorlevel 1 (
    echo ERROR: Failed to add files
    pause
    exit /b 1
)
echo ✓ Files added to staging
echo.

REM Create initial commit
echo [Step 3/3] Creating initial commit...
git commit -m "Initial commit: Stock Fundamentals Analyzer"
if errorlevel 1 (
    echo ERROR: Failed to create commit
    pause
    exit /b 1
)
echo ✓ Initial commit created
echo.

echo ================================================
echo Git setup complete!
echo ================================================
echo.
echo Next steps:
echo 1. Create a new repository on GitHub
echo    Go to: https://github.com/new
echo.
echo 2. Run these commands (replace YOUR_USERNAME and YOUR_REPO):
echo    git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. Deploy to Streamlit Cloud
echo    Go to: https://share.streamlit.io/
echo.
echo See DEPLOYMENT.md for detailed instructions
echo.
pause
