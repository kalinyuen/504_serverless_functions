import requests

url = 'https://lpl-cholesterol-250516108637.us-central1.run.app'

body = {
    "cholesterol": 80
}

response = requests.post(url, json=body)

print(response.text)