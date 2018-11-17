import json

with open('data.json', 'r') as jf:
     data = list(json.load(jf))
print(data)
