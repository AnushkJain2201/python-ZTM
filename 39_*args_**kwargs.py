# *args, **kwargs

# *args will help in passing multiple arguments in a function
def super_func(*args, **kwargs):
    
    print(args)  # will print a tuple containing all the positional arguments
    print(kwargs)  # will print a dictionary containing all the keyword arguments
    
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

# calling the function with positional arguments and keyword arguments
print(super_func(1, 2, 3, 4, 5, num1 = 5, num2 = 10))

# Rule for defining parameters 
# params, *args, default parameters, **kwargs