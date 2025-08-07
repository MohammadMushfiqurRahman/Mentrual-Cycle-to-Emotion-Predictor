import requests

# Test the emotion prediction endpoint
url = "http://127.0.0.1:8000/predictor/predict/"
params = {
    "cycle_day": 14,
    "hormone_level": 75,
    "previous_emotion": "happy"
}

try:
    response = requests.get(url, params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    print("Make sure the Django server is running on http://127.0.0.1:8000/")