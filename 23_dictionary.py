# Dictionary

dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "companies": ['Meta', 'Apple', 'Google', 'Twitter']
}

# Accessing values
print(dictionary["name"])
print(dictionary["age"])
print(dictionary["companies"])

# The keys of a dictionary can be anything immutable i.e. it can be boolean or numbers but it can't be list
dict = {
    123: [1, 2, 3, 4],
    True: 'hello',
    'name': 'John'
}

print(dict[123])
print(dict[True])
print(dict['name'])

# A key in a dictionary must be unique