# classes
"""
classes - a user defined prototype for an object that defines a set of
attributes that characterize an object of class.

the attributes are data memebers and methods accessed via dot(.) notation
"""

"""
Class Vairable: A variable that is shared by all instances of a class
Class variables are defined within a vlass but outside any of the classes
methods.

Class variables are not used frequently as instance variables

"""

"""
Instance Variable:
            A variable that is defined inside a method and belongs only
            to the current instance of a class

"""

"""
Data Member : A class variable or instance variable that hold data associated
with a class and its objects

"""
"""
Inheritance :
    the transfer of the characteristics of a class to another
    class that is derived from it
"""

"""
Instance: An individual object of a certain class
"""

"""
Instantiation: the creation of an instance of a class
"""

"""
Method: A special kind of function that is defined in a class definition
"""

"""
Object: a unique instance of a data structure that is defined by its class
an object that comprises both data members, such as class variable and instance
variables, and methods.
"""

"""
To call a function from an imported module

enter the name of the module you imported followed by the name of the function 
seperated by a dot(.)

this code produces the same output as if it was being used in the module itself

EXample 

module_name.function_name()

"""


"""
IMPORTING SPECIFIC FUNCTION

when importing functions from modules you can also import specific functions from a module take a look 

EXAMPLE 

from module_name import function_name

"""


"""
USING as

what if you wanted to import a function but it may conflic with another function that already exist, or the fucntion name is long
ehrn importing a function you can give the function an alias or a unique nickname.  to do this you will use the keyword (as)
this assigns the imported funtion a new name or alias. 

"""

"""
You can also port all functions using this 

from module_name import *
"""

# Class examples


class Animal:

    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def communicate(self):
        return "Meow! Hiss!"


class Dog(Animal):
    def communicate(self):
        return "Woof! woof!"


animals = [Dog("Zoro",), Cat("Me. Bigglesworth"), Dog("Hazel")]
for animal in animals:
    print(animal.name + ": " + animal.communicate())
