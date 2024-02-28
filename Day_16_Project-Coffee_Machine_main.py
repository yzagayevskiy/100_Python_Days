from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee():
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()

    is_machine_on = True
    while is_machine_on:
        # TODO 2 - Check resources sufficient
        menu = Menu()
        drink = input(f"What would you like? ({menu.get_items()}) ")
        if drink == "off":
            is_machine_on = False
        elif drink == "report":
            # TODO 1 - Print report
            coffee_machine.report()
            money_machine.report()
        elif drink == "latte" or drink == "espresso" or drink == "cappuccino":
            drink_of_choice = menu.find_drink(drink)
            if coffee_machine.is_resource_sufficient(drink_of_choice):
                # TODO 3 - Process coins
                # TODO 4 - Check transaction successful
                if money_machine.make_payment(drink_of_choice.cost):
                    # TODO 5 - Make coffee
                    coffee_machine.make_coffee(drink_of_choice)
        else:
            menu.find_drink(drink)


coffee()
