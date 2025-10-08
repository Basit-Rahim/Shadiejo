#!/usr/bin/env python3
"""
Test the fallback email functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.email import email_service

def test_fallback_email():
    """Test the fallback email functionality"""
    print("🧪 Testing Fallback Email Service")
    print("=" * 50)
    
    # Test verification email
    print("1. Testing verification email...")
    result = email_service.send_verification_email(
        to_email="test@example.com",
        user_name="Test User",
        verification_token="test_token_12345"
    )
    
    if result:
        print("✅ Verification email sent successfully (fallback)")
    else:
        print("❌ Verification email failed")
    
    print("\n" + "=" * 50)
    
    # Test welcome email
    print("2. Testing welcome email...")
    result = email_service.send_welcome_email(
        to_email="test@example.com",
        user_name="Test User"
    )
    
    if result:
        print("✅ Welcome email sent successfully (fallback)")
    else:
        print("❌ Welcome email failed")
    
    print("\n" + "=" * 50)
    print("✅ Fallback email testing completed!")

if __name__ == "__main__":
    test_fallback_email()
