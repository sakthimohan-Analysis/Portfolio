from django.core.management.base import BaseCommand
from core.models import Skill, Project

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database...')

        # Skills
        skills = [
            {'name': 'Python', 'proficiency': 90},
            {'name': 'Django', 'proficiency': 85},
            {'name': 'JavaScript', 'proficiency': 80},
            {'name': 'React', 'proficiency': 75},
            {'name': 'TailwindCSS', 'proficiency': 90},
        ]

        created_skills = []
        for s in skills:
            skill, created = Skill.objects.get_or_create(name=s['name'], defaults={'proficiency': s['proficiency']})
            if created:
                self.stdout.write(f"Created Skill: {skill.name}")
            created_skills.append(skill)

        # Projects
        projects = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured e-commerce site built with Django and React. Features include user authentication, payment processing, and order tracking.',
                'github_link': 'https://github.com/example/ecommerce',
                'live_link': 'https://example.com',
            },
            {
                'title': 'Portfolio Website',
                'description': 'A modern portfolio website featuring 3D elements and smooth animations using Three.js and GSAP.',
                'github_link': 'https://github.com/example/portfolio',
                'live_link': 'https://example.com',
            },
        ]

        for p in projects:
            project, created = Project.objects.get_or_create(
                title=p['title'],
                defaults={
                    'description': p['description'],
                    'github_link': p['github_link'],
                    'live_link': p['live_link']
                }
            )
            if created:
                project.technologies.set(created_skills[:3]) # Add some skills
                project.save()
                self.stdout.write(f"Created Project: {project.title}")

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
