#looping through dictionaries 

new_user = {
    "name": "Ryan", 
    "email": "ryanbrown358@gmail.com",
    "username": "ryanbrown358"
}

#now that you have a dictionary established we can loop through this like so 
# to loop through the dictionary you will use a for loop 
#using .items() allows you to loop through the key and the value in the dictionary 
for key, value in new_user.items():
    print("\nKey: " + key)
    print("Value: " + value)

#how to loop through a dictionary only grabbing the keys
for key in new_user.keys():
    print(key.title())

#looping throguh the values 
for value in new_user.values():
    print(value)

language_poll = {
    'Andrew': 'Python',
    'Mike': 'JavaScript',
    'David': 'F#',
    'Kevin': 'C#',
    'Frank': 'Java'
}

# Create a list with our friends in it.
friends = ['David', 'Mike']

# Loop through polling results
for name in language_poll.keys():
    print(name.title())
# If any name matches a friends name then print the following
    if name in friends:
        print(" Hi " + name.title() + ", I see your language of choice is " +
              language_poll[name] + ".")


letters = {}
#loop through the word mississippi
for letter in "Mississippi":
    #for each letter in mississippi add that letter to a tuple with the starting value of 0 then add 1 when the letter is found
    letters[letter] = letters.get(letter, 0) + 1
print(letters)
