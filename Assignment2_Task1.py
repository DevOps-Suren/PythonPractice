"""
Assignment 2 Task 1 Check if a Number is Even or Odd

Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.

"""

Num = float(input("Enter a number: "))
if Num % 2 == 0:
    print(Num, "is a Even number")
else:
    print(Num,"is a odd number ")