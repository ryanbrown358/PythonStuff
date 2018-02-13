# Modules
def scoop_icecream(size, *toppings):
    """Give a summary of the icecream cone we are making."""
    print("\nMaking a " + size + " ice cream cone with the following toppings")
    for topping in toppings:
        print("- " + topping)


def second_scoop(size, *color):
    """what kind of color and size do they want"""
    print("\n You wanted a " + size + color + " Cone")

