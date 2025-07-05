#!/usr/bin/env python3
"""
WSGI config for RPA project.
"""

import sys
import os

# Add the project directory to the Python path
path = '/home/yourusername/rpa-selenium'  # Cambiar por tu username
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['PYTHONPATH'] = path

# Import the Flask app
from app_simple import app as application

if __name__ == "__main__":
    application.run() 