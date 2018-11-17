import json

somedata = [{'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4), 'b': 3.0}]
print('DATA:', repr(somedata))

data_string = json.dumps(somedata)
print('JSON:', data_string)
