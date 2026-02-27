# ============================================================================
# HKDSE ICT Pre-SBA 2: Facial Expression Program
# Author: Student
# Class: 4E
# Date: 2026-02-27
# Description: A Python program that displays facial expressions using 2D arrays
#              with nested loops, user menu, and customization options.
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

class EmojiColors:
    """Class containing emoji color palettes for customization."""
    
    # Face/skin colors
    YELLOW_FACE = "🟨"
    BLUE_FACE = "🟦"
    GREEN_FACE = "🟩"
    ORANGE_FACE = "🟧"
    PURPLE_FACE = "🟪"
    BROWN_FACE = "🟫"
    WHITE_FACE = "⬜"
    BLACK_FACE = "⬛"
    RED_FACE = "🟥"
    
    # Eye/mouth colors
    BLACK_EYE = "⬛"
    RED_EYE = "🟥"
    BLUE_EYE = "🟦"
    GREEN_EYE = "🟩"
    PURPLE_EYE = "🟪"
    BROWN_EYE = "🟫"
    
    # Background colors
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

class FacialExpressions:
    """Class containing all facial expression patterns as 10x10 2D arrays."""
    
    # Template symbols that get replaced with colored emojis
    FACE_SYMBOL = "F"  # Will be replaced with face color emoji
    EYE_SYMBOL = "E"   # Will be replaced with eye color emoji
    BG_SYMBOL = "B"    # Will be replaced with background color emoji
    
    @staticmethod
    def _apply_colors(template, face_color, eye_color, bg_color):
        """Replace template symbols with actual colored emojis."""
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
        """
        Returns a 10x10 2D array representing a HAPPY face.
        Features: Emoji face with colored eyes and smile
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
        """
        Returns a 10x10 2D array representing a SAD face.
        Features: Emoji face with colored eyes and downturned mouth
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
        for row_index in range(len(face_array)):
            
            # Apply vertical scaling - repeat each row 'scale' times
            for _ in range(self.scale):
                line = ""
                
                # INNER LOOP: Iterate through each column in the current row
                for col_index in range(len(face_array[row_index])):
                    # Get the symbol at this position in the 2D array
                    symbol = face_array[row_index][col_index]
                    line += symbol
                
                # Print the completed line
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
        print("    [H] Help / How it Works")
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
        
        # Apply the selected colors if valid
        if face_choice in face_colors and eye_choice in eye_colors:
            face_name, face_emoji = face_colors[face_choice]
            eye_name, eye_emoji = eye_colors[eye_choice]
            
            self.renderer.set_colors(face_emoji, eye_emoji)
            print(f"\n  ✓ Colors updated: Face={face_name}, Eyes={eye_name}")
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
    
    def run(self):
        """Main program loop - handles user interaction."""
        
        while True:
            self.display_main_menu()
            choice = input("\n  Enter your choice: ").strip().upper()
            
            # Handle expression selection
            if choice in self.menu_options:
                name, get_face = self.menu_options[choice]
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
                input("\n  Press Enter to continue...")
            
            # Handle settings
            elif choice == 'C':
                self.customize_colors()
            
            elif choice == 'S':
                self.change_scale()
            
            elif choice == 'N':
                if np is None:
                    print("\n  NumPy is not installed, so NumPy mode is unavailable.")
                    print("  Tip: install it with: pip install numpy")
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
                input("\n  Press Enter to continue...")
            
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