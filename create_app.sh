#!/bin/bash
# ============================================================================
# Shell Script: create_app.sh
# Description: Converts the Python file to a macOS app using PyInstaller
# Author: Student
# Date: 2026-02-27
# ============================================================================

echo ""
echo "============================================"
echo "  HKDSE ICT Pre-SBA 2: App Converter (macOS)"
echo "============================================"
echo ""
echo "This script will convert 4E13_preSBA2_GUI.py"
echo "to a macOS application using PyInstaller."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed!"
    echo "Please install Python from: https://www.python.org/downloads/"
    echo "Or use: brew install python"
    echo ""
    exit 1
fi

echo "[OK] Python detected: $(python3 --version)"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "[ERROR] pip3 is not available!"
    echo ""
    exit 1
fi

echo "[OK] pip3 detected!"

# Install PyInstaller if not already installed
echo ""
echo "Checking PyInstaller installation..."
if ! pip3 show pyinstaller &> /dev/null; then
    echo "PyInstaller not found. Installing now..."
    pip3 install pyinstaller
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to install PyInstaller!"
        echo ""
        exit 1
    fi
else
    echo "[OK] PyInstaller already installed!"
fi

echo ""
echo "============================================"
echo "  Converting to macOS App..."
echo "============================================"
echo ""

# Create the application using PyInstaller
# --onefile: Create a single executable file
# --windowed: Run without console window (for GUI apps)
# --name: Name of the output executable
# --clean: Clean PyInstaller cache
# --osx-bundle-identifier: Bundle identifier for macOS
pyinstaller --onefile --windowed --name "FacialExpression_4E13" --clean --osx-bundle-identifier "com.student.facialexpression" 4E13_preSBA2_GUI.py

if [ $? -ne 0 ]; then
    echo ""
    echo "[ERROR] Conversion failed!"
    echo "Please check the error messages above."
    echo ""
    exit 1
fi

echo ""
echo "============================================"
echo "  Conversion Successful!"
echo "============================================"
echo ""
echo "The application has been created!"
echo ""
echo "Location: dist/FacialExpression_4E13.app"
echo ""
echo "You can now run the program by double-clicking:"
echo "   dist/FacialExpression_4E13.app"
echo ""
echo "Or copy the .app file to any Mac"
echo "and run it without Python installed!"
echo ""
echo "============================================"
echo ""
