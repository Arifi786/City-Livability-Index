import os
from django.http import JsonResponse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # Adjust "myproject.settings" to match your project's settings module

import django
django.setup()

from django.shortcuts import render
from myapp.models import City

def city_ranking1(request):
    # Retrieve cities data from MySQL database
    cities = City.objects.all()

    # Calculate overall ranking for each city
    ranked_cities = []
    for city in cities:
        overall_rank = ((640-city.health_rank + 640-city.education_rank +640-city.Salary_rank)*5+(640-city.Transportation_rank+640-city.literacy_rank+ 640-city.crime_rank+640-city.Living_Cost_rank)*2+(640-city.population_rank+640-city.pollution_rank)*1)/(640*12/60)
        ranked_cities.append({'name': city.city_name,'state':city.state,'overall_rank': overall_rank})
        print(overall_rank)

    # Sort cities based on overall ranking
    sorted_cities = sorted(ranked_cities, key=lambda x: x['overall_rank'], reverse=True)
    rank = 1
    for city in sorted_cities:
        city['rank'] = rank
        rank += 1

    return sorted_cities
