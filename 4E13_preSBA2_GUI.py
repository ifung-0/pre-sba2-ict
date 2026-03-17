# ============================================================================
# HKDSE ICT Pre-SBA 2: Facial Expression Program (GUI Version)
# Author: Student
# Class: 4E
# Date: 2026-02-27
# Description: A Python GUI program that displays facial expressions using
#              2D arrays with mouse-clickable interface using tkinter.
#              This version uses a graphical window with buttons and dropdowns.
# Version: 1.0.0
# ============================================================================

# Import required libraries for building the graphical interface
import tkinter as tk
from tkinter import ttk, messagebox, font
import sys

# ============================================================================
# EMOJI COLOR PALETTES - Using actual colors for Canvas rendering
# ============================================================================
# This class stores all the colors used in the program.
# Each color has two parts: a hex code (for drawing) and an emoji (for display).

class EmojiColors:
    """Class containing color palettes for canvas rendering."""

    # Face/skin colors (using actual hex colors for Canvas)
    # Format: (hex_code_for_drawing, emoji_for_display)
    YELLOW_FACE = ("#FFD93D", "🟨")
    BLUE_FACE = ("#4A90D9", "🟦")
    GREEN_FACE = ("#5CB85C", "🟩")
    ORANGE_FACE = ("#FF8C42", "🟧")
    PURPLE_FACE = ("#9B59B6", "🟪")
    BROWN_FACE = ("#8B4513", "🟫")
    WHITE_FACE = ("#FFFFFF", "⬜")
    BLACK_FACE = ("#1a1a1a", "⬛")
    RED_FACE = ("#E74C3C", "🟥")

    # Eye/mouth colors
    BLACK_EYE = ("#1a1a1a", "⬛")
    RED_EYE = ("#E74C3C", "🟥")
    BLUE_EYE = ("#4A90D9", "🟦")
    GREEN_EYE = ("#5CB85C", "🟩")
    PURPLE_EYE = ("#9B59B6", "🟪")
    BROWN_EYE = ("#8B4513", "🟫")

    # Background colors
    WHITE_BG = ("#FFFFFF", "⬜")
    BLACK_BG = ("#1a1a1a", "⬛")
    BLUE_BG = ("#4A90D9", "🟦")

    @classmethod
    def get_face_colors(cls):
        """Return list of available face colors."""
        return {
            'Yellow': cls.YELLOW_FACE,
            'Blue': cls.BLUE_FACE,
            'Green': cls.GREEN_FACE,
            'Orange': cls.ORANGE_FACE,
            'Purple': cls.PURPLE_FACE,
            'Brown': cls.BROWN_FACE,
            'White': cls.WHITE_FACE,
            'Black': cls.BLACK_FACE,
        }

    @classmethod
    def get_eye_colors(cls):
        """Return list of available eye/mouth colors."""
        return {
            'Black': cls.BLACK_EYE,
            'Red': cls.RED_EYE,
            'Blue': cls.BLUE_EYE,
            'Green': cls.GREEN_EYE,
            'Purple': cls.PURPLE_EYE,
            'Brown': cls.BROWN_EYE,
        }

    @classmethod
    def get_bg_colors(cls):
        """Return list of available background colors."""
        return {
            'White': cls.WHITE_BG,
            'Black': cls.BLACK_BG,
            'Blue': cls.BLUE_BG,
        }


# ============================================================================
# FACIAL EXPRESSION DATA - 10x10 2D ARRAYS
# ============================================================================
# Each facial expression is stored as a 10x10 grid (10 rows, 10 columns).
# The grid uses three symbols:
#   F = Face (gets replaced with face color)
#   E = Eye (gets replaced with eye color)
#   B = Background (gets replaced with background color)
# This template system lets you change colors without rewriting each expression.

class FacialExpressions:
    """Class containing all facial expression patterns as 10x10 2D arrays."""

    # Template symbols that get replaced with colored emojis
    FACE_SYMBOL = "F"  # Will be replaced with face color emoji
    EYE_SYMBOL = "E"   # Will be replaced with eye color emoji
    BG_SYMBOL = "B"    # Will be replaced with background color emoji

    @staticmethod
    def _apply_colors(template, face_color, eye_color, bg_color):
        """Replace template symbols with actual colors.
        
        How it works:
        1. Loop through each row in the template
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
        """Return a 10x10 angry face grid. Features slanted eyebrows pointing inward."""
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
        """Return a 10x10 surprised face grid. Features wide eyes and an open mouth."""
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
        """Return a 10x10 winking face grid. Features one closed eye (right side)."""
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
        """Return a 10x10 cool face grid. Features large sunglasses covering both eyes."""
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
        """Return a 10x10 love face grid. Features heart-shaped eyes (red by default)."""
        if face_color is None:
            face_color = EmojiColors.YELLOW_FACE
        if eye_color is None:
            eye_color = EmojiColors.RED_EYE
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
# MAIN GUI APPLICATION
# ============================================================================
# This class creates the graphical user interface with:
# - Buttons for selecting expressions
# - Dropdown menus for colors and size
# - A canvas that draws the face using colored rectangles
# - Keyboard shortcuts for quick access

class FacialExpressionGUI:
    """Main GUI application for displaying facial expressions."""

    def __init__(self, root):
        """Initialize the GUI application.
        
        Sets up:
        1. Main window with title and size
        2. All GUI widgets (buttons, dropdowns, canvas)
        3. Keyboard shortcuts
        4. Initial display
        """
        self.root = root
        self.root.title("HKDSE ICT Pre-SBA 2: Facial Expression Program v1.0.0")
        self.root.geometry("1100x750")
        self.root.minsize(900, 650)

        # Set style
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Initialize expression data
        self.expressions = FacialExpressions()
        self.face_colors = EmojiColors.get_face_colors()
        self.eye_colors = EmojiColors.get_eye_colors()
        self.bg_colors = EmojiColors.get_bg_colors()

        # Current settings
        self.current_face_color = "Yellow"
        self.current_eye_color = "Black"
        self.current_bg_color = "White"
        self.scale = 1
        self.current_expression = "Happy"

        # History for Undo/Redo (stores tuples of settings)
        self.history = []
        self.history_index = -1
        self.max_history = 50

        # Custom expression editor data (10x10 grid)
        self.custom_grid = None
        self.is_custom_mode = False

        # Expression methods mapping
        self.expression_methods = {
            'Happy': self.expressions.get_happy_face,
            'Sad': self.expressions.get_sad_face,
            'Angry': self.expressions.get_angry_face,
            'Surprised': self.expressions.get_surprised_face,
            'Wink': self.expressions.get_wink_face,
            'Cool (Sunglasses)': self.expressions.get_cool_face,
            'Love (Bonus!)': self.expressions.get_love_face,
        }

        self._create_widgets()
        self._setup_keyboard_shortcuts()
        self._save_to_history()
        self._update_display()

    def _setup_keyboard_shortcuts(self):
        """Setup keyboard shortcuts for quick access to features."""
        # Expression shortcuts (number keys 1-7)
        self.root.bind('<1>', lambda e: self._select_expression('Happy'))
        self.root.bind('<2>', lambda e: self._select_expression('Sad'))
        self.root.bind('<3>', lambda e: self._select_expression('Angry'))
        self.root.bind('<4>', lambda e: self._select_expression('Surprised'))
        self.root.bind('<5>', lambda e: self._select_expression('Wink'))
        self.root.bind('<6>', lambda e: self._select_expression('Cool (Sunglasses)'))
        self.root.bind('<7>', lambda e: self._select_expression('Love (Bonus!)'))
        
        # Numpad shortcuts
        self.root.bind('<KP_1>', lambda e: self._select_expression('Happy'))
        self.root.bind('<KP_2>', lambda e: self._select_expression('Sad'))
        self.root.bind('<KP_3>', lambda e: self._select_expression('Angry'))
        self.root.bind('<KP_4>', lambda e: self._select_expression('Surprised'))
        self.root.bind('<KP_5>', lambda e: self._select_expression('Wink'))
        self.root.bind('<KP_6>', lambda e: self._select_expression('Cool (Sunglasses)'))
        self.root.bind('<KP_7>', lambda e: self._select_expression('Love (Bonus!)'))
        
        # Action shortcuts
        self.root.bind('<Control-r>', lambda e: self._update_display())  # Refresh
        self.root.bind('<Control-c>', lambda e: self._copy_to_clipboard())  # Copy
        self.root.bind('<Control-d>', lambda e: self._reset_defaults())  # Reset defaults
        self.root.bind('<Control-z>', lambda e: self._undo())  # Undo
        self.root.bind('<Control-y>', lambda e: self._redo())  # Redo
        self.root.bind('<Control-s>', lambda e: self._export_png())  # Save as PNG
        self.root.bind('<Control-e>', lambda e: self._open_custom_editor())  # Custom editor
        self.root.bind('<Control-n>', lambda e: self._random_face())  # Random face
        self.root.bind('<F1>', lambda e: self._show_help())  # Help
        self.root.bind('<Control-h>', lambda e: self._show_help())  # Help alternative
        self.root.bind('<Control-a>', lambda e: self._show_about())  # About
        self.root.bind('<Alt-F4>', lambda e: self._quit_app())  # Exit
        self.root.bind('<Control-q>', lambda e: self._quit_app())  # Exit alternative
        self.root.bind('<Control-w>', lambda e: self._quit_app())  # Exit alternative

        # Scale shortcuts
        self.root.bind('<Control-1>', lambda e: self._set_scale(1))  # Normal
        self.root.bind('<Control-2>', lambda e: self._set_scale(2))  # Large
        self.root.bind('<Control-3>', lambda e: self._set_scale(3))  # Extra Large
        self.root.bind('<Control-Plus>', lambda e: self._zoom_in())  # Zoom in
        self.root.bind('<Control-Minus>', lambda e: self._zoom_out())  # Zoom out
        
        # Color cycle shortcuts (Shift + arrows)
        self.root.bind('<Shift-Up>', lambda e: self._cycle_face_color(1))  # Next face color
        self.root.bind('<Shift-Down>', lambda e: self._cycle_face_color(-1))  # Previous face color
        self.root.bind('<Shift-Right>', lambda e: self._cycle_eye_color(1))  # Next eye color
        self.root.bind('<Shift-Left>', lambda e: self._cycle_eye_color(-1))  # Previous eye color

    def _set_scale(self, scale):
        """Set the scale factor."""
        self.scale = scale
        scale_texts = {1: "Normal (10x10)", 2: "Large (20x20)", 3: "Extra Large (30x30)"}
        self.scale_var.set(scale_texts.get(scale, "Normal (10x10)"))
        self._update_display()

    def _cycle_face_color(self, direction):
        """Cycle through face colors."""
        colors = list(self.face_colors.keys())
        current_index = colors.index(self.current_face_color)
        new_index = (current_index + direction) % len(colors)
        self.current_face_color = colors[new_index]
        self.face_color_var.set(self.current_face_color)
        self._update_display()

    def _cycle_eye_color(self, direction):
        """Cycle through eye colors."""
        colors = list(self.eye_colors.keys())
        current_index = colors.index(self.current_eye_color)
        new_index = (current_index + direction) % len(colors)
        self.current_eye_color = colors[new_index]
        self.eye_color_var.set(self.current_eye_color)
        self._update_display()

    def _zoom_in(self):
        """Zoom in (increase scale)."""
        if self.scale < 3:
            self.scale += 1
            scale_texts = {1: "Normal (10x10)", 2: "Large (20x20)", 3: "Extra Large (30x30)"}
            self.scale_var.set(scale_texts.get(self.scale, "Normal (10x10)"))
            self._update_display()

    def _zoom_out(self):
        """Zoom out (decrease scale)."""
        if self.scale > 1:
            self.scale -= 1
            scale_texts = {1: "Normal (10x10)", 2: "Large (20x20)", 3: "Extra Large (30x30)"}
            self.scale_var.set(scale_texts.get(self.scale, "Normal (10x10)"))
            self._update_display()

    def _save_to_history(self):
        """Save current state to history for Undo functionality."""
        state = {
            'expression': self.current_expression,
            'face_color': self.current_face_color,
            'eye_color': self.current_eye_color,
            'bg_color': self.current_bg_color,
            'scale': self.scale,
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

    def _redo(self):
        """Redo the last undone change."""
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            state = self.history[self.history_index]
            self._restore_state(state)

    def _restore_state(self, state):
        """Restore a saved state."""
        self.current_expression = state['expression']
        self.current_face_color = state['face_color']
        self.current_eye_color = state['eye_color']
        self.current_bg_color = state['bg_color']
        self.scale = state['scale']
        self.custom_grid = state['custom_grid']
        self.is_custom_mode = state['is_custom_mode']
        
        # Update UI controls
        self.face_color_var.set(self.current_face_color)
        self.eye_color_var.set(self.current_eye_color)
        self.bg_color_var.set(self.current_bg_color)
        scale_texts = {1: "Normal (10x10)", 2: "Large (20x20)", 3: "Extra Large (30x30)"}
        self.scale_var.set(scale_texts.get(self.scale, "Normal (10x10)"))
        
        # Update button highlights
        if not self.is_custom_mode:
            self._highlight_selected(self.current_expression)
        
        self._update_display()

    def _create_widgets(self):
        """Create and layout all GUI widgets."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="🎭 Facial Expression Program 🎭",
            font=('Helvetica', 18, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Left panel - Expression selection
        left_frame = ttk.LabelFrame(main_frame, text="Select Expression", padding="10")
        left_frame.grid(row=1, column=0, sticky=(tk.N, tk.S, tk.W, tk.E), padx=(0, 10))

        # Expression buttons
        self.expression_buttons = {}
        for idx, (name, _) in enumerate(self.expression_methods.items()):
            btn = tk.Button(
                left_frame,
                text=name,
                width=25,
                bg='#f0f0f0',
                relief=tk.RAISED,
                command=lambda n=name: self._select_expression(n)
            )
            btn.grid(row=idx, column=0, pady=5, sticky=(tk.W, tk.E))
            self.expression_buttons[name] = btn

        # Highlight first button
        self._highlight_selected("Happy")

        # Middle panel - Display area using Canvas for colored rectangles
        display_frame = ttk.LabelFrame(main_frame, text="Face Display", padding="10")
        display_frame.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.W, tk.E), padx=10)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Canvas for rendering colored face
        self.face_canvas = tk.Canvas(
            display_frame,
            bg='#e0e0e0',
            highlightthickness=2,
            highlightbackground='#999999'
        )
        self.face_canvas.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        
        display_frame.columnconfigure(0, weight=1)
        display_frame.rowconfigure(0, weight=1)

        # Right panel - Customization
        right_frame = ttk.LabelFrame(main_frame, text="Customization", padding="10")
        right_frame.grid(row=1, column=2, sticky=(tk.N, tk.S, tk.W, tk.E), padx=(10, 0))

        # Face color selection
        ttk.Label(right_frame, text="Face Color:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.face_color_var = tk.StringVar(value="Yellow")
        self.face_color_combo = ttk.Combobox(
            right_frame,
            textvariable=self.face_color_var,
            values=list(self.face_colors.keys()),
            state="readonly",
            width=15
        )
        self.face_color_combo.grid(row=0, column=1, pady=5, padx=(5, 0))
        self.face_color_combo.bind('<<ComboboxSelected>>', self._on_color_change)

        # Eye color selection
        ttk.Label(right_frame, text="Eye Color:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.eye_color_var = tk.StringVar(value="Black")
        self.eye_color_combo = ttk.Combobox(
            right_frame,
            textvariable=self.eye_color_var,
            values=list(self.eye_colors.keys()),
            state="readonly",
            width=15
        )
        self.eye_color_combo.grid(row=1, column=1, pady=5, padx=(5, 0))
        self.eye_color_combo.bind('<<ComboboxSelected>>', self._on_color_change)

        # Background color selection
        ttk.Label(right_frame, text="Background:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.bg_color_var = tk.StringVar(value="White")
        self.bg_color_combo = ttk.Combobox(
            right_frame,
            textvariable=self.bg_color_var,
            values=list(self.bg_colors.keys()),
            state="readonly",
            width=15
        )
        self.bg_color_combo.grid(row=2, column=1, pady=5, padx=(5, 0))
        self.bg_color_combo.bind('<<ComboboxSelected>>', self._on_color_change)

        # Scale selection with Zoom buttons
        ttk.Label(right_frame, text="Size Scale:").grid(row=3, column=0, sticky=tk.W, pady=5)
        
        # Zoom buttons frame
        zoom_frame = ttk.Frame(right_frame)
        zoom_frame.grid(row=3, column=1, pady=5, padx=(5, 0))
        
        ttk.Button(
            zoom_frame,
            text="➖",
            width=3,
            command=self._zoom_out
        ).grid(row=0, column=0, padx=(0, 2))
        
        self.scale_var = tk.StringVar(value="Normal (10x10)")
        ttk.Label(
            zoom_frame,
            textvariable=self.scale_var,
            width=18
        ).grid(row=0, column=1, padx=(2, 0))
        
        ttk.Button(
            zoom_frame,
            text="➕",
            width=3,
            command=self._zoom_in
        ).grid(row=0, column=2, padx=(2, 0))

        # Separator
        ttk.Separator(right_frame, orient='horizontal').grid(
            row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=15
        )

        # Undo/Redo buttons (side by side)
        undo_frame = ttk.Frame(right_frame)
        undo_frame.grid(row=5, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        ttk.Button(
            undo_frame,
            text="↩️ Undo",
            command=self._undo
        ).pack(side=tk.LEFT, padx=(0, 5), expand=True, fill=tk.X)
        
        ttk.Button(
            undo_frame,
            text="↪️ Redo",
            command=self._redo
        ).pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Action buttons
        ttk.Button(
            right_frame,
            text="🎲 Random Face",
            command=self._random_face
        ).grid(row=6, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="✏️ Custom Editor",
            command=self._open_custom_editor
        ).grid(row=7, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="💾 Export as PNG",
            command=self._export_png
        ).grid(row=8, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="📋 Copy to Clipboard",
            command=self._copy_to_clipboard
        ).grid(row=9, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="🔄 Refresh Display",
            command=self._update_display
        ).grid(row=10, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="🔧 Reset to Defaults",
            command=self._reset_defaults
        ).grid(row=11, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="❓ How It Works",
            command=self._show_help
        ).grid(row=12, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="ℹ️ About",
            command=self._show_about
        ).grid(row=13, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="🚪 Exit",
            command=self._quit_app
        ).grid(row=14, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        # Status bar
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))

        self.status_label = ttk.Label(
            status_frame,
            text="Expression: Happy | Scale: 1x | Face: 🟨 | Eyes: ⬛",
            font=('Helvetica', 9)
        )
        self.status_label.grid(row=0, column=0, sticky=tk.W)

    def _select_expression(self, name):
        """Handle expression selection."""
        self.current_expression = name
        self.is_custom_mode = False
        self.custom_grid = None
        self._highlight_selected(name)
        self._save_to_history()
        self._update_display()

    def _highlight_selected(self, name):
        """Highlight the selected expression button."""
        for btn_name, btn in self.expression_buttons.items():
            if btn_name == name:
                btn.config(bg='#4A90D9', fg='white', relief=tk.SUNKEN)
            else:
                btn.config(bg='#f0f0f0', fg='black', relief=tk.RAISED)

    def _on_color_change(self, event=None):
        """Handle color selection change."""
        self.current_face_color = self.face_color_var.get()
        self.current_eye_color = self.eye_color_var.get()
        self.current_bg_color = self.bg_color_var.get()
        self._save_to_history()
        self._update_display()

    def _get_face_array(self):
        """Get the current face array with applied colors."""
        # If in custom mode, return the custom grid
        if self.is_custom_mode and self.custom_grid:
            return self.custom_grid
        
        get_face_func = self.expression_methods[self.current_expression]
        face_color = self.face_colors[self.current_face_color]
        eye_color = self.eye_colors[self.current_eye_color]
        bg_color = self.bg_colors.get(self.current_bg_color, EmojiColors.WHITE_BG)

        return get_face_func(face_color, eye_color, bg_color)

    def _random_face(self):
        """Generate a random face with random expression and colors."""
        import random
        
        # Pick random expression
        expressions = list(self.expression_methods.keys())
        self.current_expression = random.choice(expressions)
        
        # Pick random colors
        face_colors = list(self.face_colors.keys())
        eye_colors = list(self.eye_colors.keys())
        bg_colors = list(self.bg_colors.keys())
        
        self.current_face_color = random.choice(face_colors)
        self.current_eye_color = random.choice(eye_colors)
        self.current_bg_color = random.choice(bg_colors)
        
        # Random scale
        self.scale = random.randint(1, 3)
        
        # Reset custom mode
        self.is_custom_mode = False
        self.custom_grid = None
        
        # Update UI
        self.face_color_var.set(self.current_face_color)
        self.eye_color_var.set(self.current_eye_color)
        self.bg_color_var.set(self.current_bg_color)
        scale_texts = {1: "Normal (10x10)", 2: "Large (20x20)", 3: "Extra Large (30x30)"}
        self.scale_var.set(scale_texts.get(self.scale, "Normal (10x10)"))
        self._highlight_selected(self.current_expression)
        
        self._save_to_history()
        self._update_display()
        
        messagebox.showinfo(
            "Random Face Generated",
            f"🎲 Random expression created!\n\n"
            f"Expression: {self.current_expression}\n"
            f"Face Color: {self.current_face_color}\n"
            f"Eye Color: {self.current_eye_color}\n"
            f"Background: {self.current_bg_color}\n"
            f"Scale: {self.scale}x"
        )

    def _export_png(self):
        """Export the current face as a PNG image."""
        from tkinter import filedialog
        
        # Get file path
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            initialfile=f"FacialExpression_{self.current_expression}.png"
        )
        
        if file_path:
            try:
                # Get the canvas postscript data
                ps_data = self.face_canvas.postscript(colormode='color')
                
                # Create a temporary file
                import tempfile
                import os
                
                with tempfile.NamedTemporaryFile(suffix='.ps', delete=False) as tmp_file:
                    tmp_file.write(ps_data.encode('utf-8'))
                    tmp_ps_path = tmp_file.name
                
                # Convert to PNG using PIL if available
                try:
                    from PIL import Image, ImageDraw
                    import io
                    
                    # Read postscript and convert
                    img = Image.open(io.BytesIO(ps_data.encode('utf-8')))
                    img.save(file_path, 'PNG')
                    
                    messagebox.showinfo(
                        "Export Successful",
                        f"✅ Face exported to:\n{file_path}"
                    )
                except ImportError:
                    # PIL not available, save as postscript
                    with open(file_path.replace('.png', '.ps'), 'w') as f:
                        f.write(ps_data)
                    messagebox.showinfo(
                        "Export Info",
                        f"⚠️ PIL/Pillow not installed.\n"
                        f"Saved as PostScript (.ps) instead of PNG.\n\n"
                        f"Install Pillow with: pip install Pillow\n"
                        f"File saved to: {file_path.replace('.png', '.ps')}"
                    )
                
                # Clean up temp file
                os.unlink(tmp_ps_path)
                
            except Exception as e:
                messagebox.showerror(
                    "Export Failed",
                    f"❌ Could not export image.\n\nError: {str(e)}\n\n"
                    f"Tip: Install Pillow for PNG export:\n"
                    f"pip install Pillow"
                )

    def _open_custom_editor(self):
        """Open the custom expression editor window."""
        # Create a new top-level window
        editor_window = tk.Toplevel(self.root)
        editor_window.title("✏️ Custom Expression Editor")
        editor_window.geometry("600x700")
        editor_window.transient(self.root)
        editor_window.grab_set()
        
        # Create 10x10 grid for editing
        custom_frame = ttk.LabelFrame(editor_window, text="Design Your Face", padding="10")
        custom_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Store grid buttons
        grid_buttons = []
        
        # Current color for painting
        paint_color = tk.StringVar(value="face")
        
        def on_cell_click(row, col):
            """Handle cell click in custom editor."""
            color_type = paint_color.get()
            if color_type == "face":
                color = self.face_colors[self.current_face_color]
            elif color_type == "eye":
                color = self.eye_colors[self.current_eye_color]
            else:
                color = self.bg_colors[self.current_bg_color]
            
            # Update the cell
            grid_buttons[row][col].config(bg=color[0])
            
            # Update custom grid data
            if self.custom_grid is None or len(self.custom_grid) != 10:
                # Initialize custom grid
                self.custom_grid = [[self.bg_colors["White"] for _ in range(10)] for _ in range(10)]
            
            self.custom_grid[row][col] = color
        
        def clear_grid():
            """Clear the grid to background color."""
            bg_color = self.bg_colors[self.current_bg_color]
            for row in range(10):
                for col in range(10):
                    grid_buttons[row][col].config(bg=bg_color[0])
                    if self.custom_grid and len(self.custom_grid) == 10:
                        self.custom_grid[row][col] = bg_color
        
        def fill_face():
            """Fill the entire grid with face color."""
            face_color = self.face_colors[self.current_face_color]
            for row in range(10):
                for col in range(10):
                    grid_buttons[row][col].config(bg=face_color[0])
                    if self.custom_grid is None or len(self.custom_grid) != 10:
                        self.custom_grid = [[face_color for _ in range(10)] for _ in range(10)]
                    else:
                        self.custom_grid[row][col] = face_color
        
        def save_custom():
            """Save the custom expression."""
            if self.custom_grid is None or len(self.custom_grid) != 10:
                messagebox.showwarning(
                    "No Custom Design",
                    "Please draw something first!"
                )
                return
            
            self.is_custom_mode = True
            self.current_expression = "Custom"
            
            # Clear button highlights
            for btn in self.expression_buttons.values():
                btn.config(bg='#f0f0f0', fg='black', relief=tk.RAISED)
            
            self._save_to_history()
            self._update_display()
            editor_window.destroy()
            
            messagebox.showinfo(
                "Custom Expression Saved",
                "✅ Your custom face is now displayed!\n\n"
                "Click 'Custom Editor' again to modify it."
            )
        
        # Paint color selection
        paint_frame = ttk.Frame(editor_window)
        paint_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(paint_frame, text="Paint with:").pack(side=tk.LEFT, padx=5)
        
        ttk.Radiobutton(
            paint_frame,
            text="Face Color",
            variable=paint_color,
            value="face"
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Radiobutton(
            paint_frame,
            text="Eye Color",
            variable=paint_color,
            value="eye"
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Radiobutton(
            paint_frame,
            text="Background",
            variable=paint_color,
            value="bg"
        ).pack(side=tk.LEFT, padx=5)
        
        # Create 10x10 grid of buttons
        grid_frame = ttk.Frame(custom_frame)
        grid_frame.pack()
        
        for row in range(10):
            row_buttons = []
            for col in range(10):
                btn = tk.Button(
                    grid_frame,
                    text="",
                    width=4,
                    height=2,
                    bg='#FFFFFF',
                    command=lambda r=row, c=col: on_cell_click(r, c)
                )
                btn.grid(row=row, column=col, padx=1, pady=1)
                row_buttons.append(btn)
            grid_buttons.append(row_buttons)
        
        # Control buttons
        control_frame = ttk.Frame(editor_window)
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(
            control_frame,
            text="🗑️ Clear All",
            command=clear_grid
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            control_frame,
            text="🎨 Fill Face",
            command=fill_face
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            control_frame,
            text="💾 Save & Use",
            command=save_custom
        ).pack(side=tk.RIGHT, padx=5)
        
        # Instructions
        instructions = ttk.Label(
            editor_window,
            text="Click cells to paint. Use radio buttons to select color type.",
            font=('Helvetica', 9)
        )
        instructions.pack(pady=5)

    def _update_display(self):
        """Draw the face on the canvas using colored rectangles.
        
        How the rendering works:
        1. Get the 10x10 face array with current colors applied
        2. Clear the canvas
        3. Calculate cell size based on scale (1x, 2x, or 3x)
        4. Use NESTED LOOPS to draw each cell:
           - OUTER LOOP: Go through each row (0 to 9)
           - INNER LOOP: Go through each column (0 to 9)
           - Draw a colored rectangle at each position
        5. Update the status bar with current settings
        """
        face_array = self._get_face_array()

        # Clear canvas
        self.face_canvas.delete("all")

        # Get canvas dimensions
        self.face_canvas.update_idletasks()
        canvas_width = self.face_canvas.winfo_width()
        canvas_height = self.face_canvas.winfo_height()

        # Ensure minimum dimensions (winfo_* may return 1 before widget is rendered)
        if canvas_width < 100 or canvas_width == 1:
            canvas_width = 500
        if canvas_height < 100 or canvas_height == 1:
            canvas_height = 400

        # Grid is 10x10
        grid_size = 10

        # Calculate cell size based on scale
        # Base cell size for scale 1x
        base_cell_size = min(canvas_width, canvas_height) // (grid_size + 4)

        # Apply scale factor: 1x = base, 2x = 2*base, 3x = 3*base
        cell_size = base_cell_size * self.scale

        # Ensure minimum cell size (only for very small windows)
        min_cell = 25 * self.scale
        if cell_size < min_cell:
            cell_size = min_cell

        # Maximum cell size scales with scale factor to maintain proportions
        max_cell = 80 * self.scale
        if cell_size > max_cell:
            cell_size = max_cell

        # Calculate starting position to center the grid
        grid_width = cell_size * grid_size
        grid_height = cell_size * grid_size
        start_x = (canvas_width - grid_width) // 2
        start_y = (canvas_height - grid_height) // 2
        
        # Draw each cell as a colored rectangle
        for row in range(grid_size):
            for col in range(grid_size):
                color_data = face_array[row][col]
                # color_data is a tuple: (hex_color, emoji)
                if isinstance(color_data, tuple):
                    fill_color = color_data[0]
                else:
                    fill_color = "#FFFFFF"  # Default to white
                
                x1 = start_x + col * cell_size
                y1 = start_y + row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                
                # Draw rectangle with color
                self.face_canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=fill_color,
                    outline="#333333",
                    width=1
                )
        
        # Update status bar with emoji preview
        face_emoji = self.face_colors[self.current_face_color][1]
        eye_emoji = self.eye_colors[self.current_eye_color][1]
        self.status_label.config(
            text=f"Expression: {self.current_expression} | "
                 f"Scale: {self.scale}x | "
                 f"Face: {face_emoji} | "
                 f"Eyes: {eye_emoji}"
        )

    def _show_help(self):
        """Display help information."""
        help_text = """
HOW THE PROGRAM WORKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 2D ARRAY STORAGE:
   Each facial expression is stored as a 10x10 2D array.
   Templates use placeholder symbols that get replaced
   with colored rectangles:
     • F = Face color (Yellow, Blue, Green, etc.)
     • E = Eye color (Black, Red, Blue, etc.)
     • B = Background color (White, Black, Blue)

2. COLOR CUSTOMIZATION:
   Select different colors from the dropdown menus:
     • Face colors: Yellow, Blue, Green, Orange, Purple, Brown, White, Black
     • Eye colors: Black, Red, Blue, Green, Purple, Brown
     • Background: White, Black, Blue

3. NESTED LOOPS RENDERING:
   The program uses nested loops to draw the face:
     OUTER LOOP → Iterates through rows 0 to 9
     INNER LOOP → Iterates through columns 0 to 9
                  Draws a colored rectangle at each position

4. SCALING:
   The scale factor increases the size of each cell:
     • Normal (1x) = 10x10 grid
     • Large (2x) = 20x20 effective size
     • Extra Large (3x) = 30x30 effective size

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KEYBOARD SHORTCUTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Expressions:
  [1-7]     Select expression (Happy, Sad, Angry...)
  [Numpad]  Also works with numpad keys

Actions:
  [Ctrl+R]  Refresh display
  [Ctrl+C]  Copy to clipboard
  [Ctrl+D]  Reset to defaults
  [F1]      Show this help
  [Ctrl+A]  About dialog
  [Ctrl+Q]  Quit program

Scale:
  [Ctrl+1]  Normal (10x10)
  [Ctrl+2]  Large (20x20)
  [Ctrl+3]  Extra Large (30x30)

Colors:
  [Shift+↑↓] Cycle face colors
  [Shift+←→] Cycle eye colors

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HKDSE ICT Pre-SBA 2 • 2026
        """

        messagebox.showinfo("How It Works", help_text)

    def _copy_to_clipboard(self):
        """Copy the current face as emoji text to clipboard."""
        face_array = self._get_face_array()

        # Convert color tuples to emojis
        emoji_lines = []
        for row in face_array:
            line = ""
            for cell in row:
                if isinstance(cell, tuple):
                    # cell is (hex_color, emoji)
                    line += cell[1]
                else:
                    line += cell
            emoji_lines.append(line)

        # Join lines with newlines
        emoji_text = "\n".join(emoji_lines)

        # Copy to clipboard with error handling
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(emoji_text)
            self.root.update()  # Ensure clipboard is updated

            messagebox.showinfo(
                "Copied!",
                f"✅ {self.current_expression} face copied to clipboard!\n\n"
                f"You can now paste it into any text field.\n\n"
                f"Settings: {self.current_face_color} face, {self.current_eye_color} eyes, "
                f"{self.current_bg_color} background, {self.scale}x scale"
            )
        except Exception as e:
            messagebox.showerror(
                "Clipboard Error",
                f"Failed to copy to clipboard.\n\nError: {str(e)}\n\n"
                f"This may be due to clipboard access restrictions on your system."
            )

    def _reset_defaults(self):
        """Reset all settings to default values."""
        # Reset to defaults
        self.current_face_color = "Yellow"
        self.current_eye_color = "Black"
        self.current_bg_color = "White"
        self.scale = 1
        self.current_expression = "Happy"

        # Update combo boxes
        self.face_color_var.set("Yellow")
        self.eye_color_var.set("Black")
        self.bg_color_var.set("White")
        self.scale_var.set("Normal (10x10)")

        # Reset button highlights
        self._highlight_selected("Happy")

        # Update display
        self._update_display()

        # Get emojis dynamically from color settings
        face_emoji = self.face_colors["Yellow"][1]
        eye_emoji = self.eye_colors["Black"][1]
        bg_emoji = self.bg_colors["White"][1]

        messagebox.showinfo(
            "Reset Complete",
            "✅ All settings have been reset to defaults:\n\n"
            "• Expression: Happy\n"
            f"• Face Color: Yellow {face_emoji}\n"
            f"• Eye Color: Black {eye_emoji}\n"
            f"• Background: White {bg_emoji}\n"
            "• Scale: Normal (1x)"
        )

    def _show_about(self):
        """Display about dialog with project information."""
        about_text = """
🎭 FACIAL EXPRESSION PROGRAM 🎭
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Version: 1.0.0
Build Date: 27/02/2026

HKDSE ICT Pre-SBA 2 Project

STUDENT INFORMATION:
  • Class: 4E
  • Student ID: 13
  • Date: 27/02/2026

PROJECT DESCRIPTION:
  A Python GUI program that displays facial 
  expressions using 10x10 2D arrays with nested 
  loops for rendering.

FEATURES:
  ✓ 7 Facial Expressions
  ✓ 8 Face Colors
  ✓ 6 Eye/Mouth Colors
  ✓ 3 Background Colors
  ✓ 3 Size Scales
  ✓ Copy to Clipboard
  ✓ Keyboard Shortcuts
  ✓ Cross-Platform Support

TECHNOLOGIES:
  • Python 3.6+
  • tkinter (GUI)
  • PyInstaller (EXE/App builder)

KEYBOARD SHORTCUTS:
  • 1-7: Select expressions
  • Ctrl+C: Copy to clipboard
  • Ctrl+D: Reset defaults
  • F1: Help
  • Ctrl+Q: Quit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
© 2026 HKDSE ICT Pre-SBA 2
All Rights Reserved
        """

        messagebox.showinfo("About Facial Expression Program", about_text)

    def _quit_app(self):
        """Quit the application."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()
            self.root.destroy()


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = FacialExpressionGUI(root)
        root.mainloop()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)
