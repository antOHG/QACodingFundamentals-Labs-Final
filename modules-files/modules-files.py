

# Modules - such as random/ randint/math etc
# modules are python files that we can use to extend functionality of our scripts
# we can import existing modules or make our own
# Many modules are built in and do not require any setup
# Some need to be installed, with pip

# import math # importing the whole module

number = 10
answer = math.sqrt(number) # syntax for referencing an object from a module LOWERModuleName.MethodName

print(answer)

# import multiple modules

import math
import random

def random_pi():
    return math.ceil(random.randint(1,10) * math.pi) # pi * random number 

for i in range(5):
    print(random_pi())


# Just with the required objects from a module (Saves memory increasing performance of code)

# from math import pi, ceil, floor
# from random import randint

# def random_pi():
#     return floor(randint(1,10) * pi) # 

# for i in range(1,10):
#     print(random_pi())
    
    
# pypi.org can be used to find Python packages with the Python Package Index
# non-standard modules can be installed using PIP package manager.
# PIP - linux - sudo apt install python3-pip

# Exercise: create 2 files, called dice.py - write a function that will generate a random number between 1 and 6. 

# # In the second file use the dice module to simulate throwing 2 dice and print its value.

# Files
# read, write and edit files
# python can work with most file types, although may require import/install of other modules.
# Focus on .txt file type

# eg:

# file = open("filename.txt", "mode") # modes can be r (read-only), w (write) \

# r+ (read and write), a (append)

# file.close() # must close the file when finished with. This will only close most recently opened file

# to Read:
# open file, then we use readline() - read a line and moves on to the nextx line.
# readlines() - read all lines
# read() - read all the lines
# seek() - useful to make sure we're reading from the beginning of the file.
# seek(0) - places us at the start

# eg:

# file = open("example.txt", "r")

# print(file.readline()) # printing the first line and move on to the next line
# file.readline() # reads and moves on
# print(file.readline()) # prints line 3 and moves to next line
# file.seek(0) # returns to line 0/1
# print(file.readline()) # prints line 1

# file.close() # prints 1st, 3rd, 1st

# file = open("lines.txt", "r")

# lines = file.readlines() # reads all the lines and stores in a variable

# print(lines)
# file.close() # \n signifies new line in file

# Writing files

# file = open(" lines1.txt","w")

# for n in range(1,11):
#     newline = "this is line" + " " + str(n) + "\n"
#     file.write(newline)

# file.close()

# file = open("lines1.txt", "r")

# outfile = ""

# for line in range(1,11):
#     if line % 2 == 0: # takes even numbers
#         outfile += file.readline()
#     else:
#         file.readline() # skip over the odd numbers

# file = open("lines1.txt", "w")
# file.write(outfile) # Rewrites file with just even lines
# file.close()

# Exercise - open a new text file called teams.txt in write, add the names of 5 sports teams.
# read and display the names of the 1st and 4th team in the file. .strip()
# edit the file so that the top line is replaced with "this is a new line"
# print out the edited file, line by line, Index and .strip()

# open in read mode. take all lines and put in variable and update first line to "this is a new line" 

file = open("teams.txt","w")

sports_teams = ["Man united", "Man City","Liverpool", "Newcastle", "Sunderland"]

for i in sports_teams:
    newline = i + "\n"
    file.write(newline)
    
file.close()

file = open("teams.txt","r")
print(file.readline(1))

file.close()

print(newline(0).strip())
print(newline(3).strip())

file = open("teams.txt","w")

for i in range(len(newline)):
    if i == len(newline) -1:
        file.write(newline(i))
    else:
        file.write(newline(i).strip() + "\n")
        
file.close()       
        
file = open("teams.txt","r")
        
for newline in file:
    print(newline.strip())
file.close()


# with open("filename.txt, "w") as file: