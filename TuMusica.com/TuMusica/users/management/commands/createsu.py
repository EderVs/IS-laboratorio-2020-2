"""Command to create super user admin."""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """Django manage.py command."""

    def handle(self, *args, **options):
        """Handle create super user."""
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@admin.com", "admin")

