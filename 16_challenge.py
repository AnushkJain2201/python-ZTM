username = input('enter the username')
password = input('enter the password')

length_password = len(password)
secrest = '*' * length_password

print(f"{username}, your password {secrest} is {length_password} characters long")
