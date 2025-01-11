import requests

def fetch_weather(city):
    API_KEY = 'YOUR_API_KEY'  # O'zingizning OpenWeatherMap kalitingizni kiriting
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        print(f'City: {city}')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Weather: {weather_description}')
    else:
        print('Failed to retrieve data:', response.status_code)

fetch_weather('Tashkent')
