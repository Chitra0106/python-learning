def add(num1,num2,plus =0): # plus is a default Argument and it is 0
    Op=num1+num2+plus
    return Op

print(add(1,2,3)) # here plus is overwritten to 3 from 0

#Keyword arguments
print(add(plus=10,num1=5,num2=20))
def Student(name,age):
    return name, age

print(Student(age=30, name ="John"))

