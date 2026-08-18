#1
from pygments.lexers.tablegen import TableGenLexer

a= int(input("enter a number"))
if a>18:
    print("eligible to vote")
else:
    print("not eligible to vote")
#2
a= int(input("enter a number from 1 to 7"))
match a:
    case 1:print("monday")
    case 2:print("tuesday")
    case 3:print("wednesday")
    case 4:print("thursday")
    case 5:print("friday")
    case 6:print("saturday")
    case 7:print("sunday")
#3
a= int(input("enter a number"))
b= int(input("enter a number"))
c= input("enter an opration from +,-,/,*,%")
match c:
    case "+":print(str(a+b))
    case "-":print(str(a-b))
    case "/":print(str(a/b))
    case "*":print(str(a/b))
    case "%":print(str(a%b))
#4
Num= 10
for i in range(0,Num):
    print("hi")
#5
for i in range(0,Num):
    print(" 9x ",i,"=",i*9)

#6
Sum = 0
for i in range(0,100):
    Sum +=i
    print(Sum)
#7
for i in range(1,10):
    print("*"*i)
#8
num=15
while num<6:
    print(num)
#9
Password = "1234567"
Enter_PW = input("enter password")
while Enter_PW !=Password:
    Enter_PW = input("enter password")
    print(Enter_PW)

#10
