'''
Created on Feb 11, 2018

@author: ryanb
'''




"""
A class can be discribed as a blueprint.  it isnt something in itself; it discribes how to mkae something

Class provide a way to bundle data and functionality together.  When you creae a new class you crear a new type of obkect
this allows a new instance of that type to be made,  you can model almost anything using a class
"""

"""

class ClassName: #starts with the class keyword followed ny the classname then a colon 
class names by convention are capitalized 

docstring the docstring that five the documentation for a class or function 

class_functionality this is where the call functionality is defined 


"""


"""
THE __INIT__() METHOD

when a function is part of a class it is considered a method.  everything you haveb learned about functions also applies to 
methods the only difference is now instead of it being called a function it is called a method...  the __init__() method is a
special method python will run automatically whenever you create a new instance based on the parent class.  Notice that this method
has two leading __ and two trailing __ this prevents python defaul method names from confliting with you method names

"""

"""
SELF 

When you define the __init__() method it is requiered to contain the self parameter in the method definition
Note that self must come first before any other marameters are listed.  It must be included in the definition 
because when python calls this __init__() method later to create a new isntance of the parent call, the method call will 

"""


class Dog:
    '''
    This class models a dog using name and age with the ability to stay or sit
    '''
    def __init__(self, name, age):
        """initalize the attributes that discribes a dog"""
        self.name = name
        self.age = age

    def stay(self):
        """simulates a dog that will stay on command"""
        print(self.name.title() + " Was told to stay")
    
    def sit(self):
        """ simulates a dog sitting on command"""
        print(self.name.title() + " Is sitting")
        

"""
in the example aboue, the class dog has been created.  This class doesnt represent a certain dog: it represent any dog
All dogs have a name and an age.  We also know 

"""


""" 
Making an instance from a class
"""
the_dog = Dog("Ellie", 5)
print("My dog's name is " + the_dog.name.title() + ".")
print("My dog is " + str(the_dog.age) + " years old")

"""
TIP!
you can vreate as mnay instance of a class as you need, as long as you give each instance a unique variable name or it 
occupies a unique spot in a list or dictionary 

"""



"""
Calling MEthods 

once the instance from the dog class has been created, you can use dot notation to call any method defined in the dog class

"""
the_dog.stay()
the_dog.sit()















