#Header: Matej Popovski
import requests

data = requests.get("")
weather_data = data.json()

