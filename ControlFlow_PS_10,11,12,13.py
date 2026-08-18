#10
a = int(input("enter number"))
b= int(str(a)[::-1])
while a!=b:
    a = int(input("enter number"))
    b = int(str(a)[::-1])
    print(a,b)
#11
for i in range(1,11):
    print(i)
    if i>7:
        break

#12
