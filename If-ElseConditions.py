# IF else Condition
age = int(input("Enter your Age"))
if age>18:
    print("you can vote")
else : print("you can not vote")

if age>25:
     print("You can Drive")
elif age>18:
     print("You can Vote")
elif age>5:
    print("You are too young")
else:
     print("You can not Vote and drive")