#!/usr/bin/env python3
"""
Email Service Test Script for Enterprise CMS
Tests the Brevo SMTP configuration.
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import sys

def load_smtp_config():
    """Load SMTP configuration from smtp_config.py"""
    try:
        from smtp_config import SMTP_CONFIG
        return SMTP_CONFIG
    except ImportError:
        print("❌ Error: smtp_config.py not found!")
        return None

def send_test_email(smtp_config, recipient_email):
    """Send a test email using the SMTP configuration"""
    try:
        print(f"📧 Testing email service...")
        print(f"   Server: {smtp_config['server']}")
        print(f"   Recipient: {recipient_email}")
        
        # Create message
        msg = MIMEMultipart()
        # Use verified sender email if available, otherwise use username
        sender_email = smtp_config.get('sender_email', smtp_config['username'])
        sender_name = smtp_config.get('sender_name', 'Enterprise CMS')
        msg['From'] = f"{sender_name} <{sender_email}>"
        msg['To'] = recipient_email
        msg['Subject'] = "🧪 Enterprise CMS - Email Service Test"
        
        # Email body
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif;">
            <h2>✅ Email Service Test Successful!</h2>
            <p>This is a test email to verify that your Brevo SMTP service is working correctly.</p>
            <p><strong>Test Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>Your Enterprise CMS password reset emails will work properly!</p>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(body, 'html'))
        
        # Create SMTP session
        if smtp_config['use_tls']:
            server = smtplib.SMTP(smtp_config['server'], smtp_config['port'])
            server.starttls(context=ssl.create_default_context())
        else:
            server = smtplib.SMTP_SSL(smtp_config['server'], smtp_config['port'])
        
        # Login and send
        server.login(smtp_config['username'], smtp_config['password'])
        text = msg.as_string()
        server.sendmail(smtp_config['username'], recipient_email, text)
        server.quit()
        
        print("✅ Test email sent successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 ENTERPRISE CMS - EMAIL SERVICE TEST")
    print("=" * 50)
    
    # Load SMTP configuration
    smtp_config = load_smtp_config()
    if not smtp_config:
        return False
    
    # Get recipient email
    if len(sys.argv) > 1:
        recipient_email = sys.argv[1]
    else:
        recipient_email = input("📧 Enter recipient email address: ").strip()
    
    if not recipient_email:
        print("❌ No recipient email provided.")
        return False
    
    # Send test email
    success = send_test_email(smtp_config, recipient_email)
    
    if success:
        print("🎉 EMAIL SERVICE TEST SUCCESSFUL!")
        print("✅ Your Brevo SMTP service is working correctly.")
    else:
        print("❌ EMAIL SERVICE TEST FAILED!")
    
    return success

if __name__ == "__main__":
    main()
