# HKDSE ICT Pre-SBA 2: Facial Expression Program

## Student Information
- **Class**: 4E
- **Student ID**: 13
- **Project**: Pre-SBA 2 - Facial Expression
- **Date**: 27/02/2026

---

## Project Overview

This Python program displays **7 different facial expressions** using a **10x10 2D array** system with **nested loops** for rendering. The project includes **two versions**:
- **CLI Version** (`4E13_preSBA2.py`): Terminal-based with emoji rendering
- **GUI Version** (`4E13_preSBA2_GUI.py`): Mouse-clickable interface using tkinter

---

## How the 2D Array Maps to Facial Features

### Array Structure

Each facial expression is stored as a **10x10 2D array** (nested list) where:

```
Row 0: Top border (usually empty)
Row 1-2: Eyes area
Row 3-4: Forehead/space between eyes and mouth
Row 5-8: Mouth area
Row 9: Bottom border (usually empty)

Columns 0-9: Left to right positioning
```

### Visual Mapping

```
        Col: 0 1 2 3 4 5 6 7 8 9
             ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
Row 0:      [ , , , , , , , , , ]  ← Top spacing
Row 1:      [ , ,O, , , , ,O, , ]  ← Eyes (O)
Row 2:      [ , ,O, , , , ,O, , ]  ← Eyes (O)
Row 3:      [ , , , , , , , , , ]  ← Forehead space
Row 4:      [ , , , , , , , , , ]  ← Forehead space
Row 5:      [ , , ,-, -, -, -, , , ]  ← Mouth top
Row 6:      [ , ,/, , , , , \, , ]  ← Mouth sides
Row 7:      [ ,|, , , , , , , |, ]  ← Mouth sides
Row 8:      [ , ,\,_, _, _, _, /, , ]  ← Mouth bottom
Row 9:      [ , , , , , , , , , ]  ← Bottom spacing
```

### Symbol Meanings (Template System)

The program uses a template system with placeholder symbols that get replaced with colored emojis:

| Symbol | Meaning | Description |
|--------|---------|-------------|
| `F` | Face | Replaced with face color emoji (🟨🟦🟩🟧🟪🟫⬜⬛) |
| `E` | Eye/Mouth | Replaced with eye/mouth color emoji (⬛🟥🟦🟩🟪🟫) |
| `B` | Background | Replaced with background color emoji (⬜⬛🟦) | |

### Example: Happy Face Array (Template)

```python
happy_face = [
    ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"],  # Row 0: Top
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],  # Row 1: Face expands
    ["F", "F", "E", "E", "F", "F", "E", "E", "F", "F"],  # Row 2: Eyes
    ["F", "F", "E", "E", "F", "F", "E", "E", "F", "F"],  # Row 3: Eyes
    ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],  # Row 4: Space
    ["F", "E", "F", "F", "F", "F", "F", "F", "E", "F"],  # Row 5: Smile corners
    ["F", "F", "E", "F", "F", "F", "F", "E", "F", "F"],  # Row 6: Smile curve
    ["F", "F", "F", "E", "E", "E", "E", "F", "F", "F"],  # Row 7: Smile mouth
    ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],  # Row 8: Bottom
    ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"]   # Row 9: Bottom
]
# After color application: F→🟨, E→⬛, B→⬜
```

---

## Nested Loops Implementation

The program uses **nested loops** to render the face:

```python
# OUTER LOOP: Iterate through each row (y-axis)
for row_index in range(len(face_array)):
    line = ""
    
    # INNER LOOP: Iterate through each column (x-axis)
    for col_index in range(len(face_array[row_index])):
        # Get the symbol at this position
        symbol = face_array[row_index][col_index]
        line += symbol
    
    # Print the completed row
    print(line)
```

**How it works:**
1. Outer loop goes through rows 0 to 9
2. For each row, inner loop goes through columns 0 to 9
3. Each symbol at `array[row][column]` is added to the line
4. After inner loop completes, the line is printed
5. Process repeats for all 10 rows

---

## Features

### 1. Facial Expressions (7 total)
1. **Happy** - Smiling face with curved mouth
2. **Sad** - Frowning face with downturned mouth
3. **Angry** - Furrowed brows with tight mouth
4. **Surprised** - Wide eyes with open mouth
5. **Wink** - One eye winking, playful smile
6. **Cool** - Sunglasses with confident smirk
7. **Love** - Heart eyes with smile (bonus!)

### 2. Customization Options

#### CLI Version:
- **Face Colors**: 8 options (Yellow, Blue, Green, Orange, Purple, Brown, White, Black)
- **Eye/Mouth Colors**: 6 options (Black, Red, Blue, Green, Purple, Brown)
- **Size**: Scale the face 1x, 2x, or 3x
- **Display Mode**: Toggle between color and monochrome
- **Array Type**: Switch between nested lists and NumPy arrays (optional)

#### GUI Version:
- **Face Colors**: 8 options with dropdown selection
- **Eye Colors**: 6 options with dropdown selection
- **Background Colors**: 3 options (White, Black, Blue)
- **Size Scale**: Normal (10x10), Large (20x20), Extra Large (30x30)
- **Mouse-clickable interface** with real-time preview

### 3. User Interface
- **CLI**: Menu-driven interface with keyboard input
- **GUI**: Tkinter-based windowed application with buttons and comboboxes
- Help section explaining how the program works
- User-friendly prompts and feedback

---

## How to Run

### Method 1: CLI Version (Terminal)

1. Open Command Prompt or Terminal
2. Navigate to the folder containing `4E13_preSBA2.py`
3. Run: `python 4E13_preSBA2.py`

### Method 2: GUI Version (Windowed Application)

1. Open Command Prompt or Terminal
2. Navigate to the folder containing `4E13_preSBA2_GUI.py`
3. Run: `python 4E13_preSBA2_GUI.py`

### Method 3: Run the Executable (Windows)

1. Navigate to the `dist` folder
2. Double-click `FacialExpression_4E13.exe`

### Method 4: Create Your Own EXE

#### Option A: Using the Batch File
1. Double-click `create_exe.bat`
2. Follow the on-screen instructions
3. The `.exe` file will be created in the `dist` folder

#### Option B: Manual Conversion
1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Convert to EXE:
   ```
   pyinstaller --onefile --windowed --name "FacialExpression_4E13" --clean 4E13_preSBA2_GUI.py
   ```

3. Find the `.exe` in the `dist` folder

---

## Requirements

- **Python 3.6 or higher**
- **tkinter** (for GUI version - included with Python)
- **NumPy library** (optional, for CLI NumPy array demonstration)
  ```
  pip install numpy
  ```

---

## File Structure

```
sba stuff/
│
├── 4E13_preSBA2.py            # CLI version (terminal-based)
├── 4E13_preSBA2_GUI.py        # GUI version (tkinter windowed)
├── create_exe.bat             # Batch file for EXE conversion
├── README_4E13_preSBA2.md     # This documentation file
├── FacialExpression_4E13.spec # PyInstaller spec file
│
├── build/                     # PyInstaller build folder (created after build)
│   └── FacialExpression_4E13/
│
└── dist/                      # Output folder (created after build)
    └── FacialExpression_4E13.exe  # Standalone executable
```

---

## Technical Highlights

### 1. 2D Array Storage
- Uses nested lists to store 10x10 facial patterns
- Template system with placeholder symbols (F, E, B) for color customization
- Each position in the array corresponds to a specific facial feature

### 2. Nested Loops
- Outer loop iterates through rows (0-9)
- Inner loop iterates through columns (0-9)
- Demonstrates fundamental programming concepts

### 3. Emoji Color System
- Uses Unicode emoji squares for colored rendering (🟨🟦🟩🟧🟪🟫⬜⬛🟥)
- Template-based color swapping for customization
- ANSI color codes for terminal UI elements

### 4. GUI with Tkinter
- Canvas-based rendering with colored rectangles
- Combobox dropdowns for color selection
- Event-driven interface with mouse clicks

### 5. NumPy Integration (CLI only)
- Alternative rendering using NumPy arrays
- Shows modern Python data handling

### 6. User Input Handling
- Menu system with multiple choice (CLI)
- Button clicks and dropdowns (GUI)
- Input validation and error handling

---

## Screenshots

### CLI Version Menu

When you run the CLI program, you'll see:

```
============================================================
     HKDSE ICT Pre-SBA 2: FACIAL EXPRESSION PROGRAM
============================================================

  Welcome! This program displays facial expressions using
  10x10 2D arrays and nested loops.

------------------------------------------------------------
  SELECT A FACIAL EXPRESSION:
------------------------------------------------------------
    [1] Happy
    [2] Sad
    [3] Angry
    [4] Surprised
    [5] Wink
    [6] Cool (Sunglasses)
    [7] Love (Bonus!)
------------------------------------------------------------
  SETTINGS:
    [C] Customize Colors
    [S] Change Size (Scale)
    [N] Show with NumPy Array
    [B] Toggle Color (Currently: ON)
    [H] Help / How it Works
    [Q] Quit Program
============================================================

  Enter your choice:
```

### GUI Version

The GUI version opens a window with:
- **Left panel**: Expression selection buttons
- **Center panel**: Face display canvas with colored rectangles
- **Right panel**: Customization dropdowns (Face Color, Eye Color, Background, Size)
- **Status bar**: Current settings display

---

## Conclusion

This program demonstrates:
- ✅ 10x10 2D array storage of facial patterns
- ✅ Nested loops for rendering
- ✅ 7 different facial expressions
- ✅ Template-based color customization system
- ✅ Dual versions: CLI (terminal) and GUI (tkinter)
- ✅ User-friendly interfaces (keyboard + mouse)
- ✅ Creative use of Unicode emojis
- ✅ Fully commented code
- ✅ Standalone executable generation with PyInstaller

---

**Submitted for**: HKDSE ICT Pre-SBA 2
**Submission Date**: 27/02/2026
**Deadline**: 27/02/2026 (Fri) 23:59:59
