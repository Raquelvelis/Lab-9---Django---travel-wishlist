# !/usr/bin/env python
"""Script to automatically run Django migrations."""
import os
import sys
import django

# Add the wishlist directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'wishlist'))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wishlist.settings')
django.setup()

from django.core.management import call_command


def run_migrations():
    """Run Django migrations to create database tables."""
    print("Creating migrations if needed...")
    try:
        call_command('makemigrations', interactive=False)
        print("✓ Migrations created (if any were needed)")
    except Exception as e:
        print(f"Note: {e}")

    print("\nApplying migrations to database...")
    try:
        call_command('migrate', interactive=False)
        print("✓ All migrations applied successfully!")
        print("\nDatabase tables have been created.")
        print("You can now run your tests with: python manage.py test")
    except Exception as e:
        print(f"✗ Error applying migrations: {e}")
        return False

    return True


if __name__ == '__main__':
    success = run_migrations()
    sys.exit(0 if success else 1)