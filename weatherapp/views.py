from django.shortcuts import render, HttpResponse
import requests
import datetime


def home(request):
  #  return HttpResponse('Hey this is my django server')

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

    day = datetime.date.today()
    return render(request, 'home.html',{'description':description,'icon':icon,'temp':temp,'day':day})

