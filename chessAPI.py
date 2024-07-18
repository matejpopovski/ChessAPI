# from chessdotcom import get_player_profile, Client
# Client.request_config["headers"]["User-Agent"] = (
# "My Python Application. "
# "Contact me at email@example.com"
# )
# response = get_player_profile("fabianocaruana")
# player_name = response.json['player']['name']
# #or
# player_name = response.player.name 

# import requests
# x = requests.get("https://api.chess.com/pub/player/MatejPopovski")
# print(x.json())

# import requests

# url = "https://api.chess.com/pub/player/MatejPopovski"
# response = requests.get(url)

# # Print response headers for debugging
# print("Response Headers:", response.headers)

# # Check the status code of the response
# if response.status_code == 200:
#     try:
#         # Attempt to parse the response as JSON
#         json_data = response.json()
#         print(json_data)
#     except requests.exceptions.JSONDecodeError:
#         # Handle JSON decode error
#         print("Response content is not valid JSON")
#         print("Raw response content:", response.text)
# else:
#     # Handle non-200 status codes
#     print(f"Request failed with status code: {response.status_code}")
#     print("Response content:", response.text)

import requests

headers = {
 'User-Agent': 'contact matej.popovski@gmail.com if there is a problem!'
}

x = requests.get("https://api.chess.com/pub/player/MatejPopovski/stats", headers=headers)

print(x.json())