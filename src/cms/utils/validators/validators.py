"""Validation utilities for the application"""

import re


def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_phone(phone: str) -> bool:
    """Validate phone number format"""
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    return len(digits_only) >= 10


def validate_password(password: str) -> bool:
    """Validate password strength"""
    return len(password) >= 6


def validate_name(name: str) -> bool:
    """Validate name format"""
    return len(name.strip()) >= 2 and name.replace(" ", "").isalpha()
