from django.shortcuts import render
import requests
# Create your views here.


def index(request):
    api_url = 'https://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = None
    if request.method == "POST":
        city_name = request.POST['city']
        city_data = api_url + city_name
        response = requests.get(city_data)
        content = response.json()
        try:
            city = {
            'city': city_name,
            'temp': content['main']['temp'],
            'description': content['weather'][0]['description'],
            'icon': content['weather'][0]['icon']
            }
        except:
            city = None
    return render(request, 'weather.html', {'city_weather': city})

