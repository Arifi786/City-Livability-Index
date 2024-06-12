# myapp/management/commands/import_cities.py

import csv
from django.core.management.base import BaseCommand
from myapp.models import City

class Command(BaseCommand):
    help = 'Import cities data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                City.objects.create(
                    city_name=row['District'],
                    state=row['State'],
                    population= int(row['Population'].replace(',', '')) ,
                    growth=float(row['Growth'].replace('%', '')) ,
                    literacy=row['Literacy']
                )
        self.stdout.write(self.style.SUCCESS('Cities data imported successfully'))
