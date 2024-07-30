for item in 'Hello World':
    print(item)

print('--------------------------------')
    
for i in [1, 2, 3, 4, 5, 6, 7]:
    print(i)
    
print('--------------------------------')
    
for i in {1, 2, 3, 4, 5, 6, 7}:
    print(i)
    
print('--------------------------------')

for i in (1, 2, 3, 4, 5, 6, 7):
    print(i)
    
print('--------------------------------')

users = {
    'name': 'Anushk',
    'age': 22,
    'city': 'Pune'
}

# this will only print the keys
for item in users:
    print(item)
    
# this will only print the values
for item in users.values():
    print(item)

for key, value in users.items():
    print(f'{key}: {value}')