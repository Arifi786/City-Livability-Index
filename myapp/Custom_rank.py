import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import City

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # Adjust "myproject.settings" to match your project's settings module

import django
django.setup()

def calculate_overall_rank(city, weights):
    return (
        (640 - city.health_rank) * weights['health_weight'] +
        (640 - city.education_rank) * weights['education_weight'] +
        (640 - city.Salary_rank) * weights['salary_weight'] +
        (640 - city.Transportation_rank) * weights['transportation_weight'] +
        (640 - city.literacy_rank) * weights['literacy_weight'] +
        (640 - city.crime_rank) * weights['crime_weight'] +
        (640 - city.Living_Cost_rank) * weights['living_cost_weight'] +
        (640 - city.population_rank) * weights['population_weight'] +
        (640 - city.pollution_rank) * weights['pollution_weight']
    ) / (
        (weights['health_weight'] + weights['education_weight'] + weights['salary_weight'] + weights['transportation_weight'] +
        weights['literacy_weight'] + weights['crime_weight'] + weights['living_cost_weight'] + weights['population_weight'] +
        weights['pollution_weight']) * 640 / 120
    )

@api_view(['GET'])
def city_ranking2(request):
    weights = {
        'health_weight': float(request.GET.get('health_weight', 5)),
        'education_weight': float(request.GET.get('education_weight', 5)),
        'salary_weight': float(request.GET.get('salary_weight', 5)),
        'transportation_weight': float(request.GET.get('transportation_weight', 2)),
        'literacy_weight': float(request.GET.get('literacy_weight', 2)),
        'crime_weight': float(request.GET.get('crime_weight', 2)),
        'living_cost_weight': float(request.GET.get('living_cost_weight', 2)),
        'population_weight': float(request.GET.get('population_weight', 1)),
        'pollution_weight': float(request.GET.get('pollution_weight', 1))
    }

    cities = City.objects.all()
    ranked_cities = []

    for city in cities:
        overall_rank = calculate_overall_rank(city, weights)
        ranked_cities.append({
            'name': city.city_name,
            'state': city.state,
            'overall_rank': overall_rank
        })

    sorted_cities = sorted(ranked_cities, key=lambda x: x['overall_rank'], reverse=True)
    rank = 1
    for city in sorted_cities:
        city['rank'] = rank
        rank += 1

    return JsonResponse(sorted_cities, safe=False)
