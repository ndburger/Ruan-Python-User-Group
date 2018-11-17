import json
somedata = {'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4),
            'b': 3.0, 'c': {'x': 12, 'y': 100}}
print(somedata)

f = open('data.json', 'w')
json.dump(somedata, f)
f.close()

f = open('data.json', 'r')
somedata = json.load(f)
f.close()
print(somedata)

somedata['fname'] = 'Al'
f = open('data.json', 'w')
json.dump(somedata, f)
f.close()

f = open('data.json', 'r')
somedata = json.load(f)
f.close()
print(somedata)
