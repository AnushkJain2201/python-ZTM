def say_hello():
    print("Hello, World!")
    
say_hello()


def introduction(name, age):
    print(f"Hello, I am {name} and I am {age} years old")
    
# these are positional arguments; they are required to be specified positions
introduction('Anushk', 23)

# these are keyword arguments; they can be specified in any order
introduction(age=22, name='Raju')

# default parameters
def greet(name = "Rampal", age=34):
    print(f"Hello, I am {name} and I am {age} years old")

# greet() will use the default parameters
greet()

# return
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print(result)