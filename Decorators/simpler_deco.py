def deco_function(original):
    def wrapper_function(*args, **kwargs):
        print('This is the execution of the inner function aka the wrapper')
        print('Pay attention: in a while it will return the original function result -->')
        return original(*args, **kwargs)
    return wrapper_function

@deco_function
def another_display(a, b):
    return print(a+b)

myfun2 = deco_function(another_display(2, 3))
myfun2