print(range(1, 100))

for i in range(1, 101):
    print(i)
    
# range also comes with a third parameter, stepover
for i in range(1, 100, 2):
    print(i)
    
# if we change stepover to a negative value, it will go in the opposite direction
for i in range(100, 0, -1):
    print(i)
    
# we can also create a list using range 
print(list(range(1, 101)))