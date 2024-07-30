# Set
# set is simply the collection of unique objects

my_set = {1, 3, 4, 5, 3, 5} # it will not return the duplicate 3 and 5 but only return the single 3 and 5
print(my_set)

my_set.add(100)
print(my_set)

# how to remove duplicates from the list
my_list = [1, 2, 3, 3, 4, 5, 5]
my_set_from_list = set(my_list)
print(my_set_from_list)

# set donot support indexing
# print(my_set[1]) this will give an error that it's not subscriptable
print(3 in my_list)
print(len(my_list))

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

us_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# .difference()
print(us_set.difference(your_set))

# discard()
# print(us_set.discard(5))
# print(us_set)

# .difference_update() -> remove all elements from another set in this set
# us_set.difference_update(your_set)
# print(us_set)

# .intersection()
print(us_set.intersection(your_set))

# .isdisjoint() -> return True if there is no intersection
print(us_set.isdisjoint(your_set))

# .issubset()
print(us_set.issubset(your_set))

# .issuperset()
print(us_set.issuperset(your_set))

# .union()
print(us_set.union(your_set))


