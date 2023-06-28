from menu import MENU
import art
# print(art.logo)
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}
def possible_drinks(resources,MENU):
    available_drinks = []
    for drink in MENU:
        ingredients = MENU[drink]["ingredients"]
        can_make = True
        for ingredient in ingredients:
            if ingredient not in resources or resources[ingredient] < ingredients[ingredient]:
                can_make = False
                break
        if can_make:
            available_drinks.append(drink)   
    return available_drinks

def drink_possible(the_input,resources,MENU):
    for key in MENU[the_input]["ingredients"].keys():
        if key in resources and resources[key]>=MENU[the_input]["ingredients"][key]:
                # continue
            return True
        else:
            print(f"{key} is {MENU[the_input]['ingredients'][key] - resources[key]} less than required")
            return False  
total=0
def money_check(the_input,total,menu):
        left=0
        print(f"the total cost of the {the_input} is {menu[the_input]['cost']}")
        print("please insert coins ")
        print("how many quarters   ")
        quarters=int(input())
        print("how many dimes   ")
        dimes=int(input())
        print("how many nickles   ")
        nickles=int(input())
        print("how many pennies   ")
        pennies=int(input())
        total=((quarters*25)+(dimes*10)+(nickles*5)+pennies)/100
        if total>menu[the_input]["cost"]:
            left=total-menu[the_input]["cost"]
            print(f"the amount {left} is refunded")
            return the_input
        elif total==menu[the_input]["cost"]:
            return the_input
        else:
            print("the amount {total} is not enough =======  amount refunded")

while True:
    print("what would you like (espresso/latte/cappuccino):")
    the_input=input().lower()
    if the_input=="report":
        print(resources)
    elif the_input=="espresso" or the_input=="latte" or the_input=="cappuccino":
        if drink_possible(the_input,resources,MENU):
            for key in MENU[the_input]["ingredients"].keys():
                if key in resources:
                    resources[key]=resources[key]-MENU[the_input]["ingredients"][key]
            resources["money"]+=MENU[the_input]["cost"]
            print(f"here is your {money_check(the_input=the_input,total=total,menu=MENU)} ☕ enjoy!")
        else:
            print(f"the {possible_drinks(resources,MENU)} are available with present resources")
    elif the_input=="off" or not the_input:
        break 
    else:
        print("Invalid input. Please try again.")



# ---------------------------------- following tis the code given by GPT -------------------------------------

# from menu import MENU

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# def check_resources(the_input):
#     for key in MENU[the_input]["ingredients"].keys():
#         if key in resources and resources[key] >= MENU[the_input]["ingredients"][key]:
#             continue
#         else:
#             print(f"Not enough {key}.")
#             return False
#     return True

# def process_coins():
#     print("Please insert coins.")
#     quarters = int(input("How many quarters? "))
#     dimes = int(input("How many dimes? "))
#     nickels = int(input("How many nickels? "))
#     pennies = int(input("How many pennies? "))
#     total = (quarters * 25 + dimes * 10 + nickels * 5 + pennies) / 100
#     return total

# def check_payment(the_input, total):
#     if total >= MENU[the_input]["cost"]:
#         left = total - MENU[the_input]["cost"]
#         print(f"Here is your {the_input}. Enjoy! Change: ${left:.2f}")
#         return True
#     else:
#         print("Not enough money. Refunding amount.")
#         return False

# def update_resources(the_input):
#     for key in MENU[the_input]["ingredients"].keys():
#         if key in resources:
#             resources[key] -= MENU[the_input]["ingredients"][key]

# while True:
#     the_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

#     if the_input == "report":
#         print(resources)
#     elif the_input in ["espresso", "latte", "cappuccino"]:
#         if check_resources(the_input):
#             total = process_coins()
#             if check_payment(the_input, total):
#                 update_resources(the_input)
#     elif the_input == "off" or not the_input:
#         break
#     else:
#         print("Invalid input. Please try again.")
