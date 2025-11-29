import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from django.contrib.auth.models import User

username = 'sakthi'

try:
    user = User.objects.get(username=username)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"User '{username}' has been promoted to superuser.")
except User.DoesNotExist:
    print(f"User '{username}' does not exist.")
