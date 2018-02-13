planets = ["Earth", "Mars", "Saturn", "Venus"]
print(planets)

car_makes = ["Ford", "Nissan", "Fiat", "Volvo"]
print(car_makes)

north_american_countries = ["United States", "Canada", "Grenada", "Mexico", "Panama"]
print(north_american_countries)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

secondTry = ["Hello", "how was", "Your day"]
print(secondTry) 

# Nested List
our_world = ["Earth", ["United States", "Canada",
                "Grenada", "Mexico", "Panama"], [1,2,3,4,5]]

print(our_world)

#Tuples 
my_tuple = ("Doctor", "Nurse", "PA")
print(my_tuple)

#indexing
#indexs in python are 0 based meaning red is 0, yellow is 1 and so on 
color = ["red", "yellow", "blue", "green", "purple"]
print(color[2])
print(color[1:3])
print(color[2:4])

#modify the index value

#Changed the index of 1 to Bahamas 
north_american_countries[1] = "Bahamas"
print(north_american_countries)


#list functions 

#len function
#list = [1,2,3,4,5,6,7,8,9,10]
#print(len(list))

another_list = [2, "Hello", 6, "Go night night"]
print(len(another_list))

#rang function
new_numbers = list(range(1,11))
print(new_numbers)

numbers = list(range(10,101))
print(numbers)

#append function
number2 = [1,2,3,4,5,6,7,8,9,10]
number2.append(11)
# you can also append a string to the number list too

number2.append("Hello")
print(number2)

# you can append numbers to an empty list 
number3 = []
number3.append(1)
number3.append(2)
number3.append(3)
number3.append(4)
number3.append(5)
number3.append(6)
print(number3)


#insert function
#the insert function takes in two arguments, the first one
#is the index position you wish to target,
#the second one is what you want to insert into that index location

#EX
numbers4 = [1,2,3,4,5]
numbers4.insert(0,"Did this work?")
print(numbers4)

#Removing an element 
#EX
numbers5 = ["Ryan", "Brown", "Anthony"]
del numbers5[2]
print(numbers5)
numbers5 = ["Ryan", "Brown", "Anthony", "Danget"]
del numbers5[-1]
print(numbers5)


#if you know where you index is you, you can call it in a remove function
names = ["Candace", "Caitlin", "Sydney", "Madison", "Taylor", "Serina"]
names.remove("Taylor")
print(names)

sort_numbers = [2,5,7,6,3,9]
sort_numbers.sort()
print(sort_numbers)
#reverse numbers 
rev_numbers = [1,2,3,4,5,6,7,8,9,10]
rev_numbers.sort(reverse=True)
print(rev_numbers)

number_uneffected = [2,4,3,9,1,10]
print('this is the original set of numbers: ')
print(number_uneffected)

print('this is the set soreted set of numbers: ')
print(sorted(number_uneffected))

print('this is the original set of numbers again: ')
print(number_uneffected)