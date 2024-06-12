import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import City

# Fetch data from the database
cities = City.objects.all()

# Calculate ranks for each criterion
for city in cities:
    # Calculate ranks for each criterion based on the data stored in the City object
    # Lower living cost, pollution, and crime rate are better, so we'll rank them inversely
    city.growth_rank = City.objects.filter(growth__gt=city.growth).count() + 1
    city.literacy_rank = City.objects.filter(literacy__gt=city.literacy).count() + 1
    city.Salary_rank = City.objects.filter(Salary__gt=city.Salary).count() + 1
    city.Living_Cost_rank = City.objects.filter(Living_Cost__lt=city.Living_Cost).count() + 1
    city.health_rank = City.objects.filter(health__gt=city.health).count() + 1
    city.Transportation_rank = City.objects.filter(Transportation__gt=city.Transportation).count() + 1
    city.education_rank = City.objects.filter(education__gt=city.education).count() + 1
    city.pollution_rank = City.objects.filter(Pollution__lt=city.Pollution).count() + 1
    city.crime_rank = City.objects.filter(crime__lt=city.crime).count() + 1

    # Save the updated ranks
    city.save()

print("Ranks updated successfully.")
