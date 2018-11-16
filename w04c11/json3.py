import json

somedata = [{'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4),
            'b': 3.0, 'c': {'x': 12, 'y': 100}}]

# translate this data structur into a json string
data_string = json.dumps(somedata)

# display the contents of the json encoded (serialized) string representation of our somedata data structure.
print('ENCODED:', data_string)

# now, let's reverse the process, deencoding (or deserialize) the data.
decoded = json.loads(data_string)

# and print the result
print('DECODED:', decoded)

# now, let's compare the results of the preencoded data, and the end result of the unencoded (deserialized data)
print('ORIGINAL:', type(somedata[0]['fname']))
print('DECODED :', type(decoded[0]['fname']))
print('ORIGINAL:', type(somedata[0]['occupation']))
print('DECODED :', type(decoded[0]['occupation']))
print('ORIGINAL:', type(somedata[0]['a']))
print('DECODED :', type(decoded[0]['a']))
print('ORIGINAL:', type(somedata[0]['b']))
print('DECODED :', type(decoded[0]['b']))
print('ORIGINAL:', type(somedata[0]['c']))
print('DECODED :', type(decoded[0]['c']))

# notice how tuple became a list!
