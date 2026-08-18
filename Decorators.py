#A decorator is a function that wraps another function to
# add extra behavior before or after it, without modifying the original function.
def hello():
    print("hello")

def hello_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    return wrapper

hello()
hello_decorator(hello)
f = hello_decorator(hello)
f()
def sum(x):
    return  int(x)+int(x)
def sum_decorator(func):
    def wrapper(x):
        print(f"Before execution the value of x is :{x}")
        result = func(x)
        print(f"After execution the value of x is :{result}")
        return result
    return wrapper
dec_square = sum_decorator(sum)
dec_square(5)

def sub_decorator(func):
    def wrapper(x):
        print(f"Before execution the value of x is :{x}")
        result = func(x)
        print(f"After execution the value of x is :{result}")
        return result
    return wrapper
@sub_decorator
def sub(x):
    return int(x)-int(x)
sub(5)
