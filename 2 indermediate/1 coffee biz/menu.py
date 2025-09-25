class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    def __init__(self):
        """ Initializes the menu with available drinks with the resources they require and cost of making  a drink. """
        self.menu = [
            MenuItem("latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem("espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem("cappuccino", water=250, milk=50, coffee=24, cost=3.0),
        ]

    def get_items(self):
        """Returns all the names of the available drinks."""
        return "/".join([item.name for item in self.menu])

    def find_drink(self, order_name):
        """Searches the menu for a drink by name. Returns that item if it exists."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that item is not available.")
        return None
