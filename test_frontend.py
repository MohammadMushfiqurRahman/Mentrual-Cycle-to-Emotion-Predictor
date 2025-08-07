import requests

# Test the frontend input form
url = "http://127.0.0.1:8000/predictor/"

try:
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response contains form: {'<form' in response.text}")
    print(f"Page title: {response.text.split('<title>')[1].split('</title>')[0] if '<title>' in response.text else 'No title found'}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    print("Make sure the Django server is running on http://127.0.0.1:8000/")