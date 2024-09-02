#Header: Matej Popovski
import requests

data = requests.get("https://leetcode-stats-api.herokuapp.com/matejpopovski")
print(data)
print('-----------')
data = data.json()
print(data)