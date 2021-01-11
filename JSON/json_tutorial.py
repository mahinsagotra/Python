# JSON:
"""
JSON (JavaScript Object Notation) is a leightweight data format for data exchange. In Python you have the built-in json module for encoding and decoding JSON data. Simply import it and you are ready to work with JSON data:

import json
Some advantages of JSON:

JSON exists as a "sequence of bytes" which is very useful in the case we need to transmit (stream) data over a network.
Compared to XML, JSON is much smaller, translating into faster data transfers, and better experiences.
JSON is extremely human-friendly since it is textual, and simultaneously machine-friendly.
"""
from json import JSONEncoder
import json

person = {"name": "John", "age": 30, "city": "New York",
          "hasChildren": False, "titles": ["engineer", "programmer"]}

person_json = json.dumps(person)
# use different formatting style
person_json2 = json.dumps(
    person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
print(person_json)
print(person_json2)

# Or convert Python objects into JSON objects and save them into a file with the json.dump() method.
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# FROM JSON to Python (Deserialization, Decode)
# Convert a JSON string into a Python object with the json.loads() method. The result will be a Python dictionary.

person_dict = json.loads(person_json)
print(person_dict)

with open('person.json', 'r') as file:
    person_dict1 = json.load(file)

print(person_dict1)


# Working with Custom Objects
"""
Encoding
Encoding a custom object with the default JSONEncoder will raise a 
TypeError. We can specify a custom encoding function that will store 
the class name and all object variables in a dictionary. Use this 
function for the default argument in the json.dump() method.
"""


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)

# error Object not JSON serializable,
#userJson = json.dumps(user, indent=4)


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, o)


userJson = json.dumps(user, default=encode_user)

userJson = json.dumps(user, cls=UserEncoder)
# or
#userJson = UserEncoder().encode(user)

print(userJson)


"""
#Decoding
Decoding a custom object with the defaut JSONDecoder is possible, 
but it will be decoded into a dictionary. Write a custom decode 
function that will take a dictionary as input, and creates your custom 
object if it can find the object class name in the dictionary. Use this 
function for the object_hook argument in the json.load() method.
"""
user = json.loads(userJson)
print(user)


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    else:
        return dct


user = json.loads(userJson, object_hook=decode_user)
print(type(user))
print(user.name)
