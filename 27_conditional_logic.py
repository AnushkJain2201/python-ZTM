is_old = True
is_licenced = True

# if is_old:
#     print('you are old enough to drive')
# elif is_licenced:
#     print('you are not old enough to drive and have a valid license')
# else:
#     print('you are not old enough to drive')

if is_old and is_licenced:
    print('you are old enough to drive and have a valid license')
else:
    print('you are not old enough to drive')
    
# Truthy and falsy
# All values are truthy except for these values
# None
# False
# Numbers that are numerically equal to zero, including:
# 0
# 0.0
# 0j
# decimal.Decimal(0)
# fraction.Fraction(0, 1)
# Empty sequences and collections, including:
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# set() - an empty set
# '' - an empty str
# b'' - an empty bytes
# bytearray(b'') - an empty bytearray
# memoryview(b'') - an empty memoryview
# an empty range, like range(0)
# objects for which
# obj.__bool__() returns False
# obj.__len__() returns 0, given that obj.__bool__ is undefined