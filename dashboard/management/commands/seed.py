import csv

from django.core.management.base import BaseCommand, CommandError
from dashboard.models import Entry  # new
from config.settings import ENTRIES_DATAFILE

from ._utils import convert

class Command(BaseCommand):
    help = 'Seed the database with vaccination data'

    def handle(self, *args, **kwargs):
        try:
            with open(ENTRIES_DATAFILE, 'r') as fp:
                reader = csv.DictReader(fp)
                for i, row in enumerate(reader):
                    entry = Entry()  #
                    for k, v in row.items():
                        try:
                            value = convert(v)
                            setattr(entry, k, value)
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(e))
                    try:
                        entry.save()
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(e))
                    if i%1000 == 0: self.stdout.write(self.style.HTTP_INFO(i))
        except FileNotFoundError:
            raise CommandError(f'File "{ENTRIES_DATAFILE}" does not exist')

        self.stdout.write(self.style.SUCCESS('Successfully seeded database.'))