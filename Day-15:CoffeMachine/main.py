"""This program demonstrates understanding of functions and basic Python loops such as while.
The data structure dictionary is also create code for Coffe MAchine project as stated in Coffee+Machine+Program+Requirements.pdf"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# print(MENU["espresso"]["cost"])
#
# for item in MENU:
#     for contents in MENU[item]:
#             print(f"{item} : {contents} : {MENU[item][contents]}")

def report():
    for ingredient in resources:
        if ingredient in ["water", "milk"]:
            print(f"{ingredient.title()}: {resources[ingredient]} ml")
        elif ingredient in ["coffee"]:
            print(f"{ingredient.title()}: {resources[ingredient]} gm")
        else:
            print(f"{ingredient.title()}: {resources[ingredient]} $")

def check_resources(drink,ldict):
    menu_resources = MENU[drink]["ingredients"]
    for item in menu_resources:
        if resources[item] < menu_resources[item]:
            ldict[item] = menu_resources[item] - resources[item]
    if len(ldict) == 0:
        return True
    else:
        return False

def payment_check(price):
    print("Please insert coins.")
    q = int(input("How many quarters ? "))
    d = int(input("How many dimes ? "))
    n = int(input("How many nickles ? "))
    c = int(input("How many pennies ? "))
    payment = round((0.25 * q) + (0.10 * d) + (0.05 * n) + (0.01 * c),2)
    if payment > price:
        resources["money"] += price
        print(f"Refunding {round(payment - price,2)} in change")
        return True
    elif payment < price:
        print(f"Sorry, more money required! Refunding {payment} $")
        return False
    else:
        return True

def brew_item(drink):
    menu_resources = MENU[drink]["ingredients"]
    for item in menu_resources:
        resources[item] -= menu_resources[item]

def coffee_machine():
    resources["money"] = 0
    is_machine_on = True
    menu_items = []
    for item in MENU:
        menu_items.append(item)
    while is_machine_on:
        inp = input(f"Pick your favorite poison, buddy!! [{" | ".join(menu_items)}]: ")
        less_items = {}
        if inp in MENU.keys():
            if check_resources(drink=inp,ldict=less_items):
                if payment_check(price=MENU[inp]["cost"]):
                    brew_item(drink=inp)
                    print(f"Here is your {inp.title()} ☕! enjoy")
            else:
                print(f"Sorry!! More {", ".join(less_items.keys())} is required for this item.")
        elif inp == "report":
            report()
        elif inp == "stop":
            is_machine_on = False
        else:
            print(f"So you want a {inp} huh!! Look at the menu dumbass!!")

coffee_machine()