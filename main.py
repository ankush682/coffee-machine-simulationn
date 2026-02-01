MENU = {
    "espresso": {
        "ingredients":
            {
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



def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check():
    defi=0
    if want== "espresso":
        if resources["water"] <50:
            print("Sorry there is not enough water.")
            defi+=1
        if resources["coffee"]<18:
            print("Sorry there is not enough coffee in the machine.")
            defi += 1
        if defi == 0:
            return True
    elif want=="latte":
        if resources["water"] <200:
            print("Sorry there is not enough water.")
            defi += 1
        if resources["coffee"]<24:
            print("Sorry there is not enough coffee in the machine.")
            defi += 1
        if resources["milk"]<150:
            print("Sorry there is not enough milk at the moment.")
            defi += 1
        if defi == 0:
            return True
    elif want=="cappuccino":
        if resources["water"] <250:
            print("Sorry there is not enough water.")
            defi += 1
        if resources["coffee"]<24:
            print("Sorry there is not enough coffee in the machine.")
            defi += 1
        if resources["milk"]<100:
            print("Sorry there is not enough milk at the moment.")
            defi += 1
        if defi == 0:
            return True
    elif want=="report":
        report()
    return False

def pay():
    cost=MENU[want]["cost"]
    print(f"Your total for {want} is: ${cost}")
    print("please insert coins")

    quarters = int(input("how many quarters:")) * 0.25
    dimes=int(input("how many dimes?:")) * 0.1
    nickels=int(input("how many nickels?:")) *0.05
    pennies=int(input("how many pennies?:")) * 0.01

    total= quarters + dimes+ nickels+ pennies

    if total >= cost:
        change = round(total - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        print(f"Here is your {want} ☕, please enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def updates():
    cost = MENU[want]["cost"]
    for item in MENU[want]["ingredients"]:
        resources[item] -= MENU[want]["ingredients"][item]
    resources["money"] += MENU[want]["cost"]

resources["money"] = 0


c=True
while c:
    want=input("What would you like? (espresso/latte/cappuccino):").lower()
    if check():
        if pay():
            updates()
    if want=="off":
        print("Thankyou for coming, please come again later!")
        c= False
