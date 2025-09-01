"""Database service for handling all database operations"""

import sqlite3
from typing import List, Tuple, Optional


class DatabaseService:
    """Service for handling database operations"""
    
    def __init__(self, db_path: str = "customers.db"):
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        self.init_database()
    
    def init_database(self):
        """Initialize the database and create tables"""
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            
            # Create customers table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            self.conn.commit()
        except Exception as e:
            raise Exception(f"Failed to initialize database: {str(e)}")
    
    def create_customer(self, first_name: str, last_name: str, email: str, 
                       phone: str, password_hash: str) -> int:
        """Create a new customer"""
        try:
            self.cursor.execute('''
                INSERT INTO customers (first_name, last_name, email, phone, password_hash)
                VALUES (?, ?, ?, ?, ?)
            ''', (first_name, last_name, email, phone, password_hash))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise Exception("Email already registered")
        except Exception as e:
            raise Exception(f"Failed to create customer: {str(e)}")
    
    def authenticate_customer(self, email: str, password_hash: str) -> Optional[Tuple]:
        """Authenticate customer with email and password"""
        try:
            self.cursor.execute('''
                SELECT id, first_name, last_name, email 
                FROM customers 
                WHERE email = ? AND password_hash = ?
            ''', (email, password_hash))
            return self.cursor.fetchone()
        except Exception as e:
            raise Exception(f"Failed to authenticate customer: {str(e)}")
    
    def update_customer_password(self, email: str, password_hash: str) -> bool:
        """Update customer password"""
        try:
            self.cursor.execute('''
                UPDATE customers 
                SET password_hash = ? 
                WHERE email = ?
            ''', (password_hash, email))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            raise Exception(f"Failed to update password: {str(e)}")
    
    def get_all_customers(self) -> List[Tuple]:
        """Get all customers"""
        try:
            self.cursor.execute('''
                SELECT id, first_name, last_name, email, phone, created_at 
                FROM customers 
                ORDER BY created_at DESC
            ''')
            return self.cursor.fetchall()
        except Exception as e:
            raise Exception(f"Failed to get customers: {str(e)}")
    
    def email_exists(self, email: str) -> bool:
        """Check if email already exists"""
        try:
            self.cursor.execute("SELECT id FROM customers WHERE email = ?", (email,))
            return self.cursor.fetchone() is not None
        except Exception as e:
            raise Exception(f"Failed to check email existence: {str(e)}")
    
    def get_customer_by_email(self, email: str) -> Optional[Tuple]:
        """Get customer by email address"""
        try:
            self.cursor.execute('''
                SELECT id, first_name, last_name, email, phone, created_at
                FROM customers
                WHERE email = ?
            ''', (email,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            raise Exception(f"Failed to get customer: {str(e)}")

    def search_customers(self, search_term: str) -> List[Tuple]:
        """Search customers by name or email"""
        try:
            search_pattern = f"%{search_term}%"
            self.cursor.execute('''
                SELECT id, first_name, last_name, email, phone, created_at
                FROM customers
                WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ?
                ORDER BY created_at DESC
            ''', (search_pattern, search_pattern, search_pattern))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            raise Exception(f"Failed to search customers: {str(e)}")

    def get_customer_count(self) -> int:
        """Get total number of customers"""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM customers")
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            raise Exception(f"Failed to get customer count: {str(e)}")

    def get_recent_registrations_count(self, days: int = 7) -> int:
        """Get count of recent registrations"""
        try:
            self.cursor.execute('''
                SELECT COUNT(*) FROM customers 
                WHERE created_at >= datetime('now', '-{} days')
            '''.format(days))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            raise Exception(f"Failed to get recent registrations count: {str(e)}")

    def get_today_registrations_count(self) -> int:
        """Get count of today's registrations"""
        try:
            self.cursor.execute('''
                SELECT COUNT(*) FROM customers 
                WHERE date(created_at) = date('now')
            ''')
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            raise Exception(f"Failed to get today's registrations count: {str(e)}")

    def get_recent_activity(self, limit: int = 5) -> List[Tuple]:
        """Get recent customer activity"""
        try:
            self.cursor.execute('''
                SELECT first_name, last_name, email, created_at
                FROM customers 
                ORDER BY created_at DESC
                LIMIT ?
            ''', (limit,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            raise Exception(f"Failed to get recent activity: {str(e)}")

    def update_customer_profile(self, email: str, first_name: str, last_name: str, phone: str) -> bool:
        """Update customer profile information"""
        try:
            self.cursor.execute('''
                UPDATE customers 
                SET first_name = ?, last_name = ?, phone = ?
                WHERE email = ?
            ''', (first_name, last_name, phone, email))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            raise Exception(f"Failed to update profile: {str(e)}")

    def get_customer_by_id(self, customer_id: int) -> Optional[Tuple]:
        """Get customer by ID"""
        try:
            self.cursor.execute('''
                SELECT id, first_name, last_name, email, phone, created_at
                FROM customers
                WHERE id = ?
            ''', (customer_id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            raise Exception(f"Failed to get customer: {str(e)}")

    def delete_customer(self, customer_id: int) -> bool:
        """Delete customer by ID"""
        try:
            self.cursor.execute('''
                DELETE FROM customers 
                WHERE id = ?
            ''', (customer_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            raise Exception(f"Failed to delete customer: {str(e)}")

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

    def __del__(self):
        """Destructor to ensure connection is closed"""
        self.close()
