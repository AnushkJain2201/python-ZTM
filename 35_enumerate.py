# Enumerate

# The special thing of enumerate is that it can iterate over an interable with the index

for i, char in enumerate('Hello000'):
    print(i, char)
    
for i, char in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(i, char)