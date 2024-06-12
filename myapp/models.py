from django.db import models

# Create your models here.
from django.db import models


class Arif(models.Model):
    # Define fields for your table
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Add more fields as needed


# models.py

from django.db import models


class City(models.Model):
    city_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    city_name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    population = models.IntegerField()
    literacy = models.DecimalField(max_digits=12, decimal_places=2)
    growth = models.DecimalField(max_digits=12, decimal_places=2)
    crime = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    health = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    education = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    Salary = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    Living_Cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    Transportation = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    Job = models.CharField(max_length=255,null=True,blank=True)
    Pollution = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True)
    population_rank = models.IntegerField(null=True, blank=True)
    pollution_rank = models.IntegerField(null=True, blank=True)
    Transportation_rank = models.IntegerField(null=True, blank=True)
    Job_rank = models.IntegerField(null=True, blank=True)
    Living_Cost_rank = models.IntegerField(null=True, blank=True)
    Salary_rank = models.IntegerField(null=True, blank=True)
    education_rank = models.IntegerField(null=True, blank=True)
    health_rank = models.IntegerField(null=True, blank=True)
    crime_rank = models.IntegerField(null=True, blank=True)
    growth_rank = models.IntegerField(null=True, blank=True)
    literacy_rank = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.city_name
