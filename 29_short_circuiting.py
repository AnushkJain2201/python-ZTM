# while using the 'or' if the first value is True, it will ignore the second condition and start implementing the logic for the truthy value same in case of 'and' if the first condition is False, it will ignore the second condition and start implementing the logic for the truthy value

is_friend = True
is_user = False

if is_friend or is_user:
    print('user is friend or user')
    
if is_friend and is_user:
    print('user is friend or user')