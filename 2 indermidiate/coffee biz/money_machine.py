
class MoneyMachine:
    CURRENCY = "$"

    #Values of different coins.
    COIN_VALUES = {
        
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        """Initializes money machine attributes."""
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        total = 0
        for coin, value in self.COIN_VALUES.items():
            total += int(input(f"How many {coin}?: ")) * value
        self.money_received = total
        return total

    def make_payment(self, cost):
        """Returns True when payment is accepted, False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            self.money_received = 0
            return False
