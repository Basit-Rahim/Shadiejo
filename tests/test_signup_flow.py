#!/usr/bin/env python3
"""
Test the complete signup flow with email verification
"""

import requests
import json

def test_signup_flow():
    """Test the complete signup process"""
    base_url = "http://localhost:8000"
    
    print("🚀 Testing Signup Flow with Email Verification")
    print("=" * 50)
    
    # Test data
    test_user = {
        "name": "Test User",
        "email": "test@example.com",
        "phone": "+1234567890",
        "password": "testpassword123",
        "role": "user"
    }
    
    print("1. Testing user signup...")
    try:
        response = requests.post(
            f"{base_url}/auth/signup",
            json=test_user,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            user_data = response.json()
            print("   ✅ User created successfully!")
            print(f"   📧 Email: {user_data['email']}")
            print(f"   👤 Name: {user_data['name']}")
            print(f"   ✅ Verified: {user_data['is_verified']}")
            print(f"   🔒 Active: {user_data['is_active']}")
            
            # Test login with unverified user
            print("\n2. Testing login with unverified user...")
            login_data = {
                "email": test_user["email"],
                "password": test_user["password"]
            }
            
            login_response = requests.post(
                f"{base_url}/auth/login",
                json=login_data,
                headers={"Content-Type": "application/json"}
            )
            
            print(f"   Status Code: {login_response.status_code}")
            if login_response.status_code == 401:
                print("   ✅ Login correctly blocked for unverified user")
                print(f"   📝 Message: {login_response.json().get('detail', 'No message')}")
            else:
                print("   ❌ Login should be blocked for unverified user")
            
            # Test resend verification
            print("\n3. Testing resend verification...")
            resend_data = {"email": test_user["email"]}
            
            resend_response = requests.post(
                f"{base_url}/auth/resend-verification",
                json=resend_data,
                headers={"Content-Type": "application/json"}
            )
            
            print(f"   Status Code: {resend_response.status_code}")
            if resend_response.status_code == 200:
                print("   ✅ Resend verification successful")
            else:
                print(f"   ❌ Resend verification failed: {resend_response.text}")
            
        else:
            print(f"   ❌ Signup failed: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection error - make sure the server is running")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Signup flow testing completed!")
    print("\n📝 Next steps:")
    print("1. Check your email for verification link")
    print("2. Click the verification link")
    print("3. Try logging in again")

if __name__ == "__main__":
    test_signup_flow()
