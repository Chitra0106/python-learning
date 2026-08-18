#Recursion = "Do the same job again, but with a smaller problem, until there's nothing left to do."'''
'''
0,1,1,2,3,5,8,13,21,34,55,89
understanding Fibonacci sequence
fib(0) = 0
fib(1) = 1
fib(2) = fib(1)+fib(0)
fib(3) = fib(2)+fib(1)
fib(4) = fib(3)+fib(2)
fib(n) = fib(n-1)+fib(n-2)
'''
def fib(n):
    #Base case of recursion
    if(n==0 or n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2) #Recursive Call

print(fib(10))



# Factorial using recursion

def Factorial(n):
    if n==0:  # Base case
        return 1
    else:
        return n*Factorial (n-1) #Recursive Call

print(Factorial(5))