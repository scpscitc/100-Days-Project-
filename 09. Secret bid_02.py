logo = """                        ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\ 
                       .-------------.
                      /_______________\ """
list = {}
def bid():
    name = input("name?")
    list[name] = input("whats the amount?")
over = False
print(logo)
while over != True:
    bid()
    again = input("again")
    if again == "yes":
        print("\n"*110)
        over = False
    else:
        z = 0
        for x in list:
            m = int(list[x])
            if m > z:
                z = m
                winner = x
        over = True
print(f"The max amount is {z} and Winner is {x}")

