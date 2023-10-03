import requests

response = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
print(response.json())
print("Convert from string to object ")
print(response.json)