from django.shortcuts import render
from django.http import HttpResponse

import requests
from .models import City


def home(request):
    api = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8e8322284c78531efdce50f3da0a5111&units=metric'
    weather_list = []

    cities = City.objects.all()

    for city in cities:
        res = requests.get(api.format(city)).json()
        weather = {
            'city': city.name,
            'temperature': res['main']['temp'],
            'description': res['weather'][0]['description'],
            'icon': res['weather'][0]['icon']
        }
        weather_list.append(weather)

    print(weather_list)
    context = {'weather_list': weather_list}
    return render(request, 'weather/index.html', context)
