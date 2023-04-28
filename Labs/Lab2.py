
# Lab 2 - Part 1
# Created by AM on 21/04/2023

age=float(input("Enter your age: "))


if age >= 18:
    print("You are in category A")
elif age >=16:
    print("You are in category B")
else: 
    print("You are in category C")
    

# Part 2 - Calculaor


# Calculator.py created by AM on 21/04/2023

def calculator():
    while True:
        # Print options for the user
        print("Enter '+' to add two numbers together")
        print("Enter '-' to subtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")
        print("Enter 's' to find the squared number")
        print("Enter 'quit' to end the program")
        
        # Get user input
        user_input = input(": ")

        # Check if the user wants to quit
        if user_input == "quit":
            break
        # Check if the user input is a valid operator
        elif user_input in ["+", "-", "*", "/","s"]:
            
            # Get first number
            num1 = float(input("Enter a number: "))
            # Get second number
            num2 = float(input("Enter second number: "))

            # Calculate user_input
            if user_input == "+":
                result = num1 + num2
                print(num1, "+", num2, "=", result)

            elif user_input == "-":
                result = num1 - num2
                print(num1, "-", num2, "=", result)

            elif user_input == "*":
                result = num1 * num2
                print(num1, "*", num2, "=", result)

            elif user_input == "/":
                result = num1 / num2
                print(num1, "/", num2, "=", result)
                
            elif user_input == "s":
                result = num1 **2, num2 **2
                print(num1, "s", num2, "=", result)
        else:
            # Else show invalid input
            print("Invalid Input")

# Call the calculator function to start the program
calculator()

# Task 2 - # ExamGrade.py ask for an input from a user for a grade/mark
# Error checks between 1-100


grade = int(input("Please enter the grade: "))

if grade >= 71 and grade <= 100:
    print("Distinction")
elif grade >= 61 and grade <= 70:
    print("Merit")
elif grade >= 50 and grade <= 60:
    print("Pass")
elif grade >= 1 and grade < 50:
    print("Fail")
else:
    print("Error: marks must be between 1 and 100")
    
# Task 3 - ExamGrade2.py - ask for level and grade and base result on different values
# Error checks between 1-100

level = int(input("Please enter the students level: "))
grade = int(input("Please enter the students grade: "))


if(level==1):    
    if grade >= 71 and grade <= 100:
        print("Distinction")
    elif grade >= 61 and grade <= 70:
        print("Merit")
    elif grade >= 50 and grade <= 60:
        print("Pass")
    elif grade >= 1 and grade < 50:
        print("Fail")
    else:
        print("Error: marks must be between 1 and 100")
    
if(level==2):    
    if grade >= 66 and grade <= 100:
        print("Distinction")
    elif grade >= 51 and grade <= 65:
        print("Merit")
    elif grade >= 40 and grade <= 50:
        print("Pass")
    elif grade >= 1 and grade < 40:
        print("Fail")
    else:
        print("Error: marks must be between 1 and 100") 
        
        
# Task 4  - calculate the length of sides of triangle using Pythagoras Theorem

from math import sqrt

def PythagorasCalculator():
    while True:
        # Print options for the user
        print("Enter '1' to find the length of A given B and C")
        print("Enter '2' to find the length of B given A and C")
        print("Enter '3' to find the length of C given A and B")
        print("Enter 'quit' to end the program")

        # Get user input
        user_input = input(": ")

        # Check if the user wants to quit
        if user_input == "quit":
            break
        # Check if the user input is a valid operator
        elif user_input in ["1", "2", "3"]:

        # Get first number
            num1 = float(input("Enter a number: "))
        # Get second number
            num2 = float(input("Enter second number: "))
        
            if user_input == '1':
                side_a = int(input('Input the length of side a: '))
                side_b = int(input('Input the length of side b: '))
                side_c = sqrt(side_a * side_a + side_b * side_b)
                print('The length of side c is: ' )
                print(side_c)
            
            elif user_input == '2':
                side_b = int(input('Input the length of side b: '))
                side_c = int(input('Input the length of side c: '))
                side_a = sqrt((side_c * side_c) - (side_b * side_b))
                print('The length of side a is' )
                print(side_a)
                
            elif user_input == '3':
                side_a = int(input('Input the length of side a: '))
                side_b = int(input('Input the length of side c: '))
                side_c = sqrt(side_c * side_c - side_a * side_a)
                print('The length of side b is')
                print(side_c)
                
            else:
                print('Please select a side between a, b, c')
                
# Call the calculator function to start the program
PythagorasCalculator()