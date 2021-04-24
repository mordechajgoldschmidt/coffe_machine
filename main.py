from data import MENU, resources


def insert_coins():
    quarters = float(input("How many quarters? ")) * 0.25
    dimes = float(input("How many dimes? ")) * 0.1
    nickles = float(input("How many nickles? ")) * 0.05
    pennies = float(input("How many pennies? ")) * 0.01
    coin_list = [quarters, dimes, nickles, pennies]
    return coin_list


def resources_cost(user_input):
    coffee_data = MENU[user_input]
    ingredients = coffee_data["ingredients"]
    water_cost = ingredients["water"]
    milk_cost = ingredients["milk"]
    coffee_cost = ingredients["coffee"]
    coffee_price = coffee_data["cost"]
    cost_list = [int(water_cost), int(milk_cost), int(coffee_cost), float(coffee_price)]
    return cost_list


def coffee_type(user_input):
    coffee_type = user_input
    return coffee_type


def coffee_machine():

    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]

    machine_on = True
    while machine_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        if user_input == "off":
            print("AUTODESTRUCTION IN 10 SECONDS.")
            machine_on = False
        elif user_input == "report":
            print(f"Water: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}")
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            coffee = coffee_type(user_input)
            cost_list = resources_cost(user_input)
            water_cost = cost_list[0]
            milk_cost = cost_list[1]
            coffee_cost = cost_list[2]
            coffee_price = cost_list[3]
            if water_cost > water_left:
                print("There is not enough water.")
            elif milk_cost > milk_left:
                print("There is not enough milk.")
            elif coffee_cost > coffee_left:
                print("There is not enough coffee.")
            else:
                user_money = sum(insert_coins())
                if user_money >= coffee_price:
                    change = round((user_money - coffee_price), 2)
                    water_left -= water_cost
                    milk_left -= milk_cost
                    coffee_left -= coffee_cost
                    print(f"Report after purchasing {coffee}\nWater: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}")
                    print(f"Here is your coffee and {change}$ change.")
                else:
                    print("You don't have enough money.")
        else:
            print("ENGLISH MOTHERFUCKER! DO YOU SPEAK IT!?")


coffee_machine()
