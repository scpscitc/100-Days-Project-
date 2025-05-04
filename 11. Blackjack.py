#**************************blackjack***************************
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\l
      |  \/ K|                            _/ |                
      '------'                           |__/           
      """

numbers = [11,2,3,4,5,6,7,8,9,10,10,10]
users_choice = random.sample(numbers,2)
coms_choice = random.sample(numbers,2)
def repeat():
    users_choice.append(random.choice(numbers))
def blacky():
    while sum(coms_choice) < 17:
        coms_choice.append(random.choice(numbers))
    print(f"Your cards: {users_choice},   Current Score: {sum(users_choice)}")
    print(f"Computer's first card: {coms_choice[0]}")
    over = False
    while over != True:
        again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if again == "y":
            repeat()
            if sum(users_choice) > 21:
                if sum(users_choice) > 21 and 11 in users_choice:
                    users_choice.remove(11)
                    users_choice.append(1)
                    print(f"Your cards: {users_choice},   Current Score: {sum(users_choice)}")
                    print(f"Computer's first card: {coms_choice[0]}")
                else:
                    over = True
                    print(f"Your final hand: {users_choice}, final score: {sum(users_choice)}")
                    print(f"Computer's final hand: {coms_choice}, final score: {sum(coms_choice)}")
                    print("You went over. You Lose 😤")
            else:
                print(f"Your cards: {users_choice},   Current Score: {sum(users_choice)}")
                print(f"Computer's first card: {coms_choice[0]}")
                over = False
        else:
            if sum(coms_choice) > 21:
                print(f"Your final hand: {users_choice}, final score: {sum(users_choice)}")
                print(f"Computer's final hand: {coms_choice}, final score: {sum(coms_choice)}")
                print("Opponent went over. You win 😁")
            elif sum(users_choice) > sum(coms_choice):
                print(f"Your final hand: {users_choice}, final score: {sum(users_choice)}")
                print(f"Computer's final hand: {coms_choice}, final score: {sum(coms_choice)}")
                print("You win! 😁")
            elif sum(users_choice) < sum(coms_choice):
                print(f"Your final hand: {users_choice}, final score: {sum(users_choice)}")
                print(f"Computer's final hand: {coms_choice}, final score: {sum(coms_choice)}")
                print("You Lose! 😤")
            elif sum(users_choice) == sum(coms_choice):
                print(f"Your final hand: {users_choice}, final score: {sum(users_choice)}")
                print(f"Computer's final hand: {coms_choice}, final score: {sum(coms_choice)}")
                print("Its a Draw!")
            over = True
print(logo)
Entry = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if Entry == "y":
    blacky()
else:
    exit()

