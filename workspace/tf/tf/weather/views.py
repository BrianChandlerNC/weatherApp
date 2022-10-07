from django.shortcuts import render
import json
import requests


# Create your views here.
def index (requests):
    with open("/home/tuckrodgers/workspace/tf/tf/weather/forecast.json", "r") as file:
        data = json.load(file)

    periods = data['properties']['periods']

    weather_data = []

    for period in periods:
        weather = {
                 'name'             : period['name'],
                 'temperature'      : period['temperature'],
                 'icon'             : period['icon'],
                 'detailedForecast' : period['detailedForecast'],
                 'windSpeed'        : period['windSpeed'],
                 'windDirection'    : period['windDirection'],
                 'startTime'        : period['startTime'],
                 'endTime'          : period['endTime']
        }
        
        weather_data.append(weather)

    context = {'weather_data': weather_data}
    print(context)
    return render(requests, 'weather/weather.html', context)

