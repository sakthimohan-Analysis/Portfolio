import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from django.contrib.auth.models import User

username = 'sakthi'
password = '123'

if not User.objects.filter(username=username).exists():
    User.objects.create_user(username=username, password=password)
    print(f"User '{username}' created successfully.")
else:
    print(f"User '{username}' already exists.")
