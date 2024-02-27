drink = [{"name": "espresso", "price": 1.5, "water": 50, "milk": 0, "coffee": 18},
         {"name": "latte", "price": 2.5, "water": 200, "milk": 150, "coffee": 24},
         {"name": "capuccino", "price": 3.0, "water": 250, "milk": 100, "coffee": 24}]


def coins(choice):
    print("Please insert coins")
    quarter = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nickel = int(input("How many nickels? "))
    penny = int(input("How many pennies? "))
    total_coins = 0.25 * quarter + 0.1 * dime + 0.05 * nickel + 0.01 * penny
    difference = round(total_coins - drink[choice - 1]["price"],2)
    if difference >= 0.0:
        print(f"Here is your ${difference} in change.")
        print(f"Here is your {drink[choice - 1]["name"]} ☕. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
    return drink[choice - 1]["price"]


def ingredients(water_start, milk_start, coffee_start, choice):
    ingredients_enough = True
    water_end = water_start - drink[choice - 1]["water"]
    if water_end < 0:
        print("Sorry, there is not enough water.")
        water_end = water_start
        ingredients_enough = False
    milk_end = milk_start - drink[choice - 1]["milk"]
    if milk_end < 0:
        print("Sorry, there is not enough milk.")
        milk_end = milk_start
        ingredients_enough = False
    coffee_end = coffee_start - drink[choice - 1]["coffee"]
    if coffee_end < 0:
        print("Sorry, there is not enough coffee.")
        coffee_end = coffee_start
        ingredients_enough = False
    return water_end, milk_end, coffee_end, ingredients_enough


def coffee_machine():
    user_choice = ""
    water = 300
    milk = 200
    coffee = 100
    money = 0
    while not user_choice == "off":
        user_choice = input("What would you like? 1- espresso, 2- latte, 3- capuccino: ")
        if user_choice == "report":
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}gr\nMoney: ${money}")
        elif user_choice == "1" or user_choice == "2" or user_choice == "3":
            water, milk, coffee, resources = ingredients(water, milk, coffee, int(user_choice))
            if resources:
                money += coins(int(user_choice))
    return


coffee_machine()
