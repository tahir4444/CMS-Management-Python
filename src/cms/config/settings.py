"""
Application settings and configuration management
"""

import os
from pathlib import Path


class AppSettings:
    """Application settings and configuration"""
    
    def __init__(self):
        # Application info
        self.APP_NAME = "Enterprise CMS"
        self.APP_VERSION = "1.0.0"
        self.APP_DESCRIPTION = "Professional Customer Management System"
        
        # Window settings
        self.WINDOW_WIDTH = 1000
        self.WINDOW_HEIGHT = 700
        self.MIN_WIDTH = 800
        self.MIN_HEIGHT = 600
        
        # Database settings
        self.DATABASE_PATH = "customers.db"
        
        # File paths
        self.BASE_DIR = Path(__file__).parent.parent.parent.parent
        self.ASSETS_DIR = self.BASE_DIR / "assets"
        self.ICONS_DIR = self.ASSETS_DIR / "icons"
        self.LOGS_DIR = self.BASE_DIR / "logs"
        
        # Credentials file
        self.CREDENTIALS_FILE = "saved_credentials.txt"
        
        # Create necessary directories
        self._create_directories()
    
    def _create_directories(self):
        """Create necessary directories if they don't exist"""
        directories = [
            self.ASSETS_DIR,
            self.ICONS_DIR,
            self.LOGS_DIR
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    @property
    def icon_paths(self):
        """Get icon file paths"""
        return {
            'ico': self.ICONS_DIR / "app_icon.ico",
            'png': self.ICONS_DIR / "app_icon.png",
            'small_png': self.ICONS_DIR / "app_icon_small.png"
        }
    
    @property
    def log_file(self):
        """Get log file path"""
        return self.LOGS_DIR / "cms.log"
