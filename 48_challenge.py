some_list = ['a', 'b', 'c', 'd', 'e', 'd' , 'g', 'a', 'c']
duplicate_list = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicate_list)