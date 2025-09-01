# SMTP Configuration Template
# Copy this file to smtp_config.py and fill in your actual credentials

SMTP_CONFIG = {
    'server': 'smtp-relay.brevo.com',
    'port': 587,
    'username': 'your_username@smtp-brevo.com',
    'password': 'your_smtp_password_here',
    'use_tls': True,
    'sender_email': 'your_verified_email@gmail.com',
    'sender_name': 'CMS System'
}

# Instructions:
# 1. Copy this file to smtp_config.py
# 2. Replace the placeholder values with your actual SMTP credentials
# 3. Make sure your sender_email is verified with your SMTP provider
# 4. Never commit smtp_config.py to version control
