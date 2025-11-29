from django.contrib import admin
from .models import Project, Skill, Experience, Certification, ContactMessage

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Certification)
admin.site.register(ContactMessage)
