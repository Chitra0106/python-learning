c=0 # global va
def Sum(a,b): #a,b are local variables
    global c # made it global
    c= a+b # c is local
    return c
    print(c)


print(Sum(2,3))
print(c)


