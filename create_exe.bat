@echo off
REM ============================================================================
REM Batch File: create_exe.bat
REM Description: Converts the Python file to an executable (.exe) using PyInstaller
REM Author: Student
REM Date: 2026-02-27
REM ============================================================================

echo.
echo ============================================
echo   HKDSE ICT Pre-SBA 2: EXE Converter
echo ============================================
echo.
echo This batch file will convert 4E13_preSBA2_GUI.py
echo to a GUI executable (.exe) file using PyInstaller.
echo The program will have a clickable interface!
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please install Python first from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python detected!

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not available!
    echo.
    pause
    exit /b 1
)

echo [OK] pip detected!

REM Install PyInstaller if not already installed
echo.
echo Checking PyInstaller installation...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing now...
    pip install pyinstaller
    if errorlevel 1 (
        echo [ERROR] Failed to install PyInstaller!
        echo.
        pause
        exit /b 1
    )
) else (
    echo [OK] PyInstaller already installed!
)

echo.
echo ============================================
echo   Converting to EXE...
echo ============================================
echo.

REM Create the executable using PyInstaller
REM --onefile: Create a single executable file
REM --windowed: Run without console window (for GUI apps)
REM --name: Name of the output executable
REM --clean: Clean PyInstaller cache
REM --noconsole: Hide the console window (GUI only)
pyinstaller --onefile --windowed --name "FacialExpression_4E13" --clean 4E13_preSBA2_GUI.py

if errorlevel 1 (
    echo.
    echo [ERROR] Conversion failed!
    echo Please check the error messages above.
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   Conversion Successful!
echo ============================================
echo.
echo The executable file has been created!
echo.
echo Location: dist\FacialExpression_4E13.exe
echo.
echo You can now run the program by double-clicking:
echo   dist\FacialExpression_4E13.exe
echo.
echo Or copy the .exe file to any computer (Windows)
echo and run it without Python installed!
echo.
echo ============================================
echo.
pause
