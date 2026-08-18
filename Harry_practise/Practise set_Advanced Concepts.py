#9
def sum(*Args):
    sum = 0
    for arg in Args:
        sum += arg
    print(sum)
print(sum(1,2,3,4,5,6,7,8,9,10))
def dict_args(*args,**kwargs):
    print(args)
    print(kwargs)
a = dict(a=1,b=2,c=3)
print(a)
#8
def repeat():
    print("repeat")
    print("repeat")
    print("repeat")
    return 50
if (a:=repeat())>10:
    print(a)
else:
    print("else")
list_ip = ["Python","rock","ai"]
lengths = [n for w in list_ip if (n:= len(w))>4]
print(lengths)


#7
numbers =[1,2,3,4,5,6,7,8,9,10]
cube_numbers =map(lambda x: x**3,numbers)
print(list(cube_numbers))
even_numbers = filter(lambda x : x%2==0,numbers)
print(list(even_numbers))
from functools import reduce
def prod_num(a,b):
    return a*b
reduce_num = reduce(prod_num,numbers)
print(reduce_num)
#6
class NegativeNumberError(Exception):
    pass
a= int(input("enter first number"))
b= int(input("enter last number"))
try:
    if type(a)!= int:
        raise TypeError
    elif b==0:
        raise ZeroDivisionError
    elif a<0:
        raise NegativeNumberError

except TypeError:
    print(f"enter in valid number error occured for {a}")
except ZeroDivisionError:
    print(f"enter in valid number error occured for {b}")
except NegativeNumberError: print("Negative number entered")
finally:
    print(a)
    print(b)


#5

class book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
    def __str__(self):
        print(f"{self.title} by {self.author}")
        return f"{self.title} by {self.author}"
    def __len__(self):
        return len(self.title)
a= book("Roadmap","Rao",100)
print(a.__str__())
print(a.__len__())
print(str(a))
print(len(a))

#4
class math_utils:
    school_name = "International school"
    def __init__(self):
        pass

    @staticmethod
    def sum_Num(a,b):
        return a+b
    @classmethod
    def description(cls):
        print(f"this is for class math - utils and the school is {cls.school_name}")
a=math_utils
print(math_utils.description())
print(a.sum_Num(10,90))
print(a.description())



#3
class employee:
    """Use	Meaning
self._salary	Actual storage variable (backing field)
self.salary	Property that runs getter/setter logic"""
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self._salary = int(salary)
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, new_salary):
        if int(self._salary) < 100:
            (self._salary) = new_salary
            return  new_salary
        else:
            return self.salary
e= employee("Jack", "Smith", 5)
e.salary = 134350
print(e.salary)
print(e.salary)
#2
import time
def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Function took {end-start} seconds")
    return wrapper
@timer_decorator
def sum_Num():
    total = 0
    for i in range(1000000):
        total += i
    print(total)
print(sum_Num())

#print(timer_decorator(sum_Num))  dont need this since sum_Num = timer_decorator(sum_Num) Python nternally done sice @ decorator used

#1
def greet():
    print("hello world")

def greet_decorator(func):
    def wrapper():
        print("Function is being called")
        func()
        print("Function is  called")
    return wrapper()
#greet()
print(greet_decorator(greet))
