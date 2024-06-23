import requests

url = "https://api.chess.com/pub/player/MatejPopovski"
api_key = "YOUR_API_KEY"  # Replace with your actual Chess.com API key

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"  # Adjust content type if necessary
}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            print("Data received successfully:")
            print(data)
        except requests.exceptions.JSONDecodeError as e:
            print("JSON decoding error:", e)
    elif response.status_code == 403:
        print("Access forbidden. Check your API key or permissions.")
    else:
        print(f"Request failed with status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
