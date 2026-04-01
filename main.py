import requests

# 1. Setup your credentials
API_KEY = "c43a6b20d10d6df629591af869c66865"
CITY = "Proddatur"  # Your current location
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# 2. Fetch the data
response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    weather_desc = data['weather'][0]['description']

    print(f"Weather in {CITY}: {temp}°C, {weather_desc}")

    # 3. ECE Maintenance Logic (The impressive part!)
    print("\n--- Maintenance Alerts ---")
    if temp > 35:
        print("!! ALERT: High Heat. Check Suzuki Burgman engine oil level.")
    if humidity > 80:
        print("!! ALERT: High Humidity. Lubricate chain/moving parts to prevent rust.")
    if "rain" in weather_desc.lower():
        print("!! ALERT: Wet Conditions. Check tire pressure and brake grip.")
else:
    print("Error fetching data. Check your API key!") 
                                                                                                                                                                                                               