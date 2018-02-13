# into to python functions

# A function is a block of reusable code that is used to execute a single, related action.
# functions make you code more easy to write and read


def greeting():
    """This function prints a greeting"""
    print("Hello")


greeting()


# def - the def keyword is used to define a function and must alwyas
# go at the beginning

def my_function(a, b):
    print(a + b)


my_function(1, 2)


def day_of_time(greeting, time):
    print(greeting + ", it's " + time + ".")


day_of_time("Good Morning", "8:30 AM")

# add numbers


def pet(name, pet_type='dog'):
    print("I have a " + pet_type + " " + "named, " + name)


pet("Zorro")


def add_numbers(a, b=10):
    print(a + b)


add_numbers(15)

# VarArgs use a * infront of your variable


def ice_cream(*toppings):
    """Print the list of toppings that have been requested1"""
    print(toppings)


ice_cream("Sprinkles", "Cherries", "Candy Corn", "Chocolate sauce")


# return statments
def number(a, b):
    if a > b:
        return a
    elif a == b:
        return "These two numbers are equal"
    else:
        return b


print(number(2, 5))


def user_name(first_name, last_name):
    """Return the properly formatted full name"""
    full_name = first_name + " " + last_name

    return full_name.title()


"""invoke the new function"""
#new_user = user_name("Ryan", "Brown")
# print(new_user)


def new_user(first_name, last_name, age):
    """create a dictionary usign the user's first and last name"""
    user = {"first": first_name, "last": last_name, "age": age}
    return user


user_dict = new_user("Ryan", "Brown", 24)
print(user_dict)

# lambda functions
# example syntax : number = lambda x,y : x + y


def number(x, y): return x + y


number(4, 5)
print(number)


def a(x): return x > 10


print(a(20))


#  map() function
numbers = [1, 2, 3, 4, 5]
# assign the map function a new variable.  this is where the new object will be stored
squar_list = map(lambda x: x * x, numbers)
print(list(squar_list))

# define a function that takes in a number and squars it


def squar_numbers(x):
    """This function returns a number squard"""
    return x * x


# create a tuple of numbers
numbers1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# assign the map function to a variable
# the map function will loop over the tuple of numbers and run the given function squar_numbers over each number
result = map(squar_numbers, numbers1)

# Convert the new map object into a list and stor it in a new variable
numbers_squard = list(result)
print(numbers_squard)

list_a = [6, 7, 8]
list_b = [2, 3, 4]
result2 = map(lambda n1, n2: n1 + n2, list_a, list_b)
print(list(result2))


""""""""""""""""""""""""""""""""""""""""filter method bellow """""""""""""""""""""""""""""""""

# filter method ()
# the filter method filters the given iterable eith the help of a function that test each element in the iterable to be true or not
# the syntaxt for fileter is similar to the map() function
# the filter() method take in two parameters, the function and the iterable
# FUNCTION ----- THIS FUNCTION TEST IF ELEMENTS OF AN ITERABLE RETURN TRUE OR FALSE IF NONE THE FUNCTION DEFAULTS TO IDENTITY
# FUNCTION WHICH RETURNS FALSE IF ANY ELEMENTS ARE FALSE

# ITERABLE ------ wich is to be filtered could be sets list, tuples or containers of any iterators

# filter exampple
# create a list of numbers 1 - 10
number2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# assign the new filter object to a variable
# using the filter method () fin the numbers that return a modulo of 0 when divided by 2
even_numbers = filter(lambda x: x % 2 == 0, number2)
# print the new object once the object is converted to a list
print(list(even_numbers))


number_test = [20, 30, 40, 50, 60, 80, 90, 100]
number_testing = filter(lambda x: x % 4 == 0, number_test)
print(list(number_testing))

ass_dict = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
dict_ass = filter(lambda x: x % 5 == 0, ass_dict)
print(list(dict_ass))

ass_dic = [3, 1, 4, 5, 3, 6, 7, 8, 9, 22, 45, 67, 87, 11]
dction_ass = filter(lambda x: x % 9 == 0, ass_dic)
print(list(dction_ass))
