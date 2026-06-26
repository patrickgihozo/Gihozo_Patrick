#lambda function is a small function anonymous function defined using keyword lambda , It has one expression.

#syntax
#lambda arguments:expression

square = lambda x: x * x

print(square(4))

is_even = lambda x:x % 2
print(is_even(3))

numbers =[2,3,4,5,6,7]
greater_than_4 = list(filter(lambda x: x>4,[1,3,5,6,8]))
print(greater_than_4)

Fruits = ['Cherry','Banana','Date','Apple','Mango','Dragin fruit']

Fruits = sorted(Fruits, key=lambda x: len(x))

print(Fruits)

#Recursive function: These are functions that call themselves until base.

#Factorial function
#Method 1
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#method 2
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
#Count down example
def countdown(n):
    if n == 0:
        print("Done")
    else:
        print(n)
        countdown(n - 1)

countdown(5)

#Binary search

        