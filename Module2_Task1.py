"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.


"""

FisrtNum = float(input("Enter first number: "))
SecondNum = float(input("Enter second number: "))

Addition = FisrtNum + SecondNum
Subtraction = FisrtNum - SecondNum
Multiplication = FisrtNum * SecondNum
Division = FisrtNum / SecondNum
print("Addition = ", Addition)
print("Subtraction = ", Subtraction)
print("Multiplication = ", Multiplication)
print("Division = ", round(Division,2))