"""Authentication service for handling user authentication and credentials"""

import os
import hashlib
from typing import Optional, Tuple


class AuthService:
    """Service for handling authentication operations"""
    
    def __init__(self, database_service):
        self.database_service = database_service
        self.credentials_file = "saved_credentials.txt"
    
    def hash_password(self, password: str) -> str:
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def authenticate_user(self, email: str, password: str) -> Optional[Tuple]:
        """Authenticate user with email and password"""
        password_hash = self.hash_password(password)
        return self.database_service.authenticate_customer(email, password_hash)
    
    def register_user(self, first_name: str, last_name: str, email: str, 
                     phone: str, password: str) -> int:
        """Register a new user"""
        password_hash = self.hash_password(password)
        return self.database_service.create_customer(first_name, last_name, email, phone, password_hash)
    
    def save_credentials(self, email: str, password: str):
        """Save credentials to file"""
        try:
            with open(self.credentials_file, "w") as f:
                f.write(f"{email}\n{password}")
        except Exception as e:
            print(f"Error saving credentials: {e}")
    
    def load_saved_credentials(self) -> Tuple[str, str]:
        """Load saved credentials from file"""
        try:
            if os.path.exists(self.credentials_file):
                with open(self.credentials_file, "r") as f:
                    lines = f.readlines()
                    if len(lines) >= 2:
                        return lines[0].strip(), lines[1].strip()
        except Exception as e:
            print(f"Error loading saved credentials: {e}")
        return "", ""
    
    def clear_saved_credentials(self):
        """Clear saved credentials"""
        try:
            if os.path.exists(self.credentials_file):
                os.remove(self.credentials_file)
        except Exception as e:
            print(f"Error clearing saved credentials: {e}")
    
    def reset_password(self, email: str) -> str:
        """Reset user password and return temporary password"""
        import random
        import string
        
        # Generate temporary password
        temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        password_hash = self.hash_password(temp_password)
        
        # Update password in database
        self.database_service.update_customer_password(email, password_hash)
        
        return temp_password
