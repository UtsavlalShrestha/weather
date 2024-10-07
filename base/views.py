from django.shortcuts import render
import json 
import requests
import os
from dotenv import load_dotenv


# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
    else:
        city= 'Kathmandu'

    load_dotenv()
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    PARAMS = {'units':'metric'}

    final_data = requests.get(url, PARAMS).json()
    
#FORMAT ESTO CHA FOR THE JSON API
#     {
#    "coord": {
#       "lon": 7.367,
#       "lat": 45.133
#    },
#    "weather": [
#       {
#          "id": 501,
#          "main": "Rain",
#          "description": "moderate rain",
#          "icon": "10d"
#       }
#    ],
#    "base": "stations",
#    "main": {
#       "temp": 284.2,
#       "feels_like": 282.93,
#       "temp_min": 283.06,
#       "temp_max": 286.82,
#       "pressure": 1021,
#       "humidity": 60,
#       "sea_level": 1021,
#       "grnd_level": 910
#    },
#    "visibility": 10000,
#    "wind": {
#       "speed": 4.09,
#       "deg": 121,
#       "gust": 3.47
#    },
#    "rain": {
#       "1h": 2.73
#    },
#    "clouds": {
#       "all": 83
#    },
#    "dt": 1726660758,
#    "sys": {
#       "type": 1,
#       "id": 6736,
#       "country": "IT",
#       "sunrise": 1726636384,
#       "sunset": 1726680975
#    },
#    "timezone": 7200,
#    "id": 3165523,
#    "name": "Province of Turin",
#    "cod": 200
# }                    
  
    result = {
            "country_code": str(final_data['sys']['country']), 
            "current_weather": str(final_data['weather'][0]['description']),
            "temp": str(final_data['main']['temp']) + '°C', 
            "pressure": str(final_data['main']['pressure']), 
            "humidity": str(final_data['main']['humidity']), 
            "coordinate": str(final_data['coord']['lon']) + ' '+ str(final_data['coord']['lat']), 

        } 
    print(result)

    context = {'result': result}
    return render(request, 'base/home.html', context)