"""
PulseFit - Gym Membership Management System (Django Edition)
One-Click Launcher Script
"""

import os
import sys
import time
import threading
import webbrowser

# Ensure directory is in Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gym_project.settings")

def open_browser():
    """Wait for server to start, then automatically open in default web browser."""
    time.sleep(1.8)
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    import django
    from django.core.management import call_command

    django.setup()

    print("=" * 68)
    print("   [+] PULSEFIT - GYM MEMBERSHIP MANAGEMENT SYSTEM (DJANGO)")
    print("=" * 68)

    # 1. Apply database migrations
    print("  [*] Checking database migrations...")
    call_command("migrate", interactive=False)

    # 2. Seed initial sample data & superuser
    try:
        call_command("seed_data")
    except Exception as e:
        print(f"  [!] Note during seeding: {e}")

    print("=" * 68)
    print("  Server URL    : http://127.0.0.1:8000")
    print("  Django Admin  : http://127.0.0.1:8000/admin")
    print("  Admin Login   : Username: admin  |  Password: admin123")
    print("  Database      : db.sqlite3 (Django ORM)")
    print("  Press Ctrl+C to terminate the development server")
    print("=" * 68)

    # Launch browser automatically
    threading.Thread(target=open_browser, daemon=True).start()

    # Start Django Runserver
    call_command("runserver", "127.0.0.1:8000")
