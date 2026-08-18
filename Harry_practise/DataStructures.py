#Lists
marks = [90,80,70,60,95,87] #numbered list
print(marks)
mixedlist = ["chitra",35,65.5, False]
print(mixedlist[1])
print(mixedlist[0:3])
#List Methods
print(mixedlist.append("Hyd"))
print(mixedlist)
print(mixedlist.remove("Hyd"))
print(mixedlist)
marks.sort()
print(marks)
print(mixedlist.count)
print(mixedlist.index)
(mixedlist.extend(marks))
print(mixedlist)
mixedlist.pop()
print(mixedlist)
mixedlist.insert(0,"Hyd")
