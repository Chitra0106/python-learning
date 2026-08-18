name = "Harry" # strings are immutable
#name[0] = "R" #does not support
s = "Hello world"
a=len(s)
print(a)
print(s.upper())
print(s.islower())
print(s.split())
print(s.split(" ")) # converts to a list
print(s.capitalize())
print(s.title())
print(s.count("o"))
print(s.find("o"))
print(s.replace("o", " "))
print(s.replace("o", " ", 1))
print(" /nHello world".lstrip()) #kind of trim
print("Hello world/n ".rstrip())
print(s.join(" People"))
print("_".join(["Apple","Banana","Mango"]))
print("Python1234".isalpha()) # is Alphabets? =  T/F = false
print("Python1234".isdigit()) # is digits? =  T/F =  Flase
print("Python1234".isalnum()) # is Alphabets+digits? =  T/F = true
print("Python1234".isspace()) # is Spaces? =  T/F  = False



