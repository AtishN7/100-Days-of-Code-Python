"""
Oop coffee machine
This project demonstrates the use of classes and objects to represent coffee machine mechanisms.
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee = CoffeeMaker()
coffee_profit = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"What would you like? {coffee_menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        coffee_profit.report()
    else:
        drink = coffee_menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if coffee_profit.make_payment(drink.cost):
                coffee.make_coffee(drink)
