#!/usr/bin/env python3
"""
Quick test of SMTP email service
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_email_service():
    """Test the email service with SMTP"""
    try:
        from app.services.email import email_service
        
        print("🧪 Testing SMTP Email Service")
        print("=" * 50)
        
        # Test verification email
        print("1. Testing verification email...")
        result = email_service.send_verification_email(
            to_email="your-test-email@example.com",  # Change this to your email
            user_name="Test User",
            verification_token="test_token_12345"
        )
        
        if result:
            print("✅ Verification email test completed")
        else:
            print("❌ Verification email test failed")
        
        print("\n2. Testing welcome email...")
        result = email_service.send_welcome_email(
            to_email="your-test-email@example.com",  # Change this to your email
            user_name="Test User"
        )
        
        if result:
            print("✅ Welcome email test completed")
        else:
            print("❌ Welcome email test failed")
        
        print("\n" + "=" * 50)
        print("✅ Email service testing completed!")
        
    except Exception as e:
        print(f"❌ Error testing email service: {e}")

if __name__ == "__main__":
    test_email_service()
