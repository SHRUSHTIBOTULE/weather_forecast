import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f"Weather in {city}: {weather.capitalize()}")
        print(f"Temperature: {temp}°C")
    else:
        print(f"Error: {data.get('message', 'Unable to fetch weather')}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "b94853202e255e72ea40f9687e142851"  # Replace with your OpenWeatherMap API key
    get_weather(city_name, api_key)
