"""
Application Configuration Module
"""

import os

# General Application Settings
APP_NAME = "Demo Service"
APP_VERSION = "1.0.0"
DEBUG = False
SECRET_KEY = "super-secret-default-key"

# Security Settings
ALLOWED_HOSTS = ["example.com", "api.example.com"]
CORS_ORIGIN_ALLOW_ALL = True

# Database Configuration
DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "admin"
DB_PASSWORD = "main_secure_password_789"
DB_NAME = "demo_db"

# Cloud Credentials
AWS_REGION = "us-east-1"
AWS_KEY = "AKIA_FAKE_DEMO_KEY_0000"
AWS_SECRET = "fake_secret_key_1234567890"

# External API Integrations
API_TIMEOUT = 30
MAX_RETRIES = 3
