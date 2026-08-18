Height = int(input("What is your height in cm?"))
if Height >= 150 :
    print("You cna continue")
    Age = int(input("What is your age?"))
    if  Age>10:
        print("You should pay 5$")
        bill = 5
    elif Age<10:
        print("You should pay 10$")
        bill = 10
    else :
        bill = 15
        print("You should pay 15$")


    want_Photo = input("Do you want a photo?Y for Yes and N for No")
    if want_Photo == "Y":
        bill = bill+3
        print("You should dpay extra 3$ the amount is "+str(bill))
else:
    print("You should not")