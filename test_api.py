#!/usr/bin/env python3
"""
Test script for Email Domain Verifier API
"""
import json
import time
import sys

# Try to import requests, if not available, use urllib
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    import urllib.request
    import urllib.parse
    HAS_REQUESTS = False

def test_with_requests():
    """Test using requests library"""
    base_url = "http://127.0.0.1:8000"
    
    print("🧪 Testing Email Domain Verifier API with requests...")
    print("=" * 50)
    
    # Test 1: Single email verification - disposable
    print("\n📧 Test 1: Verifying disposable email (tempmail.org)")
    try:
        response = requests.post(
            f"{base_url}/api/verify/",
            json={"email": "test@tempmail.org"},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Status: {response.status_code}")
            print(f"📧 Email: {result.get('email')}")
            print(f"🌐 Domain: {result.get('domain')}")
            print(f"🚨 Is Disposable: {result.get('is_disposable')}")
            print(f"⚠️  Is Suspicious: {result.get('is_suspicious')}")
            print(f"💬 Message: {result.get('message')}")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 2: Single email verification - legitimate
    print("\n📧 Test 2: Verifying legitimate email (gmail.com)")
    try:
        response = requests.post(
            f"{base_url}/api/verify/",
            json={"email": "test@gmail.com"},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Status: {response.status_code}")
            print(f"📧 Email: {result.get('email')}")
            print(f"🌐 Domain: {result.get('domain')}")
            print(f"🚨 Is Disposable: {result.get('is_disposable')}")
            print(f"⚠️  Is Suspicious: {result.get('is_suspicious')}")
            print(f"💬 Message: {result.get('message')}")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 3: Bulk email verification
    print("\n📧 Test 3: Bulk email verification")
    test_emails = [
        "user1@gmail.com",
        "user2@tempmail.org",
        "user3@10minutemail.com",
        "user4@yahoo.com",
        "user5@mailinator.com"
    ]
    
    try:
        response = requests.post(
            f"{base_url}/api/bulk-verify/",
            json={"emails": test_emails},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Status: {response.status_code}")
            print(f"📊 Total Verified: {result.get('total')}")
            print(f"🚨 Disposable Count: {result.get('disposable_count')}")
            print(f"⚠️  Suspicious Count: {result.get('suspicious_count')}")
            print("\n📋 Results:")
            for i, res in enumerate(result.get('results', []), 1):
                status = "🚨 DISPOSABLE" if res.get('is_disposable') else "✅ LEGITIMATE"
                print(f"  {i}. {res.get('email')} → {status}")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 4: Invalid email format
    print("\n📧 Test 4: Invalid email format")
    try:
        response = requests.post(
            f"{base_url}/api/verify/",
            json={"email": "invalid-email"},
            headers={"Content-Type": "application/json"}
        )
        
        result = response.json()
        print(f"✅ Status: {response.status_code}")
        print(f"🚨 Is Valid: {result.get('is_valid')}")
        print(f"💬 Message: {result.get('message')}")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_with_urllib():
    """Test using urllib (fallback)"""
    base_url = "http://127.0.0.1:8000"
    
    print("🧪 Testing Email Domain Verifier API with urllib...")
    print("=" * 50)
    
    def make_request(endpoint, data):
        url = f"{base_url}{endpoint}"
        json_data = json.dumps(data).encode('utf-8')
        
        req = urllib.request.Request(
            url,
            data=json_data,
            headers={'Content-Type': 'application/json'}
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                return response.getcode(), json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            return e.code, {"error": str(e)}
    
    # Test single email verification
    print("\n📧 Testing single email verification...")
    status_code, result = make_request("/api/verify/", {"email": "test@tempmail.org"})
    print(f"Status: {status_code}")
    print(f"Is Disposable: {result.get('is_disposable')}")
    print(f"Message: {result.get('message')}")

def main():
    print("🚀 Email Domain Verifier API Test Suite")
    print("=" * 60)
    
    # Wait a moment for server to start
    print("⏳ Waiting for server to start...")
    time.sleep(3)
    
    if HAS_REQUESTS:
        test_with_requests()
    else:
        print("📦 requests library not available, using urllib...")
        test_with_urllib()
    
    print("\n" + "=" * 60)
    print("✅ Testing completed!")
    print("\n🌐 You can also test the web interface at:")
    print("   http://127.0.0.1:8000")
    print("\n📊 View statistics at:")
    print("   http://127.0.0.1:8000/stats/")
    print("\nℹ️  Learn more at:")
    print("   http://127.0.0.1:8000/about/")

if __name__ == "__main__":
    main() 