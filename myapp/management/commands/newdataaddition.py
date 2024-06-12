

import csv
from django.core.management.base import BaseCommand
from myapp.models import City


class Command(BaseCommand):
    help = 'Import additional city data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Open the CSV file and iterate over its rows
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                city_name = row['District']
                state = row['State']

                # Retrieve the corresponding City object from the database
                try:
                    city = City.objects.get(city_name=city_name, state=state)
                except City.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'City {city_name} in state {state} not found. Skipping...'))
                    continue

                # Update the City object with the new fields
                city.crime = row.get('Crime', None)
                city.education = row.get('Education', None)
                city.health = row.get('Health_Facility', None)
                city.Job = row.get('Job_Opportunities', None)
                city.Living_Cost = row.get('Living_Cost', None)
                city.Pollution = row.get('Pollution', None)
                city.Salary = row.get('Salary', None)
                city.Transportation = row.get('Transportation', None)
                # Save the updated City object
                city.save()

        self.stdout.write(self.style.SUCCESS('Additional city data imported successfully'))
