#16
def even(n):
    if n%2==0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")
even(9)
#15
def div(a,b):
    if b==0:
        print("cant divide by zero")
    else:
        return a/b
print(div(3,4))
#14
def fibo(n):
    if n==0:
        return 0
    else:
        return n+fibo(n-1)
print(fibo(10))

#13
def multiply(a,b):
    ''' this function is to multiply two numbers '''
    return a*b
print(multiply.__name__)
print(multiply.__doc__)
print(multiply.__hash__())
#12
num= 0
def increment(n):
    counter =1
    counter +=1
    op= counter+num
    return op
print(increment(5))
#11
import requests
print((requests.get("https://api.github.com")).json)
#10
import math
print(math.sqrt((144)))
print(math.radians(90))
#9
def sumof_digits(n):
    if n==0:
        return 0
    else: return n%10 + sumof_digits(n//10)
print(sumof_digits(125))

#8
def add_allnums(n):
    if n==0:
        return 0
    else:
        return n+add_allnums(n-1)
print(add_allnums(10))
#7
def fact(n):
    if n==0:
        return 1
    else: return n*fact(n-1)

print(fact(5))

#6
s = lambda i: i * i
list1=[1,2,3,4,5]
print(list(map(s,list1)))
#5
add = lambda x,y:x+y
print(add(1,2))

#4
def calculate_area(length, width =10):
    area = length*width
    return area
print(calculate_area(10,20))
print(calculate_area(10))
#3
def fullname(FirstName, lastName):
    print(FirstName + " " + lastName)
fullname("Chitra","Manala")
#2
def square(num):
    return num*num
print(square(3))

#1
def greet(a):
    print(f"Hello Python learner {a}")

greet("Chitra")