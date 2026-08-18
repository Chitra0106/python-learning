Size = input("Please enter the size of the pizza: S,M,L")
Pepporoni = input("Do you want the pepperoni? Y/N")
Extra_Cheese =  input("Do you want the extra cheese? Y/N")
Bill = 0
if Size =="S":
    Bill += 10
elif Size =="M":
    Bill += 20
elif Size =="L":
    Bill += 50

if Pepporoni == "Y":
    Bill += 10
if Extra_Cheese == "Y":
    Bill += 20

print(Bill)