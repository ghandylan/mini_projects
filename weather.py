import requests

API_KEY = "307fa7a0adc633c4eb6cf0a69207f710"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = str(input("Enter city name: "))
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    temperature = data["main"]["temp"] - 273.15
    print("The weather is",weather)
    print("The temperature is",round(temperature, 2),"Celsius")
else:
    print("An error occurred.")
