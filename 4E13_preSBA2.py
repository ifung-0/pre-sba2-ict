# ============================================================================
# HKDSE ICT Pre-SBA 2: Facial Expression Program
# Author: Student
# Class: 4E
# Date: 2026-02-27
# Description: A Python program that displays facial expressions using 2D arrays
#              with nested loops, user menu, and customization options.
#              This is the CLI (Command Line Interface) version that runs in
#              the terminal.
# ============================================================================

# Import required libraries
# Note: NumPy is optional. If it's not installed in the current Python environment,
# the program will still run (NumPy mode will just be unavailable).
try:
    import numpy as np  # type: ignore
except ModuleNotFoundError:
    np = None  # type: ignore

import os
import sys

# ============================================================================
# EMOJI COLOR PALETTES
# Define different color schemes for faces using emoji variants
# ============================================================================
# This class stores all the colors used in the program.
# Each color is a Unicode emoji square that displays in the terminal.

class EmojiColors:
    """Class containing emoji color palettes for customization."""

    # Face/skin colors (8 options)
    YELLOW_FACE = "🟨"
    BLUE_FACE = "🟦"
    GREEN_FACE = "🟩"
    ORANGE_FACE = "🟧"
    PURPLE_FACE = "🟪"
    BROWN_FACE = "🟫"
    WHITE_FACE = "⬜"
    BLACK_FACE = "⬛"
    RED_FACE = "🟥"

    # Eye/mouth colors (6 options)
    BLACK_EYE = "⬛"
    RED_EYE = "🟥"
    BLUE_EYE = "🟦"
    GREEN_EYE = "🟩"
    PURPLE_EYE = "🟪"
    BROWN_EYE = "🟫"

    # Background colors (3 options)
    WHITE_BG = "⬜"
    BLACK_BG = "⬛"
    BLUE_BG = "🟦"

    @classmethod
    def get_face_colors(cls):
        """Return list of available face colors."""
        return {
            '1': ('Yellow', cls.YELLOW_FACE),
            '2': ('Blue', cls.BLUE_FACE),
            '3': ('Green', cls.GREEN_FACE),
            '4': ('Orange', cls.ORANGE_FACE),
            '5': ('Purple', cls.PURPLE_FACE),
            '6': ('Brown', cls.BROWN_FACE),
            '7': ('White', cls.WHITE_FACE),
            '8': ('Black', cls.BLACK_FACE),
        }

    @classmethod
    def get_eye_colors(cls):
        """Return list of available eye/mouth colors."""
        return {
            '1': ('Black', cls.BLACK_EYE),
            '2': ('Red', cls.RED_EYE),
            '3': ('Blue', cls.BLUE_EYE),
            '4': ('Green', cls.GREEN_EYE),
            '5': ('Purple', cls.PURPLE_EYE),
            '6': ('Brown', cls.BROWN_EYE),
        }

    @classmethod
    def get_bg_colors(cls):
        """Return list of available background colors."""
        return {
            '1': ('White', cls.WHITE_BG),
            '2': ('Black', cls.BLACK_BG),
            '3': ('Blue', cls.BLUE_BG),
        }


# ============================================================================
# ANSI COLOR CODES FOR TERMINAL OUTPUT (for UI elements)
# ============================================================================

class Colors:
    """Class containing ANSI color codes for terminal UI output."""
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'


# ============================================================================
# FACIAL EXPRESSION DATA - 10x10 2D ARRAYS WITH COLOR CUSTOMIZATION
# Each expression uses template system for color swapping
# ============================================================================
# How the 2D array works:
# - Each expression is a 10x10 grid (10 rows, 10 columns)
# - The grid uses three symbols:
#   F = Face (gets replaced with face color emoji)
#   E = Eye (gets replaced with eye color emoji)  
#   B = Background (gets replaced with background color emoji)
# - This template system lets you change colors without rewriting each expression

class FacialExpressions:
    """Class containing all facial expression patterns as 10x10 2D arrays."""

    # Template symbols that get replaced with colored emojis
    FACE_SYMBOL = "F"  # Will be replaced with face color emoji
    EYE_SYMBOL = "E"   # Will be replaced with eye color emoji
    BG_SYMBOL = "B"    # Will be replaced with background color emoji

    @staticmethod
    def _apply_colors(template, face_color, eye_color, bg_color):
        """Replace template symbols with actual colored emojis.
        
        How it works:
        1. Loop through each row in the 10x10 template
        2. Loop through each cell in the row
        3. Replace F with face color, E with eye color, B with background
        4. Return the colored 10x10 grid
        """
        result = []
        for row in template:
            new_row = []
            for cell in row:
                if cell == FacialExpressions.FACE_SYMBOL:
                    new_row.append(face_color)
                elif cell == FacialExpressions.EYE_SYMBOL:
                    new_row.append(eye_color)
                elif cell == FacialExpressions.BG_SYMBOL:
                    new_row.append(bg_color)
                else:
                    new_row.append(cell)
            result.append(new_row)
        return result

    @staticmethod
    def get_happy_face(face_color=None, eye_color=None, bg_color=None):
        """Return a 10x10 happy face grid. Features a curved smile pointing upward."""
        if face_color is None:
            face_color = EmojiColors.YELLOW_FACE
        if eye_color is None:
            eye_color = EmojiColors.BLACK_EYE
        if bg_color is None:
            bg_color = EmojiColors.WHITE_BG

        template = [
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["F", "F", "E", "E", "F", "F", "E", "E", "F", "F"],
            ["F", "F", "E", "E", "F", "F", "E", "E", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "E", "F", "F", "F", "F", "F", "F", "E", "F"],
            ["F", "F", "E", "F", "F", "F", "F", "E", "F", "F"],
            ["F", "F", "F", "E", "E", "E", "E", "F", "F", "F"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"]
        ]
        return FacialExpressions._apply_colors(template, face_color, eye_color, bg_color)

    @staticmethod
    def get_sad_face(face_color=None, eye_color=None, bg_color=None):
        """Return a 10x10 sad face grid. Features a downturned mouth."""
        if face_color is None:
            face_color = EmojiColors.YELLOW_FACE
        if eye_color is None:
            eye_color = EmojiColors.BLACK_EYE
        if bg_color is None:
            bg_color = EmojiColors.WHITE_BG
            
        template = [
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["F", "F", "E", "E", "F", "F", "E", "E", "F", "F"],
            ["F", "F", "E", "E", "F", "F", "E", "E", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "F", "E", "E", "E", "E", "F", "F", "F"],
            ["F", "F", "E", "F", "F", "F", "F", "E", "F", "F"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"]
        ]
        return FacialExpressions._apply_colors(template, face_color, eye_color, bg_color)
    
    @staticmethod
    def get_angry_face(face_color=None, eye_color=None, bg_color=None):
        """
        Returns a 10x10 2D array representing an ANGRY face.
        Features: Emoji face with slanted angry eyebrows and tight mouth
        """
        if face_color is None:
            face_color = EmojiColors.YELLOW_FACE
        if eye_color is None:
            eye_color = EmojiColors.BLACK_EYE
        if bg_color is None:
            bg_color = EmojiColors.WHITE_BG
            
        template = [
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["F", "F", "E", "F", "F", "F", "F", "E", "F", "F"],
            ["F", "F", "F", "E", "F", "F", "E", "F", "F", "F"],
            ["F", "F", "E", "E", "F", "F", "E", "E", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "F", "E", "E", "E", "E", "F", "F", "F"],
            ["F", "F", "E", "F", "F", "F", "F", "E", "F", "F"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"]
        ]
        return FacialExpressions._apply_colors(template, face_color, eye_color, bg_color)
    
    @staticmethod
    def get_surprised_face(face_color=None, eye_color=None, bg_color=None):
        """
        Returns a 10x10 2D array representing a SURPRISED face.
        Features: Emoji face with raised eyebrows and open mouth
        """
        if face_color is None:
            face_color = EmojiColors.YELLOW_FACE
        if eye_color is None:
            eye_color = EmojiColors.BLACK_EYE
        if bg_color is None:
            bg_color = EmojiColors.WHITE_BG
            
        template = [
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"],
            ["B", "F", "E", "E", "F", "F", "E", "E", "F", "B"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "E", "E", "F", "F", "E", "E", "F", "F"],
            ["F", "F", "E", "E", "F", "F", "E", "E", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "E", "E", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "E", "E", "F", "F", "F", "F"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"]
        ]
        return FacialExpressions._apply_colors(template, face_color, eye_color, bg_color)
    
    @staticmethod
    def get_wink_face(face_color=None, eye_color=None, bg_color=None):
        """
        Returns a 10x10 2D array representing a WINK face.
        Features: Emoji face with one eye closed (winking) and playful smile
        """
        if face_color is None:
            face_color = EmojiColors.YELLOW_FACE
        if eye_color is None:
            eye_color = EmojiColors.BLACK_EYE
        if bg_color is None:
            bg_color = EmojiColors.WHITE_BG
            
        template = [
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["F", "F", "E", "E", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "E", "E", "F", "F", "E", "E", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "E", "F", "F", "F", "F", "F", "F", "E", "F"],
            ["F", "F", "E", "F", "F", "F", "F", "E", "F", "F"],
            ["F", "F", "F", "E", "E", "E", "E", "F", "F", "F"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"]
        ]
        return FacialExpressions._apply_colors(template, face_color, eye_color, bg_color)
    
    @staticmethod
    def get_cool_face(face_color=None, eye_color=None, bg_color=None):
        """
        Returns a 10x10 2D array representing a COOL face with sunglasses.
        Features: Emoji face with colored sunglasses and confident smirk
        """
        if face_color is None:
            face_color = EmojiColors.YELLOW_FACE
        if eye_color is None:
            eye_color = EmojiColors.BLACK_EYE
        if bg_color is None:
            bg_color = EmojiColors.WHITE_BG
            
        template = [
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["F", "E", "E", "E", "E", "E", "E", "E", "E", "F"],
            ["F", "E", "E", "E", "F", "F", "E", "E", "E", "F"],
            ["F", "F", "E", "F", "F", "F", "F", "E", "F", "F"],
            ["F", "E", "F", "F", "F", "F", "F", "F", "E", "F"],
            ["F", "F", "E", "F", "F", "F", "F", "E", "F", "F"],
            ["F", "F", "F", "E", "E", "E", "E", "F", "F", "F"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"]
        ]
        return FacialExpressions._apply_colors(template, face_color, eye_color, bg_color)
    
    @staticmethod
    def get_love_face(face_color=None, eye_color=None, bg_color=None):
        """
        Returns a 10x10 2D array representing a LOVE/HEART-EYES face.
        Features: Emoji face with red heart-shaped eyes and affectionate smile
        """
        if face_color is None:
            face_color = EmojiColors.YELLOW_FACE
        if eye_color is None:
            eye_color = EmojiColors.RED_EYE  # Hearts are red by default
        if bg_color is None:
            bg_color = EmojiColors.WHITE_BG
            
        template = [
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["F", "E", "F", "E", "F", "F", "E", "F", "E", "F"],
            ["F", "E", "E", "E", "F", "F", "E", "E", "E", "F"],
            ["F", "F", "E", "F", "F", "F", "F", "E", "F", "F"],
            ["F", "E", "F", "F", "F", "F", "F", "F", "E", "F"],
            ["F", "F", "E", "F", "F", "F", "F", "E", "F", "F"],
            ["F", "F", "F", "E", "E", "E", "E", "F", "F", "F"],
            ["B", "F", "F", "F", "F", "F", "F", "F", "F", "B"],
            ["B", "B", "B", "F", "F", "F", "F", "B", "B", "B"]
        ]
        return FacialExpressions._apply_colors(template, face_color, eye_color, bg_color)


# ============================================================================
# FACIAL EXPRESSION RENDERER CLASS
# This class handles the display and customization of facial expressions
# ============================================================================

class FaceRenderer:
    """
    Class responsible for rendering facial expressions with customization options.
    Uses nested loops to iterate through the 2D array and display the face.
    """
    
    def __init__(self):
        """Initialize the renderer with default settings."""
        self.scale = 1  # Default scale factor
        self.use_color = True  # Default to using colors
        self.face_color = EmojiColors.YELLOW_FACE
        self.eye_color = EmojiColors.BLACK_EYE
        self.bg_color = EmojiColors.WHITE_BG
    
    def set_scale(self, scale):
        """
        Set the scale factor for the face display.
        
        Args:
            scale (int): Scale factor (1 = normal, 2 = double size, etc.)
        """
        self.scale = max(1, min(scale, 3))  # Limit scale between 1 and 3
    
    def set_colors(self, face_color, eye_color, bg_color=None):
        """
        Set custom colors for different parts of the face.
        
        Args:
            face_color (str): Emoji for face color
            eye_color (str): Emoji for eye/mouth color
            bg_color (str): Emoji for background color
        """
        self.face_color = face_color
        self.eye_color = eye_color
        if bg_color:
            self.bg_color = bg_color
    
    def toggle_color(self):
        """Toggle between color and monochrome mode."""
        self.use_color = not self.use_color
        if not self.use_color:
            # Set to monochrome (black and white)
            self.face_color = EmojiColors.WHITE_FACE
            self.eye_color = EmojiColors.BLACK_EYE
            self.bg_color = EmojiColors.BLACK_BG
        else:
            # Restore default colors
            self.face_color = EmojiColors.YELLOW_FACE
            self.eye_color = EmojiColors.BLACK_EYE
            self.bg_color = EmojiColors.WHITE_BG
        return self.use_color
    
    def get_face_with_colors(self, face_template_func):
        """Get a face with current color settings applied."""
        if self.use_color:
            return face_template_func(self.face_color, self.eye_color, self.bg_color)
        else:
            # Monochrome version
            return face_template_func(EmojiColors.WHITE_FACE, EmojiColors.BLACK_EYE, EmojiColors.BLACK_BG)
    
    def render_face(self, face_array, use_color=True):
        """
        Render a facial expression using nested loops to iterate through the 2D array.

        This is the KEY FUNCTION that demonstrates nested loops:
        
        OUTER LOOP (rows):
        - Goes through each row from 0 to 9 (top to bottom)
        - For each row, it may repeat 'scale' times for vertical scaling
        
        INNER LOOP (columns):
        - Goes through each column from 0 to 9 (left to right)
        - Gets the emoji at position [row][column]
        - Adds it to the line being built
        
        After the inner loop finishes, the complete line is printed.
        
        Args:
            face_array (list): 10x10 2D array representing the face
            use_color (bool): Whether to apply color formatting
        """
        # Clear the screen for better display
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n" + "=" * 50)
        print("         FACIAL EXPRESSION DISPLAY")
        print("=" * 50 + "\n")

        # OUTER LOOP: Iterate through each row of the 2D array
        # This loop runs 10 times (once for each row: 0, 1, 2, ... 9)
        for row_index in range(len(face_array)):

            # Apply vertical scaling - repeat each row 'scale' times
            # If scale=2, each row prints twice to make the face taller
            for _ in range(self.scale):
                line = ""

                # INNER LOOP: Iterate through each column in the current row
                # This loop runs 10 times (once for each column: 0, 1, 2, ... 9)
                for col_index in range(len(face_array[row_index])):
                    # Get the symbol at this position in the 2D array
                    # Example: face_array[2][3] gets row 2, column 3
                    symbol = face_array[row_index][col_index]
                    line += symbol

                # Print the completed line
                # After inner loop finishes, we have a complete row of emojis
                print(line)

        print("\n" + "=" * 50)
    
    def render_face_numpy(self, face_array, use_color=True):
        """
        Alternative rendering method using NumPy arrays.
        """
        if np is None:
            raise RuntimeError("NumPy is not installed. Install it with: pip install numpy")

        np_array = np.array(face_array)
        
        print("\n" + "=" * 50)
        print("    FACIAL EXPRESSION (NumPy Array Version)")
        print("=" * 50 + "\n")
        
        rows, cols = np_array.shape
        print(f"Array Dimensions: {rows} rows x {cols} columns\n")
        
        # Iterate through the NumPy array using nested loops
        for i in range(rows):
            line = ""
            for j in range(cols):
                symbol = np_array[i, j]
                line += symbol
            
            # Print each row 'scale' times for vertical scaling
            for _ in range(self.scale):
                print(line)
        
        print("\n" + "=" * 50)


# ============================================================================
# USER INTERFACE CLASS
# Handles menu display and user input
# ============================================================================

class UserInterface:
    """Class responsible for handling user interaction and menu display."""
    
    def __init__(self):
        """Initialize the UI with available expressions and renderer."""
        self.expressions = FacialExpressions()
        self.renderer = FaceRenderer()
        self.current_face = None
        self.use_numpy = False

        # History for Undo/Redo
        self.history = []
        self.history_index = -1
        self.max_history = 50

        # Custom expression
        self.custom_grid = None
        self.is_custom_mode = False

        # Dictionary mapping menu choices to expression methods
        self.menu_options = {
            '1': ('Happy', self.expressions.get_happy_face),
            '2': ('Sad', self.expressions.get_sad_face),
            '3': ('Angry', self.expressions.get_angry_face),
            '4': ('Surprised', self.expressions.get_surprised_face),
            '5': ('Wink', self.expressions.get_wink_face),
            '6': ('Cool (Sunglasses)', self.expressions.get_cool_face),
            '7': ('Love (Bonus!)', self.expressions.get_love_face),
        }

        # Save initial state
        self._save_to_history()
    
    def display_main_menu(self):
        """Display the main menu with all available options."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 60)
        print("     HKDSE ICT Pre-SBA 2: FACIAL EXPRESSION PROGRAM")
        print("=" * 60)
        print("\n  Welcome! This program displays facial expressions using")
        print("  10x10 2D arrays and nested loops.\n")
        print("-" * 60)
        print("  SELECT A FACIAL EXPRESSION:")
        print("-" * 60)

        # Display menu options using a loop
        for key, (name, _) in self.menu_options.items():
            print(f"    [{key}] {name}")

        print("-" * 60)
        print("  SETTINGS:")
        print("    [C] Customize Colors")
        print("    [S] Change Size (Scale)")
        print("    [N] Show with NumPy Array")
        print(f"    [B] Toggle Color (Currently: {'ON' if self.renderer.use_color else 'OFF'})")
        print("-" * 60)
        print("  NEW FEATURES:")
        print("    [R] Random Face Generator")
        print("    [E] Custom Expression Editor")
        print("    [X] Export to Text File")
        print("    [U] Undo | [Y] Redo")
        print("-" * 60)
        print("  [H] Help / How it Works")
        print("    [Q] Quit Program")
        print("=" * 60)
    
    def display_color_menu(self):
        """Display the color customization menu."""
        print("\n" + "-" * 50)
        print("  COLOR CUSTOMIZATION OPTIONS:")
        print("-" * 50)

        print("  Face Colors:")
        face_colors = EmojiColors.get_face_colors()
        for key, (name, emoji) in face_colors.items():
            print(f"    [{key}] {name} {emoji}")

        print("\n  Eye/Mouth Colors:")
        eye_colors = EmojiColors.get_eye_colors()
        for key, (name, emoji) in eye_colors.items():
            print(f"    [{key}] {name} {emoji}")

        print("\n  Background Colors:")
        bg_colors = EmojiColors.get_bg_colors()
        for key, (name, emoji) in bg_colors.items():
            print(f"    [{key}] {name} {emoji}")

        print("-" * 50)
    
    def customize_colors(self):
        """Handle color customization user input."""
        self.display_color_menu()

        # Get face color choice
        face_choice = input("\n  Select face color (1-8): ").strip()
        face_colors = EmojiColors.get_face_colors()

        # Get eye color choice
        eye_choice = input("  Select eye/mouth color (1-6): ").strip()
        eye_colors = EmojiColors.get_eye_colors()

        # Get background color choice
        bg_choice = input("  Select background color (1-3): ").strip()
        bg_colors = EmojiColors.get_bg_colors()

        # Apply the selected colors if valid
        if face_choice in face_colors and eye_choice in eye_colors:
            face_name, face_emoji = face_colors[face_choice]
            eye_name, eye_emoji = eye_colors[eye_choice]

            # Apply background color if valid, otherwise use default
            if bg_choice in bg_colors:
                bg_name, bg_emoji = bg_colors[bg_choice]
                self.renderer.set_colors(face_emoji, eye_emoji, bg_emoji)
                print(f"\n  ✓ Colors updated: Face={face_name}, Eyes={eye_name}, Background={bg_name}")
            else:
                self.renderer.set_colors(face_emoji, eye_emoji)
                print(f"\n  ✓ Colors updated: Face={face_name}, Eyes={eye_name} (Background unchanged)")
        else:
            print("\n  ✗ Invalid choice. Colors unchanged.")

        input("\n  Press Enter to continue...")
    
    def change_scale(self):
        """Handle scale/size customization."""
        print("\n" + "-" * 50)
        print("  SIZE CUSTOMIZATION:")
        print("-" * 50)
        print(f"  Current scale: {self.renderer.scale}x")
        print("\n  Select scale:")
        print("    [1] Normal (10x10)")
        print("    [2] Large (20x20)")
        print("    [3] Extra Large (30x30)")
        print("-" * 50)
        
        scale_choice = input("\n  Enter choice (1-3): ").strip()
        if scale_choice in ['1', '2', '3']:
            self.renderer.set_scale(int(scale_choice))
            print(f"\n  ✓ Scale updated to {self.renderer.scale}x!")
        else:
            print("\n  ✗ Invalid choice. Scale unchanged.")
        
        input("\n  Press Enter to continue...")
    
    def display_help(self):
        """Display help information about how the program works."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 60)
        print("           HOW THE PROGRAM WORKS")
        print("=" * 60)
        print("""
  1. 2D ARRAY STORAGE:
     Each facial expression is stored as a 10x10 2D array template.
     Templates use placeholder symbols (F, E, B) that get replaced
     with colored emoji characters:
       F = Face color (e.g., 🟨 yellow)
       E = Eye color (e.g., ⬛ black)
       B = Background color (e.g., ⬜ white)
     
     Example template:
     [
       ["B", "B", "F", "F", "B", "B"],  <- Background corners, face center
       ["B", "F", "F", "F", "F", "B"],  <- Face expands
       ["F", "F", "E", "E", "F", "F"],  <- Eyes appear
       ... (continues for 10 rows)
     ]
  
  2. COLOR CUSTOMIZATION:
     The program swaps emoji colors based on user selection:
     - Face colors: Yellow 🟨, Blue 🟦, Green 🟩, Orange 🟧, etc.
     - Eye colors: Black ⬛, Red 🟥, Blue 🟦, Green 🟩, etc.
     - Toggle Color: Switches between color and monochrome (B&W)
  
  3. NESTED LOOPS RENDERING:
     The program uses nested loops to display the face:
     
     OUTER LOOP (for each row):
         → Iterates through rows 0 to 9
         
         INNER LOOP (for each column in the row):
             → Iterates through columns 0 to 9
             → Prints the emoji at array[row][column]
  
  4. NumPy MODE:
     Uses numpy arrays for storage and display, demonstrating
     alternative 2D array handling with the same visual output.
        """)
        print("=" * 60)
        input("\n  Press Enter to return to main menu...")

    def _save_to_history(self):
        """Save current state to history for Undo functionality."""
        state = {
            'renderer_scale': self.renderer.scale,
            'renderer_use_color': self.renderer.use_color,
            'renderer_face_color': self.renderer.face_color,
            'renderer_eye_color': self.renderer.eye_color,
            'renderer_bg_color': self.renderer.bg_color,
            'custom_grid': self.custom_grid,
            'is_custom_mode': self.is_custom_mode
        }
        
        # Remove any future states if we're not at the end
        if self.history_index < len(self.history) - 1:
            self.history = self.history[:self.history_index + 1]
        
        # Add new state
        self.history.append(state)
        
        # Limit history size
        if len(self.history) > self.max_history:
            self.history.pop(0)
        else:
            self.history_index += 1

    def _undo(self):
        """Undo the last change."""
        if self.history_index > 0:
            self.history_index -= 1
            state = self.history[self.history_index]
            self._restore_state(state)
            print("\n  ✓ Undo successful!")
        else:
            print("\n  ⚠ Nothing to undo.")
        input("\n  Press Enter to continue...")

    def _redo(self):
        """Redo the last undone change."""
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            state = self.history[self.history_index]
            self._restore_state(state)
            print("\n  ✓ Redo successful!")
        else:
            print("\n  ⚠ Nothing to redo.")
        input("\n  Press Enter to continue...")

    def _restore_state(self, state):
        """Restore a saved state."""
        self.renderer.scale = state['renderer_scale']
        self.renderer.use_color = state['renderer_use_color']
        self.renderer.face_color = state['renderer_face_color']
        self.renderer.eye_color = state['renderer_eye_color']
        self.renderer.bg_color = state['renderer_bg_color']
        self.custom_grid = state['custom_grid']
        self.is_custom_mode = state['is_custom_mode']

    def random_face(self):
        """Generate a random face with random expression and colors."""
        import random
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 60)
        print("          🎲 RANDOM FACE GENERATOR")
        print("=" * 60)
        
        # Pick random expression
        expressions = list(self.menu_options.keys())
        random_expr = random.choice(expressions)
        
        # Pick random colors
        face_colors = EmojiColors.get_face_colors()
        eye_colors = EmojiColors.get_eye_colors()
        bg_colors = EmojiColors.get_bg_colors()
        
        random_face_key = random.choice(list(face_colors.keys()))
        random_eye_key = random.choice(list(eye_colors.keys()))
        random_bg_key = random.choice(list(bg_colors.keys()))
        
        face_emoji = face_colors[random_face_key][1]
        eye_emoji = eye_colors[random_eye_key][1]
        bg_emoji = bg_colors[random_bg_key][1]
        
        # Set random scale
        random_scale = random.randint(1, 3)
        self.renderer.set_scale(random_scale)
        
        # Apply colors
        self.renderer.set_colors(
            face_emoji,
            eye_emoji,
            bg_emoji
        )
        
        # Reset custom mode
        self.is_custom_mode = False
        self.custom_grid = None
        
        # Render the face
        name, get_face = self.menu_options[random_expr]
        self.current_face = self.renderer.get_face_with_colors(get_face)
        self.renderer.render_face(self.current_face, self.renderer.use_color)
        
        print(f"\n  🎲 Random Expression: {name}")
        print(f"  Scale: {random_scale}x")
        print(f"  Face: {face_colors[random_face_key][0]} {face_emoji}")
        print(f"  Eyes: {eye_colors[random_eye_key][0]} {eye_emoji}")
        print(f"  Background: {bg_colors[random_bg_key][0]} {bg_emoji}")
        
        self._save_to_history()
        input("\n  Press Enter to continue...")

    def custom_expression_editor(self):
        """Open custom expression editor in terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 60)
        print("        ✏️  CUSTOM EXPRESSION EDITOR")
        print("=" * 60)
        print("\n  Create your own 10x10 facial expression!")
        print("\n  Legend:")
        print("    F = Face color  |  E = Eye color  |  B = Background")
        print("\n  Instructions:")
        print("  1. Enter each row as 10 characters (F, E, or B)")
        print("  2. Press Enter after each row")
        print("  3. Type 'cancel' anytime to exit")
        print("  4. Type 'clear' to clear current row")
        print("-" * 60)
        
        # Initialize custom grid
        custom_grid = []
        
        for row in range(10):
            while True:
                row_input = input(f"  Row {row + 1}/10: ").strip().upper()
                
                if row_input == 'CANCEL':
                    print("\n  Custom editor cancelled.")
                    input("  Press Enter to continue...")
                    return
                
                if row_input == 'CLEAR':
                    print(f"  Row {row + 1} cleared.")
                    continue
                
                # Validate input
                if len(row_input) != 10:
                    print(f"  ⚠ Row must be exactly 10 characters. You entered {len(row_input)}.")
                    continue
                
                # Check for valid characters
                valid = True
                for char in row_input:
                    if char not in ['F', 'E', 'B']:
                        valid = False
                        break
                
                if not valid:
                    print("  ⚠ Only F (Face), E (Eye), and B (Background) are allowed.")
                    continue
                
                # Convert to colored grid
                colored_row = []
                for char in row_input:
                    if char == 'F':
                        colored_row.append(self.renderer.face_color)
                    elif char == 'E':
                        colored_row.append(self.renderer.eye_color)
                    else:
                        colored_row.append(self.renderer.bg_color)
                
                custom_grid.append(colored_row)
                break
        
        # Save custom expression
        self.custom_grid = custom_grid
        self.is_custom_mode = True
        
        print("\n  ✓ Custom expression created!")
        
        # Render it
        self.renderer.render_face(custom_grid, self.renderer.use_color)
        
        print("\n  Your custom face is displayed above.")
        print("  It will remain active until you select a preset expression.")
        
        self._save_to_history()
        input("\n  Press Enter to continue...")

    def export_to_file(self):
        """Export the current face to a text file."""
        if self.current_face is None:
            print("\n  ⚠ No face to export. Please select an expression first.")
            input("\n  Press Enter to continue...")
            return
        
        # Generate filename
        timestamp = __import__('datetime').datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"FacialExpression_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=" * 50 + "\n")
                f.write("   FACIAL EXPRESSION EXPORT\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Exported: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Scale: {self.renderer.scale}x\n")
                f.write(f"Color Mode: {'ON' if self.renderer.use_color else 'OFF'}\n")
                f.write(f"Face: {self.renderer.face_color}\n")
                f.write(f"Eyes: {self.renderer.eye_color}\n")
                f.write(f"Background: {self.renderer.bg_color}\n\n")
                f.write("-" * 50 + "\n")
                f.write("FACE DISPLAY:\n")
                f.write("-" * 50 + "\n\n")
                
                # Write the face
                for row in self.current_face:
                    for cell in row:
                        f.write(cell)
                    f.write("\n")
                
                f.write("\n" + "=" * 50 + "\n")
                f.write("HKDSE ICT Pre-SBA 2 - Facial Expression Program\n")
                f.write("=" * 50 + "\n")
            
            print(f"\n  ✓ Face exported to: {filename}")
            
        except Exception as e:
            print(f"\n  ✗ Export failed: {e}")
        
        input("\n  Press Enter to continue...")
    
    def run(self):
        """Main program loop - handles user interaction."""

        while True:
            self.display_main_menu()
            choice = input("\n  Enter your choice: ").strip().upper()

            # Handle expression selection
            if choice in self.menu_options:
                name, get_face = self.menu_options[choice]
                
                # If in custom mode, exit it
                if self.is_custom_mode:
                    self.is_custom_mode = False
                    self.custom_grid = None
                
                self.current_face = self.renderer.get_face_with_colors(get_face)

                # Render using selected method
                if self.use_numpy:
                    self.renderer.render_face_numpy(self.current_face, self.renderer.use_color)
                else:
                    self.renderer.render_face(self.current_face, self.renderer.use_color)

                print(f"\n  Expression: {name}")
                print(f"  Scale: {self.renderer.scale}x | Color: {'ON' if self.renderer.use_color else 'OFF'}")
                if self.renderer.use_color:
                    print(f"  Face: {self.renderer.face_color} | Eyes: {self.renderer.eye_color}")
                self._save_to_history()
                input("\n  Press Enter to continue...")

            # Handle settings
            elif choice == 'C':
                self.customize_colors()
                self._save_to_history()

            elif choice == 'S':
                self.change_scale()
                self._save_to_history()

            elif choice == 'N':
                if np is None:
                    print("\n  NumPy is not installed, so NumPy mode is unavailable.")
                    print("  Tip: install it with: pip install numpy")
                    print("  NumPy mode will remain OFF until NumPy is installed.")
                    self.use_numpy = False
                else:
                    self.use_numpy = not self.use_numpy
                    status = "ON" if self.use_numpy else "OFF"
                    print(f"\n  NumPy mode: {status}")
                input("\n  Press Enter to continue...")

            elif choice == 'B':
                new_state = self.renderer.toggle_color()
                status = "ON" if new_state else "OFF"
                print(f"\n  Color toggled: {status}")
                if not new_state:
                    print("  (Monochrome mode: white face, black eyes, black background)")
                else:
                    print("  (Color mode: yellow face, black eyes, white background)")
                self._save_to_history()
                input("\n  Press Enter to continue...")

            # New features
            elif choice == 'R':
                self.random_face()

            elif choice == 'E':
                self.custom_expression_editor()

            elif choice == 'X':
                self.export_to_file()

            elif choice == 'U':
                self._undo()

            elif choice == 'Y':
                self._redo()

            elif choice == 'H':
                self.display_help()

            elif choice == 'Q':
                print("\n  Thank you for using the Facial Expression Program!")
                print("  Goodbye! 👋\n")
                break

            else:
                print("\n  ✗ Invalid choice. Please try again.")
                input("\n  Press Enter to continue...")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        app = UserInterface()
        app.run()
    except KeyboardInterrupt:
        print("\n\n  Program interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n  An error occurred: {e}")
        sys.exit(1)