from django.shortcuts import render, HttpResponse
import requests
import datetime


def home(request):

    unsplash_access_key = 'tpzvIjb5VjAPUMzywh94f9m8yFZDRN6fOhbHrELNzRQ'
    if 'city' in request.POST:
      city = request.POST['city']
    else:
      city = 'Ernakulam'

    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=131da488b326fb7e0f1b8fddf1543d33'
    geo_data = requests.get(url).json()

    params = {'units': 'metric'}

    if geo_data:
      lat = geo_data[0]['lat']
      lon = geo_data[0]['lon']

      w_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=131da488b326fb7e0f1b8fddf1543d33'
      data = requests.get(w_url, params).json()

      description = data['weather'][0]['description']
      icon = data['weather'][0]['icon']
      temp = data['main']['temp']
    else:

      description, icon, temp = "Not Found", "", "N/A"


    city_background_url = f'https://api.unsplash.com/photos/random?query={city},cityscape&client_id={unsplash_access_key}'
    city_background = requests.get(city_background_url).json()

    city_image = city_background.get('urls', {}).get('regular', 'https://unsplash.com')

    day = datetime.date.today()
    return render(request, 'home.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city_image':city_image})

