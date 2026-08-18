#8
PalindromStr = "45554"
if PalindromStr == PalindromStr[::-1]:
    print(PalindromStr+" is a palindrome")
else:
    print(PalindromStr+" is not a palindrome")


#7
Inputstring =  "Chitra"
print(Inputstring.lower().count("a")+Inputstring.count("e")+Inputstring.count("i")+Inputstring.count("o")+Inputstring.count("u"))
Sentence = "Chitra Manala"
sum=0
vowels = ["a","e","i","o","u"]
for char in Sentence:
    if char in vowels:
        sum+=1
print(sum)
#6
string1= "Python is fun"
print(string1.replace("fun","Awsome"))
print(string1.index("Python"))
print(string1.upper())
#5
name=  'chitra manala'
Role = "AI engineer"
print(f" Hello {name},\n Congratulations! \n you have selected for the role of {Role}")
print(" Hello {},\n Congratulations! \n you have selected for the role of {}", name, Role)
print("Hello {}, Congratulations! \n you have selected for the role of {}".format(name,Role))

#4
string= " I love python Programming "
print(string.strip())
print(string.title().strip())
print(string.count("o"))
if ("Python12345".isalnum()):
    print("Python12345 is alphanumeric")
else:
    print("Python12345 is not alphanumeric")

#remove extra spaces from ends
#3
s = "python Programming"
first_6 = s[0:6]
print(first_6)
last_6 = s[len(s)-6] # same as s[-6]
print(last_6)
print(s[0:len(s):2]) # same as [::2]
print(s[::-1]) # reverse a string
#2
print("Hello","world")
print("hello"+" "+"world")

#1
FullName = "Chitra Manala"
print(FullName[0])
print(FullName[-1])
print(len(FullName))