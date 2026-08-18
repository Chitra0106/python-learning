a= int(input("Enter a number"))
for number in range(0,a):
    if number%2 ==0:
        print("Even Number")
    elif number%2==1:
        print("Odd Number")
    else:
        print("Not a Number")