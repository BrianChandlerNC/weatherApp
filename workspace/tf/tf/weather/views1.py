import json
import requests

# Create your views here.
with open("/home/tuckrodgers/workspace/tf/tf/weather/forecast.json", "r") as file:
    data = json.load(file)
    for i in data['properties']['periods']:
        print(i)
