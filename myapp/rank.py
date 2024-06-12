import os
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
settings.configure()

from myapp.models import City

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
