from django.shortcuts import render
import json
import requests


# Create your views here.
def index (requests):
    with open("/home/tuckrodgers/workspace/tf/tf/weather/forecast.json", "r") as file:
        data = json.load(file)

    periods = data['properties']['periods']

    forecast_data = []

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
        
        forecast_data.append(weather)

    context = {'forecast_data': forecast_data}
    print(context)
    return render(requests, 'weather/weather.html', context)

