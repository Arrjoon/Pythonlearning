import json

json_string = '{"name":"Arjun","age":22}'
print(type(json_string))
data = json.loads(json_string)


print(data['name'])

print("data type")
print(type(data))


print("data ",data)

