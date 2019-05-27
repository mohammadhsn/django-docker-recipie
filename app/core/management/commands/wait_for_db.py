import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write('Waiting for database...')
        connection = None
        while not connection:
            try:
                connection = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second ...')
                time.sleep(1)

        self.stderr.write(self.style.SUCCESS('Database available!'))
