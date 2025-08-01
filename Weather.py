import requests

api = "7d210ec7c4928c8fa5ba926211a3e57"
name = input("Enter the city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api}&units=metric"

r = requests.get(url)
data = r.json()

if r.status_code == 200 and "main" in data:
    temp = data['main']['temp']
    print(f"The temperature in {name} is: {temp}°C")
else:
    print("City not found or data not available.")