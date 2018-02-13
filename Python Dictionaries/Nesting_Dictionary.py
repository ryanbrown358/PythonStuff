# Nesting Dictionaries 
contact_0 = {"name": "Ryan", "phone": "480-809-1979"}
contact_1 = {"name": "Candace", "phone": "602-348-5568"}
contact_2 = {"name": "Catlin", "phone": "602-425-8349"}

#now that we have started three dictionaries we need to create another variable to store these dictionaries in 
address_book = [contact_0, contact_1, contact_2]
#from here we can loop through the single variable to print out all the contacts in the address book
for contact in address_book:
    print(contact)

#as the loop above is executed, this will print the contacts in the addess book on a new line



#empty list for a car lot
car_lot = []

# Make 10 new cars
for car_number in range(10):
    # Establish the new_car dictionary
    new_car = {'car': 'Sedan', 'year': 2017, 'color': 'White'}
    # Add new_car to the car_lot list
    car_lot.append(new_car)
# Print car lot
print(car_lot)

for car in car_lot[:5]:
    print(car)
    
#check to see how man cars were created
print("The total number of cars: " + str(len(car_lot)))

# nesting a list with a dictionary 
ice_cream = {
    "cone": "dipped",
    "flavor": "Vanilla",
    "toppings": ["Sprinkles", "Chocolate chip", "Cherries"],
    "scoops": "one"
}
print("You ordered an ice cream cone " + ice_cream["cone"] + ", with " + ice_cream["scoops"] + 
      " scoop of " + ice_cream['flavor'] + ", and these toppings: ")

for topping in ice_cream["toppings"]:
    print(topping.title())
