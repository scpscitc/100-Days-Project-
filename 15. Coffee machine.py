water = 300
milk = 150
coffee = 50
money = 0
def pay():
    w = int(input("How many quarters? : "))
    x = int(input("How many  dimes? : "))
    y = int(input("How many  nickles? : "))
    z = int(input("How many  pennies? : "))
    p = (w * 0.25) + (x * 0.10) + (y * 0.05) + (z * 0.01)
    return p
while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        print("Turned off!")
        exit()
    elif order == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}ml")
        print(f"Money: {money}$")
    elif order == "espresso":
        if water > 50 and coffee > 18:
            payment = pay()
            if payment >= 1.5:
                back = payment - 1.5
                money = money + (payment-back)
                water = water - 50
                coffee = coffee - 18
                print(f"You had gave {round(payment, 2)}$ and Here is your return {round(back, 2)}$")
                print(f"Enjoy your {order.title()}!")
            else:
                print(f"Sorry thats not enough money. {round(payment, 2)}$ refunded")
        else:
            print("Sorry! There is not enough material")
    elif order == "latte":
        if water > 200 and coffee > 24 and milk > 150:
            payment = pay()
            if payment >= 2.5:
                back = payment - 2.5
                money = money + (payment-back)
                water = water - 200
                coffee = coffee - 24
                milk = milk - 150
                print(f"You had gave {round(payment, 2)}$ and Here is your return {round(back, 2)}$")
                print(f"Enjoy your {order.title()}!")
            else:
                print(f"Sorry thats not enough money. {round(payment, 2)}$ refunded")
        else:
            print("Sorry! There is not enough material")
    elif order == "cappuccino":
        if water > 250 and coffee > 24 and milk > 100:
            payment = pay()
            if payment >= 3.0:
                back = payment - 3.0
                money = money + (payment-back)
                water = water - 250
                coffee = coffee - 24
                milk = milk - 100
                print(f"You had gave {round(payment, 2)}$ and Here is your return {round(back, 2)}$")
                print(f"Enjoy your {order.title()}!")
            else:
                print(f"Sorry thats not enough money. {round(payment, 2)}$ refunded")
        else:
            print("Sorry! There is not enough material")
    else:
        print("Inappropriate Order!")






