#!/usr/bin/env python3
"""
Test SMTP email functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.email import email_service
from app.core.config import settings

def test_smtp_configuration():
    """Test SMTP configuration"""
    print("🔧 SMTP Configuration Test")
    print("=" * 50)
    
    print(f"SMTP Server: {settings.smtp_server}")
    print(f"SMTP Port: {settings.smtp_port}")
    print(f"SMTP Username: {settings.smtp_username}")
    print(f"SMTP Password: {'*' * len(settings.smtp_password) if settings.smtp_password else 'Not set'}")
    print(f"SMTP Use TLS: {settings.smtp_use_tls}")
    print(f"From Email: {settings.smtp_from_email}")
    
    if all([settings.smtp_server, settings.smtp_username, settings.smtp_password]):
        print("✅ SMTP configuration looks complete")
        return True
    else:
        print("❌ SMTP configuration incomplete")
        print("📝 Please check your .env file for missing SMTP settings")
        return False

def test_verification_email():
    """Test sending verification email"""
    print("\n📧 Testing Verification Email")
    print("=" * 50)
    
    result = email_service.send_verification_email(
        to_email="test@example.com",
        user_name="Test User",
        verification_token="test_token_12345"
    )
    
    if result:
        print("✅ Verification email sent successfully")
    else:
        print("❌ Verification email failed")
    
    return result

def test_welcome_email():
    """Test sending welcome email"""
    print("\n🎉 Testing Welcome Email")
    print("=" * 50)
    
    result = email_service.send_welcome_email(
        to_email="test@example.com",
        user_name="Test User"
    )
    
    if result:
        print("✅ Welcome email sent successfully")
    else:
        print("❌ Welcome email failed")
    
    return result

if __name__ == "__main__":
    print("🧪 Testing SMTP Email Service")
    print("=" * 60)
    
    # Test configuration
    config_ok = test_smtp_configuration()
    
    if config_ok:
        # Test emails
        test_verification_email()
        test_welcome_email()
    else:
        print("\n⚠️ Skipping email tests due to incomplete configuration")
        print("\n📝 Required .env settings:")
        print("SMTP_SERVER=smtp.gmail.com")
        print("SMTP_PORT=587")
        print("SMTP_USERNAME=your-email@gmail.com")
        print("SMTP_PASSWORD=your-app-password")
        print("SMTP_USE_TLS=true")
        print("SMTP_FROM_EMAIL=your-email@gmail.com")
    
    print("\n" + "=" * 60)
    print("✅ SMTP email testing completed!")
