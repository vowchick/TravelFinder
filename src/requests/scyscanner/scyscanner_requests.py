import requests

# Replace with your Skyscanner API key
api_key = "sh428739766321522266746152871799"

# Define the request URL
url = "https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create"

# Define the request headers with your API key
headers = {
    "x-api-key": api_key
}

# Define the request data as a dictionary
data = {
    "query": {
        "market": "UK",
        "locale": "en-GB",
        "currency": "GBP",
        "query_legs": [
            {
                "origin_place_id": {
                    "iata": "LHR"
                },
                "destination_place_id": {
                    "iata": "SIN"
                },
                "date": {
                    "year": 2023,
                    "month": 12,
                    "day": 22
                }
            }
        ],
        "adults": 1,
        "cabin_class": "CABIN_CLASS_ECONOMY"
    }
}

# Send the POST request
response = requests.post(url, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    print("Request was successful!")
    print(response.json())  # Assuming the response is in JSON format
else:
    print("Request failed with status code:", response.status_code)
