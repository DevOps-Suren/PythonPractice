"""
Assignment 3 - Task 2 -  Using the Math Module for Calculations4

Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

"""

import math

def main():

    try :

        num = float(input("Enter a number: "))
        # Validate input for square root & logarith is positive
        if num <= 0:
            print("Error: square root & logarith requires a positive number ")
            return
        # Calculate Sqaure Root
        sqrt = math.sqrt(num)

        # Calculate Sqaure Root
        log = math.log(num)

        # Calculate Sqaure Root
        sine = math.sin(num)

        print(f"\n Results for number :- {num}")
        print(f"Square root  :- {sqrt}")
        print(f"Logarithm (log e)  :- {log}")



        print(f"Sin (in Radians(  :- {sine}")

    except ValueError:
        print("Error: Please enter a valid number")
    except Exception as e:
        print(f"An unexcepted error occured:{e}")

if __name__ == "__main__":
    main()

