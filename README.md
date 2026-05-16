# Django Weather App
-----------------------
A simple weather web application built with Django that shows the current weather of any city along with a dynamic background image of that city.

The application fetches weather data from the OpenWeatherMap API and a city image from the Unsplash API.


## Features
---------------
- Search weather by city name
- Displays temperature in Celsius
- Shows weather description and icon
- Dynamic city background image
- Default city display when no city is entered

## Tech Stack
--------------
Backend:
- Python
- Django

Frontend:
- HTML
- CSS

APIs Used:
- OpenWeatherMap API
- Unsplash API

---

## Project Structure
--------------------
weather_project/
│
├── manage.py
├── weather_app/
│ ├── views.py
│ ├── models.py
│ ├── urls.py
│ ├── settings.py
│ ├── templates/
│   └── home.html
│ 
│
└── requirements.txt

## Installation
------------------

```bash
git clone  https://github.com/achintyah9895/Weather-App.git
cd Weather-App
python -m venv menv
source menv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver

