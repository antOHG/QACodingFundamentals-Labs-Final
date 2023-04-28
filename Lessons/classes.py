# Classes and methods is part of OOP - object orientated programming.
# Key concepts:
# Class - a blueprint of attributes(variables), and methods (functions) - we can use \
# to make objects of a class.
# Object - is an instance of a class. 
# Methods - Functions attached to a class.
# Allows us to easily make multiple objects of the same type.
# if we model a group of students if we didnt use classes we would need \
# to assign unique variables for each student. 

class Dog: # Creates a class called dog.
    energy = "high" # setting an attribute for the class.

    def speak(self): # Create  method called speak (like a function)
        print("bark")

fido = Dog() # sets fido as an object of the class

# Redefine attribute

#fido.energy = "low"

print(fido.energy) # calling the attribute
fido.speak() # Calling the method

### 

class Students:
    pass

student_1 = Students()
student_2 = Students()

print(student_1) # Retunrs it is an object of the class students and its memory location

student_1.first = "john"
student_1.last = "smith"
student_1.age = 10

print(student_1.first, student_1.last)

student_2.first = "katie"
student_2.last = "smith"
student_2.age = 12

print(student_2.age)

# What if we needed to do this for 30 students? 

class Student:
    def __init__(self, first, last, age): # __indicates a background tasks__ 
        self.first = first  # init initialises the object with these attributes.
        self.last = last    # self param refers to the object itself
        self.age = age      # The object itself is passed as the first argument. 
                            # self maps the class data to the object data.

student_3 = Student("john", "smith", 10)
student_4 = Student("Katie", "smith", 12)

print(student_3.age, student_4.age)

class Student1:
    def __init__(self, first, last, age):
        self.first = first  
        self.last = last    
        self.age = age
        self.full = first + " " + last      


student_5 = Student1("john", "smith", 10)
student_6 = Student1("Katie", "smith", 12)

print(student_5.full)

# As a method... 

class Student2:
    def __init__(self, first, last, age):
        self.first = first  
        self.last = last    
        self.age = age

    def fullname(self):
        return(self.first + " " + self.last)


student_7 = Student2("john", "smith", 10)
student_8 = Student2("Katie", "smith", 12)

print(student_7.fullname())
print(Student2.fullname(student_8)) # Same result as line 90


# Change an attribute with a method:

class Student3:
    def __init__(self, first, last, age):
        self.first = first  
        self.last = last    
        self.age = age

    def fullname(self):
        return(self.first + " " + self.last)
    
    def change_age(self):
        self.age = int(self.age + 1)

student_9 = Student3("john", "smith", 10)
student_10 = Student3("Katie", "smith", 12)

print(student_9.age)
student_9.change_age()
print(student_9.age)

# Using a self-class variable

class Student4:

    age_increase_amount = 25 # self class variable

    def __init__(self, first, last, age):
        self.first = first  
        self.last = last    
        self.age = age

    def fullname(self):
        return(self.first + " " + self.last)
    
    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)


student_11 = Student4("john", "smith", 10)
student_12 = Student4("Katie", "smith", 12)


student_11.change_age()
print(student_11.age)

print(student_11.age_increase_amount) # returns the value of the variable from the object
print(Student4.age_increase_amount) #  returns from the class itself.

#__dict__

#print(Student4.__dict__)
print(student_11.__dict__)

# Make a change to the variable

Student4.age_increase_amount = 20
student_12.age_increase_amount = 15

print(Student4.age_increase_amount)
print(student_11.age_increase_amount)
print(student_12.age_increase_amount)

print(student_11.__dict__)
print(student_12.__dict__)

# Non self class variables

class Student5:

    age_increase_amount = 25 # self class variable
    num_of_students = 0

    def __init__(self, first, last, age):
        self.first = first  
        self.last = last    
        self.age = age

        Student5.num_of_students += 1

    def fullname(self):
        return(self.first + " " + self.last)
    
    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)


student_13 = Student5("john", "smith", 10)
student_14 = Student5("Katie", "smith", 12)

print(Student5.num_of_students)

# Parent class

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

# Child class
class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")

my_cat = Cat("whiskers", "feline", "siamese")

my_cat.meow()
my_cat.eat()

print(my_cat)

# __str__

class Animal1:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return f"{self.name} ({self.species})"

# Child class
class Cat1(Animal1):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")

    def __str__(self):
        return f"{self.name} ({self.species}, {self.breed})"

my_cat1 = Cat1("whiskers", "feline", "siamese")

my_cat1.meow()
my_cat1.eat()

print(my_cat1)

# Leading and trailing underscores:
# _money = 100 - single leading underscore signifies the variable is private. 
# type_ print_ class_ -  single trailing inderscore used for python keywords
# double leading underscore - name mangling -avoid collisions if our classs is extended.
# attribute not accessible without referencing our class name. 
# we access them _classname__attributeName. 

class Feline:
    __family = "felidae"

cat2 = Feline()
