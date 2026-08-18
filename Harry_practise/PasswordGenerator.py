from random import random

letters = ['a','b','c','d','e','f']
Numbers = ['1','2','3','4','5','6','7','8','9']
Symbols = ['!','@','#','$','%','^','&','*']
n_Letters = int(input("Enter number of letters: "))
n_Numbers = int(input("Enter number of numbers: "))
n_Symbols = int(input("Enter number of symbols: "))
Password = ""
for i in range(1,n_Letters+1):
    Password += random.choice(letters)
for i in range(1,n_Numbers+1):
    Password += random.choice(Numbers)
for i in range(1,n_Symbols+1choice):
    Password += random.(Symbols)

print(Password)
