import requests

url = 'https://kalin-serverless-504-gwf9avgsepezcrdb.eastus-01.azurewebsites.net/api/http_trigger1?code=xoWH1DUU4msicUZwDcFTCEohvui4LtJymXJvZyZIiIVcAzFubct9QQ=='

body = {
    "cholesterol": 180
}

response = requests.post(url, json=body)

print(response.text)