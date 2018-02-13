'''
Created on Feb 11, 2018

@author: ryanb
'''
from gevent.libev.corecext import stat
class Stadium: 
    """ Create a class that returns the name of a stadium, city and state where it is located and the capacity of it"""
    def __init__(self, name, city_state, capacity):
        self.name = name
        self.city_state = city_state
        self.capacity = capacity
        self.update = 0
    
    def discribe(self):
        """Get the stadium and return it"""
        new_stadium = self.name + " Is located in " + self.city_state + " and has a capacity of " + str(self.capacity)
        return new_stadium.title()
    
    def sports_played(self, sports):
        """ display what main sport is played at this stadium"""
        self.sports = sports
        sport_played = "The following sport is mainly played at this stadium: " + self.sports
        return sport_played.title()
    
    def seats_available(self, seats):
        """Update the seats for the stadium"""
        self.update = seats
      
    def seat_updates(self, updated_seats):
        if updated_seats <= self.update:
            self.update = updated_seats
        else:
            print("Seats can not be more than what is available")
    
    
    
stadium1 = Stadium("jobbing.com", "Phoenix, Arizona", 100000)
print(stadium1.discribe())
print(stadium1.sports_played("football"))


""" Update the seats in the stadium"""



