# list, set, dictionary comprehensions

# instead of creating a list like this, we can use comprehensions
# my_list = []
# for char in 'hello':
#     my_list.append(char)
    
# print(my_list)

# comprehensions => my_list= [param for param in iterable]

my_list = [i for i in 'hello']
# print(my_list)

# This will generate the list containing the numbers from 1 to 100
my_list2 = [num for num in range(1, 101)]
# print(my_list2)

# We can also define any operation in the first param, in this case we want to create a list that contains the numbers from 1 to 100 multiply by 2
my_list3 = [num*2 for num in my_list2]
# print(my_list3)

# We can also use condition in the comprehension
my_list4 = [num for num in range(1, 101) if num%2 == 0]
# print(my_list4)

# Set Comprehensions
my_set = {i for i in 'hello'}
# print(my_set)

# This will generate the list containing the numbers from 1 to 100
my_set2 = {num for num in range(1, 101)}
# print(my_set2)

# We can also define any operation in the first param, in this case we want to create a list that contains the numbers from 1 to 100 multiply by 2
my_set3 = {num*2 for num in my_set2}
# print(my_set3)

# We can also use condition in the comprehension
my_set4 = {num for num in range(1, 101) if num%2 == 0}
# print(my_set4)

#Dictionary comprehension
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6
}

# Here we are creating a dictionary that has values which is 2 to the power of values of simple_dict
my_dict = {key: value**2 for key, value in simple_dict.items() }
print(my_dict)

my_dict2 = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0 }
print(my_dict2)

my_dict3 = {num: num*2 for num in [1, 2, 3]}
print(my_dict3)
