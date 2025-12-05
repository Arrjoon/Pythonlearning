import json

data = {
    "name": "Arjun",
    "skills": ["Python", "React"]
}

json_string = json.dumps(data)
print(json_string)
