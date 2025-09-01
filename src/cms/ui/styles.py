"""Style manager for the application UI"""

from tkinter import ttk


class StyleManager:
    """Manages application styles and themes"""
    
    def __init__(self):
        self.setup_styles()
    
    def setup_styles(self):
        """Setup professional enterprise-grade styles"""
        style = ttk.Style()
        
        # Professional color palette
        primary_color = "#2563eb"      # Modern blue
        secondary_color = "#64748b"    # Slate gray
        accent_color = "#f59e0b"       # Amber accent
        success_color = "#10b981"      # Emerald green
        warning_color = "#f59e0b"      # Amber
        error_color = "#ef4444"        # Red
        background_color = "#f8fafc"   # Light gray background
        card_background = "#ffffff"    # White cards
        text_primary = "#1e293b"       # Dark text
        text_secondary = "#64748b"     # Secondary text
        border_color = "#e2e8f0"       # Border color
        
        # Configure professional card style
        style.configure("Professional.TFrame", 
                       background=card_background,
                       relief="flat", 
                       borderwidth=0)
        
        # Configure card style for registration page
        style.configure("Card.TFrame", 
                       background=card_background,
                       relief="flat", 
                       borderwidth=0)
        
        # Modern button styles
        style.configure("Primary.TButton", 
                       font=("Inter", 11, "bold"),
                       padding=(24, 14))
        
        style.configure("Secondary.TButton", 
                       font=("Inter", 11, "bold"),
                       padding=(20, 12))
        
        style.configure("Success.TButton", 
                       font=("Inter", 11, "bold"),
                       padding=(20, 12))
        
        # Professional entry style
        style.configure("Professional.TEntry", 
                       fieldbackground="#ffffff",
                       borderwidth=2)
        
        # Professional label styles
        style.configure("Title.TLabel", 
                       font=("Inter", 24, "bold"),
                       foreground=text_primary,
                       background=card_background)
        
        style.configure("Subtitle.TLabel", 
                       font=("Inter", 16, "normal"),
                       foreground=text_secondary,
                       background=card_background)
        
        style.configure("Heading.TLabel", 
                       font=("Inter", 18, "bold"),
                       foreground=text_primary,
                       background=card_background)
        
        style.configure("Body.TLabel", 
                       font=("Inter", 14, "normal"),
                       foreground=text_primary,
                       background=card_background)
        
        style.configure("Caption.TLabel", 
                       font=("Inter", 12, "normal"),
                       foreground=text_secondary,
                       background=card_background)
        
        # Professional checkbox style
        style.configure("Professional.TCheckbutton", 
                       font=("Inter", 12, "normal"),
                       background=card_background,
                       foreground=text_primary)
        
        # Checkbutton style for registration page
        style.configure("Checkbutton.TCheckbutton", 
                       font=("Inter", 12, "normal"),
                       background=card_background,
                       foreground=text_primary)
        
        # Hover effects for buttons
        style.map("Primary.TButton",
                 relief=[("pressed", "sunken"), ("active", "raised")])
        
        style.map("Secondary.TButton",
                 relief=[("pressed", "sunken"), ("active", "raised")])
        
        # Store colors for use in the app
        self.colors = {
            'primary': primary_color,
            'secondary': secondary_color,
            'accent': accent_color,
            'success': success_color,
            'warning': warning_color,
            'error': error_color,
            'background': background_color,
            'card': card_background,
            'text_primary': text_primary,
            'text_secondary': text_secondary,
            'border': border_color
        }
