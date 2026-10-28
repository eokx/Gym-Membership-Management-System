"""
PulseFit - Gym Membership Management System
Compatibility entrypoint - runs the Django application launcher
"""
import sys
import subprocess

if __name__ == "__main__":
    subprocess.call([sys.executable, "run.py"])
