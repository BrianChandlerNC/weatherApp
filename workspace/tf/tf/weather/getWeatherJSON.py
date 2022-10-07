#!/usr/bin/env python3
import json
import requests


url = 'https://api.weather.gov/gridpoints/RAH/68,55/forecast'

r = requests.get(url).json()
    
with open('forecast.json', 'w+', encoding="utf-8") as f:
    json.dump(r, f, ensure_ascii=False, indent=4)
