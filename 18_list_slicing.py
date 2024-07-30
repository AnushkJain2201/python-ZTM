amazon_cart=['notebooks', 'sunglasses', 'grapes', 'toys']

# print all the items
print(amazon_cart)

# print all the items excluding the every next item
print(amazon_cart[0::2])

# 0 inclusive and 2 exclusive
print(amazon_cart[0:2])

# unlike strings, lists are mutable 
amazon_cart[1] = 'sunglasses_new'
print(amazon_cart)

# the list slicing will create a new list, therefore mutating the sliced list will not affect the original list
sliced_list = amazon_cart[0:2]
sliced_list[0] = 'notebooks_new'
print(amazon_cart)
print(sliced_list)

# but here's a tricky thing, here we are not slicing but assigning the same list object to different variables, it means that the sliced_list and amazon_cart both point to same list, thus changing one will change the other
sliced_list = amazon_cart;
sliced_list[0] = 'gums'
print(amazon_cart)
print(sliced_list)