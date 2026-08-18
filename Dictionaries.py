marks_dict= dict(chitra=90, Sri=89, ric=98)
marks_dict["Ved"] = 97
print(marks_dict)
marks_dict.pop("Ved")
print(marks_dict)
marks_dict.popitem()
print(marks_dict)
#print(Marks_dict.add("Ved:97"))
print(marks_dict)
print(marks_dict.values())

# Dictionary comprehensions
table_5 = {i:i*5 for i in range(5)}
print(table_5)
Square_dict = {x: x*x for x in range(10)}
print(Square_dict)