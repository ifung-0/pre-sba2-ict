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
python -m pip --version >nul 2>&1
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
python -m pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing now...
    python -m pip install pyinstaller
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
echo Please wait... This may take a few minutes.
echo.

REM Create the executable using PyInstaller
REM --onefile: Create a single executable file
REM --windowed: Run without console window (for GUI apps)
REM --name: Name of the output executable
REM --clean: Clean PyInstaller cache
python -m PyInstaller --onefile --windowed --name "FacialExpression_4E13" --clean 4E13_preSBA2_GUI.py

REM Check if build completed
if errorlevel 1 (
    echo.
    echo [ERROR] Conversion failed!
    echo Please check the error messages above.
    echo.
    pause
    exit /b 1
)

REM Give the file system a moment to finalize
timeout /t 2 /nobreak >nul 2>&1

echo.
echo ============================================
echo   Conversion Complete!
echo ============================================
echo.

REM Verify the EXE was created using absolute path
set "EXE_FILE=%~dp0dist\FacialExpression_4E13.exe"
if exist "%EXE_FILE%" (
    echo [SUCCESS] Executable file created!
    echo.
    for %%A in ("%EXE_FILE%") do echo File size: %%~zA bytes
    echo.
    echo Location: %EXE_FILE%
    echo.
    echo You can now run the program by double-clicking:
    echo   dist\FacialExpression_4E13.exe
    echo.
    echo Or copy the .exe file to any computer (Windows)
    echo and run it without Python installed!
) else (
    echo [ERROR] EXE file not found!
    echo Please check the build output for errors.
    echo.
    echo Expected location: %EXE_FILE%
)

echo.
echo ============================================
echo.
pause
