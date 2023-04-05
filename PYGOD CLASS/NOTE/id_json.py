import json

with open("id.json")as json_file:
    data = json.loads(json_file)
print(data[0]['name'])
print(data[0['email']])