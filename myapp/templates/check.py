# Import necessary modules
import os
import django
import numpy as np

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# Assuming you have a City model defined in models.py
from myapp.models import City

def fetch_data_from_django():
    # Fetch data using Django ORM
    cities = City.objects.all()

    # Convert fetched data to a numpy array
    data = np.array([[float(city.crime), float(city.Salary), float(city.Living_Cost), float(city.population),
                      float(city.literacy), float(city.education), float(city.health), float(city.Pollution),
                      float(city.Transportation)] for city in cities])
    return data

def normalize_data(data):
    return data / np.linalg.norm(data, axis=0)

def calculate_ideal_solution(data, weights):
    return np.max(data, axis=0) * weights

def calculate_negative_ideal_solution(data, weights):
    return np.min(data, axis=0) * weights

def calculate_euclidean_distance(data, ideal_solution, negative_ideal_solution):
    d_plus = np.linalg.norm(data - ideal_solution, axis=0)  # Calculate along columns
    d_minus = np.linalg.norm(data - negative_ideal_solution, axis=0)  # Calculate along columns
    return d_plus, d_minus


def calculate_similarity_score(d_plus, d_minus):
    return d_minus / (d_plus + d_minus)

# Given data points for Mumbai and Bagalkot
mumbai_data = np.array([10, 140000.00, 30000, 9356962, 89.91, 11, 10, 30, 10])
bagalkot_data = np.array([4, 10935.00, 56238.00, 1889752, 68.82, 6, 4, 20.35, 4])

# Normalize data
mumbai_normalized = normalize_data(mumbai_data)
bagalkot_normalized = normalize_data(bagalkot_data)

# Example weights (replace with your own)
#weights = np.array([-1, 3, -1, 1, 1, 3, 3, -0.5, 0.3])  # Adjust weights based on importance
weights = np.array([-10, 33.33, -10, 10, 10, 33.33, 33.33, -5,  3.33])
weights = weights / np.sum(weights)

# Calculate ideal and negative ideal solutions
mumbai_ideal_solution = calculate_ideal_solution(mumbai_normalized, weights)
bagalkot_ideal_solution = calculate_ideal_solution(bagalkot_normalized, weights)

mumbai_negative_ideal_solution = calculate_negative_ideal_solution(mumbai_normalized, weights)
bagalkot_negative_ideal_solution = calculate_negative_ideal_solution(bagalkot_normalized, weights)

# Calculate Euclidean distance
mumbai_d_plus, mumbai_d_minus = calculate_euclidean_distance(mumbai_normalized, mumbai_ideal_solution, mumbai_negative_ideal_solution)
bagalkot_d_plus, bagalkot_d_minus = calculate_euclidean_distance(bagalkot_normalized, bagalkot_ideal_solution, bagalkot_negative_ideal_solution)

# Calculate similarity score
mumbai_similarity_score = calculate_similarity_score(mumbai_d_plus, mumbai_d_minus)
bagalkot_similarity_score = calculate_similarity_score(bagalkot_d_plus, bagalkot_d_minus)

print("Mumbai Similarity Score:", mumbai_similarity_score)
print("Bagalkot Similarity Score:", bagalkot_similarity_score)
