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
    "money": 0
}
coffee_machine_on = True


def print_report():
    for resource in resources:
        print(f"{resource} : {resources[resource]}")


def get_recipe(recipe_choice):
    return MENU[recipe_choice]


def check_resources(resource_choice):
    recipe = get_recipe(resource_choice)
    print(recipe)
    enough_resources = True
    ingredients = MENU[resource_choice]["ingredients"]
    for ingredient in ingredients:
        if resources.get(ingredient) < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            enough_resources = False
    return enough_resources


def process_payment():
    quaters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    total = (quaters * 25) + (dimes * 10) + (nickels * 5) + pennies
    return total


while coffee_machine_on:
    choice = input(" What would you like? (espresso/latte/cappuccino): ")
    can_make_choice = False
    if choice == "off":
        coffee_machine_on = False
    elif choice in ["espresso", "latte", "cappuccino"]:
        can_make_choice = check_resources(choice)
    elif choice == "report":
        print_report()
    else:
        print("invalid choice")

    if can_make_choice:
        print("Please insert coins.")
        payment_amount = process_payment() / 100
        cost = MENU[choice]["cost"]
        if payment_amount < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            resources["money"] += cost
            ingredients = MENU[choice]["ingredients"]
            resources["water"] -= ingredients["water"]
            resources["milk"] -= ingredients["milk"]
            resources["coffee"] -= ingredients["coffee"]
            print(f"Here is ${float(payment_amount - cost):.2f} in change.")
            print(f"Here is your {choice} ☕️.Enjoy!")

