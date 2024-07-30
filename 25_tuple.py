# Tuple
# tuple is like a list, but unlike list we cannot modify them. They are immutable
my_tuple = (1, 2, 3, 4)
# my_tuple[1] = 'z'; it will throw an error

print(my_tuple[1])
print(5 in my_tuple)

# when we have a single item in a tuple we always have to put a , after it
new_tuple = my_tuple[1: 2]
print(new_tuple)

# unpacking the tuple
a, b, *other = my_tuple
print(a)
print(b)
print(other)

# it has only two methods - count() AND index() 
print(my_tuple.count(2))
print(my_tuple.index(3))

print(len(my_tuple))