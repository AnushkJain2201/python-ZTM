total = 0

# By using the global keyword, the local scope can get access to the global variables
# It can feel like static variables

def count():
    global total
    total += 1
    return total

print(count())
print(count())
print(count())
print(count())
print(count())
print(count())

# Using global keyword gets confusing when the file is large
# So instead of using global keyword, we use dependencies injection, we pass the global variable in the arguments of a function
def count_with_dependency(total):
    total += 1
    return total


print(count_with_dependency(count_with_dependency(count_with_dependency(total))))

    
    