import json

data = ['Bob', 'Jones', '1234 Elm Street']
with open('data.json', 'w') as jf:
     json.dump(data, jf)
     json.dump(data, jf)
