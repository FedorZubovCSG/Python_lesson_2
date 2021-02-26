import requests
import json

url=https://youtu.be/yDly4gmLLHg
response = requests.get(url)
data = json.loads(response.text)
print(response)
