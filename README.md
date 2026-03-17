# HKDSE ICT Pre-SBA 2: Facial Expression Program

## Student Information
- **Class**: 4E
- **Student ID**: 13
- **Project**: Pre-SBA 2 - Facial Expression
- **Date**: 27/02/2026

---

## Project Website

Visit the interactive demo and project page:

**https://ifung-0.github.io/pre-sba2-ict/**

---

## Quick Start

Run the program in one click:

**Windows:**
```
python 4E13_preSBA2_GUI.py
```

**Mac/Linux:**
```
python3 4E13_preSBA2_GUI.py
```

You will see a window with 7 facial expressions. Click any button to display that expression. Use the dropdown menus to change colors and size.

---

## What This Program Does

This program shows 7 facial expressions using emoji squares. You can:

- Pick from 7 expressions (Happy, Sad, Angry, Surprised, Wink, Cool, Love)
- Change face color (8 options)
- Change eye color (6 options)
- Change background color (3 options)
- Make the face bigger (3 size options)

The program has two versions:

| Version | File | Best For |
|---------|------|----------|
| GUI Version | `4E13_preSBA2_GUI.py` | Visual learners, mouse users |
| CLI Version | `4E13_preSBA2.py` | Keyboard users, terminal lovers |

---

## Key Concepts Explained Simply

### What is a 2D Array?

A 2D array is like a grid or table. Think of it as a spreadsheet with rows and columns.

This program uses a **10x10 grid** (10 rows, 10 columns) to store each face:

```
Row 0:  [B, B, B, F, F, F, F, B, B, B]
Row 1:  [B, F, F, F, F, F, F, F, F, B]
Row 2:  [F, F, E, E, F, F, E, E, F, F]
...
```

Each letter means something:
- **F** = Face (gets colored yellow, blue, green, etc.)
- **E** = Eye (gets colored black, red, blue, etc.)
- **B** = Background (gets colored white, black, blue)

### What are Nested Loops?

A nested loop is a loop inside another loop. The program uses nested loops to read the 10x10 grid:

```python
# Outer loop: goes through each ROW (top to bottom)
for row in range(10):
    # Inner loop: goes through each COLUMN (left to right)
    for col in range(10):
        # Get the emoji at this position
        print(grid[row][col], end="")
    print()  # Move to next line
```

**How it works:**
1. Outer loop picks row 0
2. Inner loop prints all 10 cells in row 0
3. Outer loop picks row 1
4. Inner loop prints all 10 cells in row 1
5. Repeat until all 10 rows are printed

This prints the face one row at a time.

---

## Features

### 7 Facial Expressions

| Expression | Description |
|------------|-------------|
| Happy | Smiling face with curved mouth |
| Sad | Frowning face with downturned mouth |
| Angry | Furrowed brows with tight mouth |
| Surprised | Wide eyes with open mouth |
| Wink | One eye closed, playful smile |
| Cool | Sunglasses with confident smirk |
| Love | Heart-shaped eyes (red) |

### Color Options

**Face Colors (8):** Yellow, Blue, Green, Orange, Purple, Brown, White, Black

**Eye Colors (6):** Black, Red, Blue, Green, Purple, Brown

**Background Colors (3):** White, Black, Blue

### Size Options

| Scale | Size | Description |
|-------|------|-------------|
| 1x | 10x10 | Normal size |
| 2x | 20x20 | Double size |
| 3x | 30x30 | Triple size |

---

## How to Run

### Method 1: GUI Version (Recommended for beginners)

1. Open Command Prompt (Windows) or Terminal (Mac/Linux)
2. Navigate to the project folder:
   ```
   cd c:\Users\Isaac\OneDrive\Desktop\pre-sba2-ict-master
   ```
3. Run the program:
   ```
   python 4E13_preSBA2_GUI.py
   ```

### Method 2: CLI Version (Terminal-based)

1. Open Command Prompt or Terminal
2. Navigate to the project folder
3. Run:
   ```
   python 4E13_preSBA2.py
   ```
4. Follow the menu prompts

### Method 3: Create an Executable (Run without Python)

**Windows:**
```
double-click create_exe.bat
```

**Mac/Linux:**
```
bash create_app.sh
```

The executable will be in the `dist` folder.

---

## Keyboard Shortcuts (GUI Version)

### Select Expressions
| Key | Action |
|-----|--------|
| 1-7 | Select expression (Happy to Love) |
| Numpad 1-7 | Also works |

### Actions
| Key | Action |
|-----|--------|
| Ctrl+R | Refresh display |
| Ctrl+C | Copy to clipboard |
| Ctrl+D | Reset to defaults |
| F1 | Show help |
| Ctrl+Q | Quit |

### Change Size
| Key | Action |
|-----|--------|
| Ctrl+1 | Normal (10x10) |
| Ctrl+2 | Large (20x20) |
| Ctrl+3 | Extra Large (30x30) |

### Change Colors
| Key | Action |
|-----|--------|
| Shift+Up/Down | Cycle face colors |
| Shift+Left/Right | Cycle eye colors |

---

## File Structure

```
pre-sba2-ict-master/
│
├── 4E13_preSBA2.py         # CLI version (terminal)
├── 4E13_preSBA2_GUI.py     # GUI version (window)
├── create_exe.bat          # Make .exe for Windows
├── create_app.sh           # Make .app for Mac
├── requirements.txt        # List of dependencies
├── README.md              # This file
├── LICENSE                # MIT License
└── index.html             # Project webpage
```

---

## Requirements

You need:
- Python 3.6 or higher
- tkinter (comes with Python)
- NumPy (optional, for CLI demo)

### Install Dependencies

```
pip install -r requirements.txt
```

---

## Troubleshooting

**Problem:** "Python not found"
**Fix:** Install Python from https://www.python.org/downloads/

**Problem:** "tkinter not found"
**Fix:** tkinter comes with Python. Reinstall Python if missing.

**Problem:** Program window is too small
**Fix:** Use the Size dropdown or press Ctrl+2 / Ctrl+3

**Problem:** Colors look wrong
**Fix:** Click "Reset to Defaults" or press Ctrl+D

---

## What You Will Learn

By studying this code, you will understand:

1. **2D Arrays** - How to store data in rows and columns
2. **Nested Loops** - How to process 2D data
3. **Functions** - How to organize code into reusable blocks
4. **Classes** - How to group related data and functions
5. **GUI Programming** - How to build windowed applications
6. **User Input** - How to handle mouse clicks and keyboard presses
7. **Color Systems** - How to use hex color codes

---

## Code Structure

### GUI Version (`4E13_preSBA2_GUI.py`)

| Class | Purpose |
|-------|---------|
| EmojiColors | Stores all color options |
| FacialExpressions | Stores all 7 face templates |
| FacialExpressionGUI | Builds and runs the window |

### CLI Version (`4E13_preSBA2.py`)

| Class | Purpose |
|-------|---------|
| EmojiColors | Stores all color options |
| FacialExpressions | Stores all 7 face templates |
| FaceRenderer | Draws faces in terminal |
| UserInterface | Handles menu and input |

---

## Tips for Understanding the Code

1. **Start with the 2D arrays** - Look at `get_happy_face()` to see how a face is stored
2. **Trace the nested loops** - Follow how `render_face()` prints each row
3. **Try changing values** - Modify a color or expression and see what happens
4. **Add comments** - Write notes to yourself as you read the code

---

## Project Demo

Visit the project webpage for an interactive demo:
https://ifung-0.github.io/pre-sba2-ict/

---

## Star History

<a href="https://www.star-history.com/?repos=ifung-0%2Fpre-sba2-ict&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=ifung-0/pre-sba2-ict&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=ifung-0/pre-sba2-ict&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=ifung-0/pre-sba2-ict&type=date&legend=top-left" />
 </picture>
</a>

---

**Submitted for:** HKDSE ICT Pre-SBA 2
**Submission Date:** 27/02/2026
**Deadline:** 27/02/2026 (Fri) 23:59:59
