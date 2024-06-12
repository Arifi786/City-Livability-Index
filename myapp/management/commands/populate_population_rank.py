# myapp/management/commands/populate_population_rank.py

from django.core.management.base import BaseCommand
from myapp.models import City

class Command(BaseCommand):
    help = 'Populates population rank for cities based on population'

    def handle(self, *args, **kwargs):
        # Fetch the population data ordered by population
        cities = City.objects.order_by('-population')

        # Assign ranks to each city based on population order
        rank = 1
        previous_population = None
        for city in cities:
            if city.population != previous_population:
                city.population_rank = rank
            else:
                city.population_rank = previous_rank
            city.save()
            previous_population = city.population
            previous_rank = rank
            rank += 1

        self.stdout.write(self.style.SUCCESS('Successfully populated population rank.'))
