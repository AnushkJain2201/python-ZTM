dicto = {
    'basket': [1, 2 ,3],
    'greet': 'hello',
    'age': 30,
    'name': 'John'
}

# get(key) 
print(dicto.get('basket'))
print(dicto.get('age')) # will return none

# get(key, default_value) 
print(dicto.get('age', 23))

#uncommon way of creating a dictionary
user2 = dict(name='John')

# 'in' in dictionary
print('name' in user2)
print('basket' in dicto)

# keys() to get keys in the dictionary
print('age' in user2.keys())

# values() to get values in the dictionary
print(1 in user2.values())

# items() to get both keys and values in the dictionary in a form of tuple
print(dicto.items())

# clear() to clear the dictionary
user2.clear()
print(user2)

# copy() to create a copy of the dictionary
dicto2 = dicto.copy()
print(dicto)
print(dicto2)

# pop(key) to remove a key-value pair from the dictionary
print(dicto.pop('greet'))
print(dicto)

# popitem() to remove a random key-value pair from the dictionary
print(dicto.popitem())
print(dicto)

# update() to add or update key-value pairs in the dictionary
dicto.update({'age': 31, 'city': 'New York'})
print(dicto)
