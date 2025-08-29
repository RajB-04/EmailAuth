#!/usr/bin/env python
"""
Startup script for Email Domain Verifier
This script properly initializes the database and starts the server
"""
import os
import sys
import subprocess
import time

def run_command(command, description):
    """Run a command and print its status"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        if result.stdout.strip():
            print(f"Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr.strip() if e.stderr else e.stdout.strip()}")
        return False

def main():
    print("🚀 Email Domain Verifier - Startup Script")
    print("=" * 60)
    
    # Change to the script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Step 1: Apply migrations
    if not run_command("python manage.py migrate", "Applying database migrations"):
        sys.exit(1)
    
    # Step 2: Populate disposable domains
    if not run_command("python manage.py populate_domains", "Populating disposable domains"):
        print("⚠️  Warning: Could not populate domains, but continuing...")
    
    # Step 3: Show database status
    print("\n📊 Database Status:")
    try:
        result = subprocess.run("python manage.py shell -c \"from verifier.models import DisposableDomain; print(f'Total domains: {DisposableDomain.objects.count()}')\"", 
                              shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout.strip())
        else:
            print("Could not check database status")
    except:
        print("Could not check database status")
    
    print("\n" + "=" * 60)
    print("🎉 Setup completed! Starting Django development server...")
    print("🌐 The application will be available at: http://127.0.0.1:8000")
    print("📊 Statistics page: http://127.0.0.1:8000/stats/")
    print("ℹ️  About page: http://127.0.0.1:8000/about/")
    print("\n⏹️  Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Step 4: Start the server
    try:
        subprocess.run("python manage.py runserver 8000", shell=True, check=True)
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 