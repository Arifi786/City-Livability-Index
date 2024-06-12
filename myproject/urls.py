"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

from myapp.Custom_rank import city_ranking2
from myapp.views import arif_create, success_view, city_list, display_city_ranking, city_ranking, display_city_ranking1, \
    CitySearchView, CityDetailView, CityDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
path('arif/create/', arif_create, name='arif_create'),
path('success/', success_view , name='success_url'),
path('cities/', city_list, name='city_list'),
path('city_ranking/',  display_city_ranking, name='city_ranking12'),
path('city_ranking1/',  city_ranking, name='city_ranking'),
path('city-ranking2/', city_ranking2, name='city_ranking2'),
path('api/search/', CitySearchView.as_view(), name='city-search'),
path('api/city/<int:city_id>/', CityDetailView.as_view(), name='city-detail'),
re_path(r'^.*', TemplateView.as_view(template_name='index.html')),

]




