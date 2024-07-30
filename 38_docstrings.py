# Docstrings
# these are the comments at the starting of the function declaration that gives the information about the function
# this docstring will be shown in the popup window while calling the function
def greet_user(name):
    """
    This function greets a user by name.
    
    Parameters:
    name (str): The name of the user to be greeted.
    
    Returns:
    str: The greeting message.
    """
    return f"Hello, {name}!"

greet_user('Anushk')

# help() is a built in function to print the info about any function
help(greet_user)

# we can also get the same information from __doc__ method
print(greet_user.__doc__)