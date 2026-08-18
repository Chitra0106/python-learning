numbers = [1,2,3,4,5,6,7]
#map - Transform every element Same number of elements
def square(x):
    return x*x
new_numbers = map(square, numbers)
print(list(new_numbers))

new_cube_numbers = map(lambda x: x**3, numbers)
print(list(new_cube_numbers))

#Filter Keep elements matching a condition Fewer or equal elements
def greater_5(x):
    return x>5
greater_numbers = filter(greater_5, numbers)
print(list(greater_numbers))
greaterNumbers = list(filter(lambda x: x>4,numbers))
print(list(greaterNumbers))

#reduce Combine all elements into one value Single value
from functools import reduce
def square_red(x,y):
    return x+y
red_squ_numbers = reduce(square_red, numbers)
print(list(red_squ_numbers))

