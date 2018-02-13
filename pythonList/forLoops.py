#for loops 
countries = ["USA", "Canada", "England", "Ireland"]
for country in countries:
    print(country)

#another Exampple
countries2 = ["usa", "canada", "england", "ireland"]
for country in countries2:
    print(country.title())

#mathmatical loops
numbers = [1,2,3,4,5]
for number in numbers:
    print(number ** 2)

ages = [10,13,15,18]
for age in ages:
    if age < 15:
        print("Sorry, not permitted")
    elif age < 18:
        print("Pleas enjoy with anyone over the age of 18")
    else:
        print("Please enjoy the movie")


#while loops 
number1 = 1
while number1 <= 5:
    print(number1)
    number1 += 1

#break statement 
#this will print everything in the loop untill the letter t is found, 
#then the loop will break (stop)
for letter in "Exeter":
    if letter == "t":
        break
    print("Current letter: " + letter)

print("The loop is over")

number2 = 7
while number2 > 0:
    print("The current value is:", number2)
    number2 -= 1
    if number2 == 4:
        break

print("The loop is over")

#continue statement 
number = 10
while number > 0:
    number = number - 1
    if number == 4:
        continue
    print('Current number value:', number)
print("This loop is over")


