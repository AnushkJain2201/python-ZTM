# map(function, iterable)
def multiply_by_2(item):
    return item * 2

# we will have to convert the map function to list as it return the object of map class
print(list(map(multiply_by_2, [1, 2, 3])))

# map is a pure function, it will not modify the global variable but create a new list instead
my_list = [2, 4, 6]
print(list(map(multiply_by_2, my_list)))
print(my_list)