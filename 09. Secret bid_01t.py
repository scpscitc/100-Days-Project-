#**********just define!*********
def bid():
    name = input("Whats ur name?")
    amount = input("whatd your bid?")
    names.append(name)
    amounts.append(amount)
#*******just run and execute!!******
over= False
while over != True:
    names = []
    amounts = []
    bid()
    again = input("any one left? 'yes' or 'no'").lower()
    if again == "yes":
        print("\n"*100)
        over = False
    elif again == "no":
        x = max(amounts)
        y= amounts.index(x)
        winer = names[y]
        print(f"The max amount is {x} and Payer is {winer}")
        over = True

