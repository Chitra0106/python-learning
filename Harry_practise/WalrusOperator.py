def slow_function():
    print("Hello World")
    print("Hello World")
    print("Hello World")
    return 50
#a= slow_function()
if((a:= slow_function())>5):
    print("Hello ")
else:
    print(" World")
while(data:=input("Enter a number")):
    print(data)
    if data == 5:
        break