#!/usr/bin/env python3



## addition function
def add(x, y):

    return x + y

## subtraction function 
def sub(x, y ):
    return x - y

## multipication function 
def mul(x, y):
    return x * y

## division function 
def div(x, y):
   if y == 0:
    print("Can't divid by 0")
   else:
    return x / y

## User input

num1 = float(input("Enter first number"))
op = input("Select operation")
num2 = float(input("Enter second number"))



if op == "+":
   print(add(num1, num2))
            

elif op == "-":
   print(sub(num1, num2))

elif op == "*":
    print(mul(num1, num2))

elif op == "/":
    print(div(num1, num2))

else:
    print("Invalid input")
