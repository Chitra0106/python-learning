# args will be atuple of all values passsed
def sum(*args):
    for arg in args:
        print(arg+arg)

c = sum(1,2,3,4)
print(c)
def marks(**kwargs):
    for arg in kwargs.keys():
        print(arg, kwargs[arg])

marks(Chitra = 100)
a = [1, 2]
b = a
a = a + [3]
print(b)

