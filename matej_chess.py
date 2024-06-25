from numpy import mean
import requests

data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
weather_data = data.json()

print(f"Latitude: {weather_data['latitude']}")
print(f"Longitude: {weather_data['longitude']}")
print(f"Timezone: {weather_data['timezone']}")
print(f"Current Temperature: {weather_data['current']['temperature_2m']} {weather_data['current_units']['temperature_2m']}")
print(f"Current Wind Speed: {weather_data['current']['wind_speed_10m']} {weather_data['current_units']['wind_speed_10m']}")

# Loop through the hourly data and print it
print("\nHourly Weather Data:")
allTemp = []
allHumidity = []
allWindSpeed = []
for i, time in enumerate(weather_data['hourly']['time']):
    temperature = weather_data['hourly']['temperature_2m'][i]
    allTemp.append(temperature)
    humidity = weather_data['hourly']['relative_humidity_2m'][i]
    allHumidity.append(humidity)
    wind_speed = weather_data['hourly']['wind_speed_10m'][i]
    allWindSpeed.append(wind_speed)
    #print(f"Time: {time}, Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} km/h")

print(f"Mean temp: ", mean(allTemp), "Mean humidity: ", mean(allHumidity), "Mean wind speed: ",  mean(allWindSpeed))

##change