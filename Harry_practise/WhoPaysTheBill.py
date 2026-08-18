import  random
from math import frexp

friendsList = ["a","b","c","d","e","f"]
whopay = random.choice(friendsList)
print(whopay)

friend_Index =  random.randint(0, 6)
print( friendsList[friend_Index])

print(friendsList[random.randint(0,len(friendsList))])