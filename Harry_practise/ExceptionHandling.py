from logging import exception

try:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    if b==0:
        raise ZeroDivisionError("should not divide with 0")
    sum = a+b
    div = a/b
    print(f" {sum}  , {div} for 2 numbers")
except ValueError:
    print("enter numeric value")
except ZeroDivisionError:
    print("enter numeric value")
except NameError:
    print("enter numeric value")
except exception as e:
    print("enter valid number error occured",e)
else:
    print("enter valid number error occured")



