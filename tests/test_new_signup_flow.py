#!/usr/bin/env python3
"""
Test the new signup flow - users are only created after email verification
"""

import requests
import json

def test_new_signup_flow():
    """Test the new signup process"""
    base_url = "http://localhost:8000"
    
    print("🚀 Testing New Signup Flow (Email Verification First)")
    print("=" * 60)
    
    # Test data
    test_user = {
        "name": "Test User New Flow",
        "email": "newflow@example.com",
        "phone": "+1234567890",
        "password": "testpassword123",
        "role": "user"
    }
    
    print("1. Testing user signup (should NOT create user in database)...")
    try:
        response = requests.post(
            f"{base_url}/auth/signup",
            json=test_user,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("   ✅ Signup successful - verification email sent")
            print(f"   📧 Message: {result.get('message', 'No message')}")
            print(f"   📧 Email: {result.get('email', 'No email')}")
            
            # Check if user exists in database (should NOT exist yet)
            print("\n2. Checking if user exists in database (should be empty)...")
            users_response = requests.get(f"{base_url}/auth/oauth/users")
            if users_response.status_code == 200:
                users_data = users_response.json()
                user_emails = [user['email'] for user in users_data.get('users', [])]
                
                if test_user['email'] in user_emails:
                    print("   ❌ User should NOT exist in database yet!")
                else:
                    print("   ✅ User correctly NOT in database yet")
                    print(f"   📊 Total users in database: {len(users_data.get('users', []))}")
            
            # Test login with unverified user (should fail)
            print("\n3. Testing login with unverified user (should fail)...")
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
                print("   ✅ Login correctly blocked (user doesn't exist yet)")
            else:
                print("   ❌ Login should be blocked")
            
            print("\n4. Next steps:")
            print("   📧 Check console for verification email content")
            print("   🔗 Copy the verification link from console")
            print("   🌐 Visit the verification link to create the user")
            
        else:
            print(f"   ❌ Signup failed: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection error - make sure the server is running")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("✅ New signup flow testing completed!")

if __name__ == "__main__":
    test_new_signup_flow()
