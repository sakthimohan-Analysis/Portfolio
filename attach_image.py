import os
import django
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from django.core.files import File
from core.models import Project
from django.conf import settings

STATIC_SAMPLE = Path(settings.BASE_DIR) / 'static' / 'images' / 'sample_project.svg'

p = Project.objects.first()
if not p:
    print('No Project instance found. Create a project first or run populate_data.py')
else:
    if p.image:
        print(f'Project "{p.title}" already has an image: {p.image.url}')
    else:
        # Ensure we have the file
        if not STATIC_SAMPLE.exists():
            print('Sample image not found in static/images/sample_project.svg')
        else:
            with open(STATIC_SAMPLE, 'rb') as f:
                django_file = File(f)
                # Save to 'projects/' upload_to path; set name to 'sample_project.svg'
                p.image.save('sample_project.svg', django_file, save=True)
            print(f'Image attached to project "{p.title}". Image url: {p.image.url}')
