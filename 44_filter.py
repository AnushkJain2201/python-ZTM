# for filter, we will use the function that will return boolean values

def check_odd(item):
    return item % 2 

print(list(filter(check_odd, [1, 2, 3, 4, 6, 7, 5, 3, 2, 1])))