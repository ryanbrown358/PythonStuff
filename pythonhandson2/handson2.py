#Performing operations in Python

day = "9th,"
month = "October"
year = "1993"

my_birthday = month + " " + day + " " + year

print(my_birthday)


#Stretch Goal 1
first = "happy"
second = "birthday"
third = "to"
fourth = "you"

final = first + " " + second + " " + third + " " + fourth
print(final)

#stretch goal 2
age = 15

if age < 10:
    print("Not Permitted")
elif age < 15:
    print("Permitted with Parent")
elif age < 18:
    print("Permitted with anyone over 18")
else:
    print("Permitted to attend alone")
    