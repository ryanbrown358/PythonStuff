#example of a dictionary
# dictionary = {key1 : value1, key2 : value2}

#empty dictionary 
#empty_dictionary = {}

#Dictionary 1
new_employee = {"name": "Ryan", "age": 24, "position": "Mentor"}
print(new_employee)

#an address
my_address = {"City": "buckeye", "State": "Arizona", "zip": 85326}
print(my_address)

dictionary = {}
dictionary["name"] = "Ryan"
print(dictionary)

#dict function
new_dict = dict(name="ryan", age=19, hometown="phoenix")
print(new_dict)

#try it out
my_house = {"single": "Single story house", "4 bedroom": "With two baths"}
print(my_house)

my_computer = dict(name="asus", age=1, color="red", secondaryColor="blue")
print(my_computer)

#read
my_person = {"name": "Andrew", "age": 28, "city": "Phoenix", "State": "Az"}
print(my_person["name"])
#here you can print a specific item in the dictionary 

#dict.keys() - isolates keys
#dict.values() - isolates values 
#dict.items() - Returns items in a list format of 
#dict.get() - this method returns a value for the given key, if the key is not available then returns a default value of non

student = {"name": "Andrew", "program": "Software Development", "id": 1, "grad_date": "09/18/2017"}
print(student.keys())

#values of the keys 
print(student.values())

#items prints the whole key and values 
print(student.items())

#get method = dict.get(key, default=None)
contact = {"name": "Andrew", "occupation": "Software Developer"}
print("Name : " + contact.get("name"))
print("Occupation : " + contact.get("occupation"))

#Update 
#you can update a key anytime without having to use a function 
address = {"state": "Az", "city": "Buckeye"}
address["street"] = "W Nancy Lane"
address["state"] = "Arizona"
print(address)

my_dictionary = {"name": "Ryan", "age": 24, "city": "Buckeye"}
my_dictionary["name"] = "Ryan Brown"
print(my_dictionary)

#Establish a dictionary 
contact2 = {
    "first_name": "Ryan",
    "last_name": "Brown",
    "phone_number": "480-809-1979",
    "street": "W Nancy Lane",
    "city": "Buckeye",
    "state": "Arizona", 
    "zip_code": "85326"
}
# this removed the phone number from the contact
#del contact2["phone_number"]
del contact2
print(contact2)
#you can also used del to remove an entire dictionary 
