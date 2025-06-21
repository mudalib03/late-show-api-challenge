import os

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:<your_password>@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = "super-secret-key"  # You can change this to any random string
