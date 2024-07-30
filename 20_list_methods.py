basket = [1, 2, 3, 4, 5]
print(len(basket))

# append(object)
# the important thing to note here is that append do not create a new list, but will change the original list
new_basket = basket.append(6)
print(new_basket) # none
print(basket)

# insert(index, object)
# insert also donot return a new list but changes the original list
basket.insert(2, 999)
print(basket)

# extend(iterable's object)
basket.extend([222, 333, 444])
print(basket)

# pop() pops off the last element of the list, pop returns the value that we removed
# basket.pop()
# print(basket)

# pop(index)
# basket.pop(2)
# print(basket)

# remove(value) it will remove the particular value that we provide in the method
# basket.remove(1)
# print(basket)

# clear() it will remove all the elements from the list
# basket.clear()
# print(basket)

# index(value) will return the index of the value provided
print(basket.index(2))

# index(value, start, end) will return the index of the value starting at start and ending at end index
#print(basket.index(2, 2, 5)) # gives an error

# reverse() will reverse the list in place
basket.reverse()
print(basket)

# count(value) will return the number of times the value provided is in the list
print(basket.count(2))

# in is a keyword to find a value exist in the list or not, returns a boolean; can even do it for strings
print(2 in basket)
print('d' in 'i am a doctor')

# sort() will sort the list in place
basket.sort()
print(basket)

# sorted() will return a new sorted list; it's not a method of list but a built in function
print(sorted(basket))

# copy() will create a new list and copy all the elements from the original list
copied_basket = basket.copy()
print(copied_basket)

# reverse using slicing
print(basket[:: -1])

# to generate a list fast
print(list(range(1, 100)))

# join() this method will concatenate all the elements of the list with the specified separator
print('-'.join(['apple', 'banana', 'cherry']))


