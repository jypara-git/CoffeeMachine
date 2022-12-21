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


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {resources['money']}$")


def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def calculate_coins(quarters, dimes, nickels, pennies):
    total = quarters * 0.25
    total += dimes * 0.10
    total += nickels * 0.05
    total += pennies * 0.01
    return total


def check_money(drink, amount, profit):
    cost = MENU[drink]["cost"]
    if amount >= cost:
        change = round(amount - cost, 2)
        print(f"Here is ${change} in change.")
        profit += cost
        resources["money"] += profit
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")


def main():
    on = True
    profit = 0
    while on:
        answer = input("What would you like? (espresso/latte/cappuccino):")
        if answer == "report":
            print_report()
        elif answer == "off":
            on = False
        elif answer == "espresso" or answer == "latte" or answer == "cappuccino":
            drink = MENU[answer]
            if check_resources(drink["ingredients"]):
                print("Please insert coins.")
                quarters = int(input("how many quarters?"))
                dimes = int(input("how many dimes?"))
                nickels = int(input("how many nickels?"))
                pennies = int(input("how many pennies?"))
                amount = calculate_coins(quarters, dimes, nickels, pennies)
                if check_money(answer, amount, profit):
                    make_coffee(answer, MENU[answer]["ingredients"])

main()