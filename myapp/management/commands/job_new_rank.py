# job_new_rank.py

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # Replace "myproject.settings" with your actual settings module
django.setup()

from django.core.management.base import BaseCommand
from django.db.models import Case, CharField, F, Value, When, IntegerField
from myapp.models import City

class Command(BaseCommand):
    help = 'Rank jobs based on preference within each field'

    def handle(self, *args, **kwargs):
        calculate_and_save_rank()
        self.stdout.write(self.style.SUCCESS('Job rankings updated successfully'))

def calculate_and_save_rank():
    # Define the weights for each job
    weights = {
        "IT": 5,
        "Engineering": 5,
        "Business": 4,
        "Construction": 3,
        "Small business": 3,
        "Labour": 2,
        "Agriculture": 2
    }

    # Annotate each row with points for each job
    cases = [When(Job__contains=job, then=Value(weights[job])) for job in weights.keys()]
    points_expression = sum(Case(*cases, output_field=IntegerField(), default=Value(0)) for job in weights.keys())
    ranked_cities = City.objects.annotate(total_points=points_expression)

    # Rank the cities based on total points
    ranked_cities = ranked_cities.order_by('-total_points')

    # Update ranks
    for index, city in enumerate(ranked_cities, start=1):
        city.Job_rank = index
        city.save()

    return ranked_cities
