# ============================================================================
# HKDSE ICT Pre-SBA 2: Facial Expression Program (GUI Version)
# Author: Student
# Class: 4E
# Date: 2026-02-27
# Description: A Python GUI program that displays facial expressions using
#              2D arrays with mouse-clickable interface using tkinter.
# Version: 1.0.0
# ============================================================================

import tkinter as tk
from tkinter import ttk, messagebox, font
import sys

# ============================================================================
# EMOJI COLOR PALETTES - Using actual colors for Canvas rendering
# ============================================================================

class EmojiColors:
    """Class containing color palettes for canvas rendering."""

    # Face/skin colors (using actual hex colors for Canvas)
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

class FacialExpressions:
    """Class containing all facial expression patterns as 10x10 2D arrays."""

    FACE_SYMBOL = "F"
    EYE_SYMBOL = "E"
    BG_SYMBOL = "B"

    @staticmethod
    def _apply_colors(template, face_color, eye_color, bg_color):
        """Replace template symbols with actual colors."""
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

class FacialExpressionGUI:
    """Main GUI application for displaying facial expressions."""

    def __init__(self, root):
        """Initialize the GUI application."""
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

        # Scale selection
        ttk.Label(right_frame, text="Size Scale:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.scale_var = tk.StringVar(value="Normal (10x10)")
        self.scale_combo = ttk.Combobox(
            right_frame,
            textvariable=self.scale_var,
            values=["Normal (10x10)", "Large (20x20)", "Extra Large (30x30)"],
            state="readonly",
            width=18
        )
        self.scale_combo.grid(row=3, column=1, pady=5, padx=(5, 0))
        self.scale_combo.bind('<<ComboboxSelected>>', self._on_scale_change)

        # Separator
        ttk.Separator(right_frame, orient='horizontal').grid(
            row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=15
        )

        # Action buttons
        ttk.Button(
            right_frame,
            text="🔄 Refresh Display",
            command=self._update_display
        ).grid(row=5, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="📋 Copy to Clipboard",
            command=self._copy_to_clipboard
        ).grid(row=6, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="🔧 Reset to Defaults",
            command=self._reset_defaults
        ).grid(row=7, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="❓ How It Works",
            command=self._show_help
        ).grid(row=8, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="ℹ️ About",
            command=self._show_about
        ).grid(row=9, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Button(
            right_frame,
            text="🚪 Exit",
            command=self._quit_app
        ).grid(row=10, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

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
        self._highlight_selected(name)
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
        self._update_display()

    def _on_scale_change(self, event=None):
        """Handle scale selection change."""
        scale_text = self.scale_var.get()
        if "Normal" in scale_text:
            self.scale = 1
        elif "Large" in scale_text:
            self.scale = 2
        else:
            self.scale = 3
        self._update_display()

    def _get_face_array(self):
        """Get the current face array with applied colors."""
        get_face_func = self.expression_methods[self.current_expression]
        face_color = self.face_colors[self.current_face_color]
        eye_color = self.eye_colors[self.current_eye_color]
        bg_color = self.bg_colors.get(self.current_bg_color, EmojiColors.WHITE_BG)

        return get_face_func(face_color, eye_color, bg_color)

    def _update_display(self):
        """Update the face display with current settings using colored rectangles."""
        face_array = self._get_face_array()
        
        # Clear canvas
        self.face_canvas.delete("all")
        
        # Get canvas dimensions
        self.face_canvas.update_idletasks()
        canvas_width = self.face_canvas.winfo_width()
        canvas_height = self.face_canvas.winfo_height()
        
        # Ensure minimum dimensions
        if canvas_width < 100:
            canvas_width = 500
        if canvas_height < 100:
            canvas_height = 400
        
        # Grid is 10x10
        grid_size = 10
        
        # Calculate cell size based on scale
        base_cell_size = min(canvas_width, canvas_height) // (grid_size + 2)
        cell_size = base_cell_size * self.scale
        cell_size = max(cell_size, 20)  # Minimum cell size
        cell_size = min(cell_size, 60)  # Maximum cell size
        
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
        
        # Copy to clipboard
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
        
        messagebox.showinfo(
            "Reset Complete",
            "✅ All settings have been reset to defaults:\n\n"
            "• Expression: Happy\n"
            "• Face Color: Yellow 🟨\n"
            "• Eye Color: Black ⬛\n"
            "• Background: White ⬜\n"
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
