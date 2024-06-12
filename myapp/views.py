from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect


from .TOPSIS import your_view_function
from .form import ArifForm


def arif_create(request):
    if request.method == 'POST':
        form = ArifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success/')  # Redirect to a success page or another URL
    else:
        form = ArifForm()
    return render(request, 'arif_create.html', {'form': form})


def success_view(request):
    return render(request, 'success_url.html')


# views.py

from django.shortcuts import render
from .models import City


def city_list(request):
    cities = City.objects.all()
    return render(request, 'city_list.html', {'cities': cities})


from .Result_Calculation import  city_ranking1


def display_city_ranking(request):


    ranked_cities1 = your_view_function(request)  # Call the imported function

    return render(request, 'city_ranking.html', {'ranked_cities': ranked_cities1})
def city_ranking(request):
    sorted_cities = city_ranking1(request)

    return render(request, 'city_ranking.html', {'sorted_cities': sorted_cities})






def display_city_ranking1(request):


    ranked_cities = city_ranking1(request)  # Call the imported function

    return render(request, 'city_ranking.html', {'ranked_cities12': ranked_cities})
from django.http import JsonResponse
from django.views import View
from myapp.models import City

class CitySearchView(View):
    print("her0")
    def get(self, request):
        print("hero")
        city_name = request.GET.get('city_name', None)
        if city_name:
            cities = City.objects.filter(city_name__icontains=city_name).values()
            return JsonResponse(list(cities), safe=False)
        return JsonResponse({'error': 'No city name provided'}, status=400)





from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import City

class CityDetailView(View):
    def get(self, request, city_id):
        city = get_object_or_404(City, pk=city_id)
        data = {

            'City_Name': city.city_name,
            'Population': city.population,
            'Education': city.education,
            'Transportation': city.Transportation,
            'Crime': city.crime,
            'Literacy': city.literacy,
            'Salary': city.Salary,
            'Living-Cost': city.Living_Cost,
            'Pollution': city.pollution

        }
        return JsonResponse(data)


