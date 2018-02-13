"""
Pythons library includes a math module that provides a plethora of methods you can use to perform 
mathmatical procedures 

utilizing the math module, you can call the math.floor() and math.ceil() methods to enable a program to preform 
rounding of a floating point vaule specified between their parentheses to the closest integer

math.ceil() - This method rounds up to the nearest integer
math.floor() - This method rounds down to the nearest integer

math.pow() - Takes in two arguments to raise a specified vaule by a specified power 
math.sqrt() - Takes in one argument and returns the squar root of that specified value
"""
"""
to use the math shit, use import math

"""

import math
import random

print("Round the number 8.5 down", math.floor(8.5))

print("Round the number 8.5 up", math.ceil(8.5))

print("5 to the power of 10 = ", math.pow(5, 10))

print("The squar root of 82 is: ", math.sqrt(82))
"""
Python inclueds a random module that be used to produce pseudo-random numbers once imported into a program.  Below
are a few othe methods

random.random() - Produces a single floating-point number between 0 and 1.0
random.sample() - Produces a list of elements selected at random from a sequence.  This method 
requiers two arguments to specify to select from.  And the length of the list to be produced using the rang() function will 
allow you to specify a sequence as the first argument 
"""
numbers = random.sample(
    range(1, 49), 7
)  # the first argument given is the range from one to 49 the second argument is how many numbers you want to be returned from that range
print("Your lucky numbers areL ", numbers)
