class CoffeeMaker:
    def __init__(self):
        """Initializes the coffee machine with default resources."""
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True if enough resources to make drink, False if not."""
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_coffee(self, order):
        """Deducts resources when coffee is made."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕. Enjoy!")
