# reduce donot come as the built in function of the python, to use the reduce we need to import it
from functools import reduce

#reduce(function, data, accumulator)
my_list = [1, 2, 3]

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator ,my_list, 0))