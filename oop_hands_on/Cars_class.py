'''
Created on Feb 11, 2018

@author: ryanb
'''

class Car: 
    """ modeling a car"""
    
    def __init__(self, make, model, year):
        """initalize attributes to discribe a var"""
        self.make = make
        self.model = model
        self.year = year
        
        self.odometer = 0

    def get_car(self):
        """Return a formatted car"""
        car_name = str(self.year) + " " + self.make + " " + self.model
        return car_name.title()
    
    """Now that we have a method to discribe a car, we can add the next method which helps read the odometer"""
    def read_odometer(self):
        """Shows the cars odometer"""
        print("This car has, " + str(self.odometer), " miles on it.")
    
    def update_odomete(self, miles):
        """update the odometer with new mileage, Rejected changes if roll back is attempted"""
        if miles >= self.odometer:
            self.odometer = miles
        else:
            print("Error: Rolling back odometer not allowed")
     
    def increment_odometer(self, mileage):
        """add a certain number of miles to the odometer"""
        self.odometer += mileage
   



new_car = Car("Ford", "Flex", "2010")
print(new_car.get_car())
new_car.update_odomete(40)
new_car.read_odometer()
print("\n")
"""updated mileage on car"""
new_car.increment_odometer(200)
new_car.read_odometer()