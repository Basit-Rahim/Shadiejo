#!/usr/bin/env python3
"""
Test script for email service functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.email import email_service

def test_email_credentials():
    """Test getting Nodemailer credentials"""
    print("🔍 Testing Nodemailer API credentials...")
    
    try:
        credentials = email_service.get_credentials()
        if credentials:
            print("✅ Successfully obtained Nodemailer credentials")
            print(f"📧 API Response: {credentials}")
            return True
        else:
            print("❌ Failed to get credentials")
            return False
    except Exception as e:
        print(f"❌ Error getting credentials: {e}")
        return False

def test_send_verification_email():
    """Test sending verification email"""
    print("\n🔍 Testing verification email sending...")
    
    try:
        result = email_service.send_verification_email(
            to_email="test@example.com",
            user_name="Test User",
            verification_token="test_token_123"
        )
        
        if result:
            print("✅ Verification email sent successfully")
            return True
        else:
            print("❌ Failed to send verification email")
            return False
    except Exception as e:
        print(f"❌ Error sending verification email: {e}")
        return False

def test_send_welcome_email():
    """Test sending welcome email"""
    print("\n🔍 Testing welcome email sending...")
    
    try:
        result = email_service.send_welcome_email(
            to_email="test@example.com",
            user_name="Test User"
        )
        
        if result:
            print("✅ Welcome email sent successfully")
            return True
        else:
            print("❌ Failed to send welcome email")
            return False
    except Exception as e:
        print(f"❌ Error sending welcome email: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Testing Email Service with Nodemailer API")
    print("=" * 50)
    
    # Test credentials
    credentials_ok = test_email_credentials()
    
    if credentials_ok:
        # Test sending emails
        test_send_verification_email()
        test_send_welcome_email()
    else:
        print("\n⚠️ Skipping email tests due to credential failure")
    
    print("\n" + "=" * 50)
    print("✅ Email service testing completed!")
