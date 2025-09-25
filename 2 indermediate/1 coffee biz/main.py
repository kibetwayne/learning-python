from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    # Ask user what they want
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        #Get resources from coffeemaker.py
        coffee_maker.report()
        #get current profit
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            # 1. Check if resources are enough and Process payment
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                # 3. Make coffee
                coffee_maker.make_coffee(drink)