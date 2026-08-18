
#1
print("Hello, World ! Welcome to Python.")
#2
print("Twinkle twinkle little star \n How I wonder what you are")
#3
print("""Twinkle twinkle little star 
How I wonder what you are """)
#4
name = input("Enter your name: ")
Age = int(input("Enter your Age: "))
Height = int(input("Enter your Height: "))
if Age>7 and Height>100:
    Is_Student = True
else:
    Is_Student = False
print("Name is : "+ name+" student ; "+str(Is_Student))
#5
num = "45"
print(int(num)+10)
#6
fav_Food = input("What is you favourite Food")
print("WoW! I like "+fav_Food)
#7
a= int(input("Enter the fist Numbe:"))
b= int(input("Enter the second Numbe:"))
c = a+b
d= a-b
e = a*b
f=a%b
print(c,d,e,f)
#8
print("Python is Awsome\n This is a new Line \n this is a tab->\t<-")
#9
a= int(input("Enter the first Number:"))
b = a**2
c = a**3
print("Square is "+str(b)+" cube is :"+str(c))