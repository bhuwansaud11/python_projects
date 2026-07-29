import requests
import json

def main(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c065aae5a3adbc9902a63b83f434455f&units=metric'
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException:
        print("Network error. Please check your connection.")
        return None

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    elif response.status_code == 404:
        print("City not found. Please check the city name.")
        return None
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
while True:

    city = input("City: ")
    city_info = main(city)

    if city_info:
        with open(f'city_{city}.json','w') as file:
            json.dump({
                "Temperature": city_info['main']['temp'],
                "Feels like": city_info['main']['feels_like'],
                "Description": city_info['weather'][0]['description'],
                "Humidity": city_info['main']['humidity'],
                "Wind speed": city_info['wind']['speed']},file,indent=4)
        print(f"Temperature: {city_info['main']['temp']}")
        print(f"Feels like: {city_info['main']['feels_like']}")
        print(f"Description: {city_info['weather'][0]['description']}")
        print(f"Humidity: {city_info['main']['humidity']}")
        print(f"Wind speed: {city_info['wind']['speed']}")
        print(f"Saved to city_{city}.json successfully")
    again = input("Check another city(y or n): ")
    if again.lower() == 'n':
        print("Thanks for visiting me...")
        print("Exiting...")
        break