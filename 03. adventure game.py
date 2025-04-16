print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')
print("Welcome to Treasure Island!")
print("You need to go in the right path and find treasure!")
print("You're at a cross road. Where do you want to go?")
r= input("Wanna go Right or left? type'Right' or 'Left'").lower()
if r == "right":
    print("Game Over!")
elif  r == "left":
    print("You've come to a lake! There is an island in the middle of the lake!")
    print("Wanna wait for boat or wanna swim across the lake?")
    w=input("Type 'wait' to Wait or To Swim type'swim' ").lower()
    if w == "swim":
        print("Game Over!")
    elif w == "wait":
        print("You've arrived at the island unharmed! Now you are in front of a house with 3 doors")
        d=input("Tyep'red' for the Red door, 'yellow' for the Yellow door and 'blue' for the Blue door!").lower()
        if d== "yellow":
            print("Congrats! You've found the treasure!")
        elif d=="red":
            print("It's a room of fire! You died! Game Over. ")
        elif d=="blue":
            print("You;ve attracted by a Shark. Game Over")


