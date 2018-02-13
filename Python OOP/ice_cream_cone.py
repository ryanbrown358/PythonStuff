import ice_cream as i
# from ice_cream import scoop_icecream # importing a specific function this way
# this way you can give the function an alias/nickname to use witout changing the function
from ice_cream import scoop_icecream as scoop

i.scoop_icecream("small", "sprinkles", "Chocolate", "Cherries")
i.scoop_icecream("large", "peanuts")

scoop("Large", "Pink", "Green", "Blue")
