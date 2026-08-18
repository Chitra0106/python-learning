def  divide(a, b):
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    try:
        d = a/b
        print(d)
    except Exception as e:
        print(e)
        #Finally will always execute
    finally:
        print(a)
        print(b)

divide(10,5)