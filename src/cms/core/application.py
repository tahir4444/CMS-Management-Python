"""
Main application class for Enterprise CMS
Handles the core application logic and initialization.
"""

import tkinter as tk
from tkinter import ttk
import os

from ..ui.styles import StyleManager
from ..services.database.database_service import DatabaseService
from ..services.auth.auth_service import AuthService
from ..services.email.email_service import EmailService
from ..ui.pages.login_page import LoginPage
from ..ui.pages.register_page import RegisterPage
from ..ui.pages.dashboard_page import DashboardPage
from ..ui.pages.users_page import UsersPage
from ..ui.dialogs.message_box import CustomMessageBox
from ..config.settings import AppSettings
from ..utils.helpers.icon_manager import IconManager


class CustomerApp:
    """Main application class for Enterprise CMS"""
    
    def __init__(self, root):
        """Initialize the application"""
        self.root = root
        self.setup_window()
        
        # Initialize services
        self.settings = AppSettings()
        self.database_service = DatabaseService()
        self.auth_service = AuthService(self.database_service)
        self.email_service = EmailService()
        
        # Initialize UI components
        self.style_manager = StyleManager()
        self.message_box = CustomMessageBox(self.root)
        self.icon_manager = IconManager(self.root)
        
        # Initialize pages
        self.login_page = None
        self.register_page = None
        self.dashboard_page = None
        self.users_page = None
        
        # Current user state
        self.current_user = None
        
        # Setup main frame
        self.setup_main_frame()
        
        # Show login page by default
        self.show_login_page()
    
    def setup_window(self):
        """Setup the main window"""
        self.root.title("Enterprise CMS - Professional Customer Management")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        self.root.resizable(True, True)
        
        # Center the window
        self.center_window()
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_main_frame(self):
        """Setup the main frame"""
        self.main_frame = ttk.Frame(self.root, padding="20", style="Professional.TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
    
    def clear_main_frame(self):
        """Clear all widgets from main frame"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_login_page(self):
        """Show the login page"""
        self.clear_main_frame()
        self.login_page = LoginPage(self)
        self.login_page.show()
    
    def show_register_page(self):
        """Show the register page"""
        self.clear_main_frame()
        self.register_page = RegisterPage(self)
        self.register_page.show()
    
    def show_dashboard(self, user):
        """Show the dashboard page"""
        self.clear_main_frame()
        self.current_user = user
        self.dashboard_page = DashboardPage(self, user)
        self.dashboard_page.show()
    
    def show_users_list(self):
        """Show the users list page"""
        self.clear_main_frame()
        self.users_page = UsersPage(self)
        self.users_page.show()
    
    def logout(self):
        """Logout the current user"""
        self.current_user = None
        self.auth_service.clear_saved_credentials()
        self.show_login_page()
    
    def run(self):
        """Start the application"""
        self.root.mainloop()
