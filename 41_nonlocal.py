# nonlocal keyword help in using the variable in the parent function
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner: ", x)
    
    inner()
    print("outer: ", x)

outer()