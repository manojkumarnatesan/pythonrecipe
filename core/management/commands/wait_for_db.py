"""
Django Command to wait for the database to ba available
"""

from psycopg2 import OperationalError as Psycopg2OperationalError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command for wait for database ..."""
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except (Psycopg2OperationalError,OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second..")
        self.stdout.write(self.style.SUCCESS("Database available.."))