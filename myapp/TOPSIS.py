# Import necessary modules
import os
import django
import numpy as np
from django.shortcuts import render

from myapp.management.commands.job_updation import data
from myapp.models import City  # Assuming you have a City model defined in models.py

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

def fetch_data_from_django():
    # Fetch data using Django ORM
    cities = City.objects.all()

    # Convert fetched data to a numpy array
    # data = np.array([[city.crime, city.Salary, city.Living_Cost, city.population, city.literacy, city.education, city.health, city.Pollution, city.Transportation] for city in cities])
    data = np.array([[float(city.crime), float(city.Salary), float(city.Living_Cost), float(city.population),
                      float(city.literacy), float(city.education), float(city.health), float(city.Pollution),
                      float(city.Transportation)] for city in cities])
    return data

def normalize_data(data):


    return data / np.linalg.norm(data, axis=0)

def min_max_scaling(data):
    min_vals = np.min(data, axis=0)
    max_vals = np.max(data, axis=0)
    scaled_data = (data - min_vals) / (max_vals - min_vals)
    return scaled_data

def calculate_ideal_solution(data, weights):

    return np.max(data, axis=0) * weights

def calculate_negative_ideal_solution(data, weights):
    return np.min(data, axis=0) * weights

def calculate_euclidean_distance(data, ideal_solution, negative_ideal_solution):
    d_plus = np.linalg.norm(data - ideal_solution, axis=1)
    d_minus = np.linalg.norm(data - negative_ideal_solution, axis=1)

    return d_plus, d_minus

def calculate_similarity_score(d_plus, d_minus):
    return d_minus / (d_plus + d_minus)

def rank_cities(similarity_scores):
    return np.argsort(similarity_scores)[::-1]

def your_view_function(request):
    # Retrieve data from Django
    data = fetch_data_from_django()

    # Example weights (replace with your own)
    weights = np.array([-10, 15, -10, 5, 5, 15, 15, -10,  10])  # Adjust weights based on importance
    # Ensure the sum of weights equals 100
    # weights = np.array([15, 20, 5, 15, 10, 33, 33, 15, 20])  # Adjusted weights (without Literacy Growth)

    weights = (weights / np.sum(weights))

    #normalized_data = min_max_scaling(data)

    normalized_data = normalize_data(data)

    ideal_solution = calculate_ideal_solution(normalized_data, weights)

    negative_ideal_solution = calculate_negative_ideal_solution(normalized_data, weights)

    d_plus, d_minus = calculate_euclidean_distance(normalized_data, ideal_solution, negative_ideal_solution)
    similarity_scores = calculate_similarity_score(d_plus, d_minus)

    ranked_cities = []
    for i, score in enumerate(similarity_scores):
        ranked_cities.append({

            'name': City.objects.all()[i].city_name,
            'state': City.objects.all()[i].state,
            'score': "{:.2f}".format(score * 100)
        })
    ranked_cities = sorted(ranked_cities, key=lambda x: x['score'], reverse=True)
    rank = 1
    for i, city in enumerate(ranked_cities):
        city['rank'] = i + 1


    # Pass the ranked cities to the template for rendering
    return ranked_cities
