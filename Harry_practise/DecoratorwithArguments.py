def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                print(i)
                func(a)
        return wrapper
    return decorator
@repeat(7)
def print_sound(a):
    print(f"hello {a}")
print_sound(5)