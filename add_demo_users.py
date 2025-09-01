#!/usr/bin/env python3
"""
Script to add demo users to the database
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from cms.services.database.database_service import DatabaseService
from cms.services.auth.auth_service import AuthService
import hashlib
from datetime import datetime, timedelta


def add_demo_users():
    """Add demo users to the database"""
    try:
        # Initialize services
        db_service = DatabaseService()
        auth_service = AuthService(db_service)
        
        # Demo users data
        demo_users = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@enterprise.com",
                "phone": "+1-555-0101",
                "password": "password123",
                "created_at": datetime.now() - timedelta(days=15)
            },
            {
                "first_name": "Jane",
                "last_name": "Smith",
                "email": "jane.smith@enterprise.com",
                "phone": "+1-555-0102",
                "password": "password123",
                "created_at": datetime.now() - timedelta(days=14)
            },
            {
                "first_name": "Michael",
                "last_name": "Johnson",
                "email": "michael.johnson@enterprise.com",
                "phone": "+1-555-0103",
                "password": "password123",
                "created_at": datetime.now() - timedelta(days=12)
            },
            {
                "first_name": "Sarah",
                "last_name": "Wilson",
                "email": "sarah.wilson@enterprise.com",
                "phone": "+1-555-0104",
                "password": "password123",
                "created_at": datetime.now() - timedelta(days=10)
            },
            {
                "first_name": "David",
                "last_name": "Brown",
                "email": "david.brown@enterprise.com",
                "phone": "+1-555-0105",
                "password": "password123",
                "created_at": datetime.now() - timedelta(days=8)
            },
            {
                "first_name": "Lisa",
                "last_name": "Davis",
                "email": "lisa.davis@enterprise.com",
                "phone": "+1-555-0106",
                "password": "password123",
                "created_at": datetime.now() - timedelta(days=6)
            },
            {
                "first_name": "Thomas",
                "last_name": "Miller",
                "email": "thomas.miller@enterprise.com",
                "phone": "+1-555-0107",
                "password": "password123",
                "created_at": datetime.now() - timedelta(days=4)
            },
            {
                "first_name": "Emma",
                "last_name": "Wilson",
                "email": "emma.wilson@enterprise.com",
                "phone": "+1-555-0108",
                "password": "password123",
                "created_at": datetime.now() - timedelta(days=2)
            },
            {
                "first_name": "Robert",
                "last_name": "Taylor",
                "email": "robert.taylor@enterprise.com",
                "phone": "+1-555-0109",
                "password": "password123",
                "created_at": datetime.now() - timedelta(days=1)
            },
            {
                "first_name": "Amanda",
                "last_name": "Anderson",
                "email": "amanda.anderson@enterprise.com",
                "phone": "+1-555-0110",
                "password": "password123",
                "created_at": datetime.now()
            }
        ]
        
        print("🔄 Adding demo users to database...")
        
        # Add each demo user
        for i, user_data in enumerate(demo_users, 1):
            try:
                # Check if user already exists
                if not db_service.email_exists(user_data["email"]):
                    # Create user
                    user_id = auth_service.register_user(
                        user_data["first_name"],
                        user_data["last_name"],
                        user_data["email"],
                        user_data["phone"],
                        user_data["password"]
                    )
                    
                    # Update the created_at timestamp
                    db_service.cursor.execute('''
                        UPDATE customers 
                        SET created_at = ? 
                        WHERE id = ?
                    ''', (user_data["created_at"].strftime('%Y-%m-%d %H:%M:%S'), user_id))
                    db_service.conn.commit()
                    
                    print(f"✅ Added user {i}: {user_data['first_name']} {user_data['last_name']} ({user_data['email']})")
                else:
                    print(f"⚠️  User {i} already exists: {user_data['email']}")
                    
            except Exception as e:
                print(f"❌ Error adding user {i}: {str(e)}")
        
        # Show final statistics
        total_users = db_service.get_customer_count()
        print(f"\n📊 Database Statistics:")
        print(f"   Total Users: {total_users}")
        print(f"   This Week: {db_service.get_recent_registrations_count(7)}")
        print(f"   Today: {db_service.get_today_registrations_count()}")
        
        print("\n🎉 Demo users added successfully!")
        print("💡 You can now log in with any of these demo accounts using password: password123")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    add_demo_users()
