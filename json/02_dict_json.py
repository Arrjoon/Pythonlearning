import json


dict = {"name":"Arjun Nepali","Roll no":19}

print(dict)

jsonobj = json.dumps(dict)

print("obj of json",jsonobj)
print(type(jsonobj))