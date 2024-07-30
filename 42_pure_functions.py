# A function is called pure function if it always returns the same result for same argument values and it has no side effects like modifying an argument (or global variable) or outputting something. The only result of calling a pure function is the return value.

# An example of a pure function
def multiply_by_2(li):
    new_list = []
    for num in li:
        new_list.append(num * 2)
    return new_list

# An example of a function with side effects as it uses the print function
def multiply_by_2(li):
    new_list = []
    for num in li:
        new_list.append(num * 2)
    print(new_list)
    
