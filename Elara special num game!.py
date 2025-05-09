import random
task = [
    "Fun",             "Lovely",           "Overwhelming",    "Special",
    "Cute",            "Chaotic",          "Heartfelt",       "Cheesy",
    "Goofy",           "Magical",          "Crazy",           "Warm",
    "Romantic",        "Silly",            "Honest",          "Secret",
    "Funny",           "Unexpected",       "Random",          "Peaceful",
    "Childish",        "Flirty",           "Sweet",           "Dreamy",
    "Raw",             "Reassuring",       "Brave",           "Kiddish",
    "Deep",            "Whispered",        "Mushy",           "Hopeful",
    "Witty",           "Cringy-but-cute",  "Comforting",      "Bolod-level",
    "Melting",         "From-her-soul",    "Bold",            "Pure",
    "Stupidly-beautiful", "Only-for-Shan", "Tummy-butterfly", "Jokeful",
    "No-filter",       "Eye-twinkling",    "Randomly-romantic","Little-moment",
    "Innocent",        "Forever-kind",     "Midnight-worthy"
]

num = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print(num)
diff = input("Choose a Difficalty. Type 'easy' or 'hard': ").lower()
if diff == "easy":
    life = 10
elif diff == "hard":
    life = 5
else:
    print("You dont wanna play? cool!....Bye~")
    exit()


def checker(guess, num):
    if guess < num + 5 and guess > num - 5:
        print("My Number can listen Your breath! just go a but right-left and You'll be right here! ")
    elif guess < num + 10 and guess > num - 10:
        print("You are too close")
    elif guess < num + 20 and guess > num - 20:
        print("You are close")
    elif guess < num - 50:
        print("Your guess is too small!!!")
    elif guess > num + 50:
        print("Your guess is too High!!!")
    elif guess > num:
        print("Your guess is high!")
    elif guess < num:
        print("Your guess is low!")


while life != 0:
    print(f"You have {life} attempt remaining to guess the Number!")
    guess = int(input("Guess the number: "))
    if guess == num:
        print("You are right!")
        print("You won!")
        exit()
    else:
        life = life - 1
        checker(guess, num)
        while life == 1:
            chance_1 = input("Do you want any special favour from your bf? Type 'yes' or 'no': ").lower()
            if chance_1 == "yes":
                print(f"Okh fine! Then go and tell Shan something '{random.choice(task)}'")
                chance_2 = input("You wanna do this? Type 'yes' or 'no': ").lower()
                if chance_2 == "yes":
                    chance_3 = input("Ki korso??? Type 'yes' or 'no': ").lower()
                    if chance_3 == "yes":
                        print("Cool! Jao tmk valobeshe aro 3ta attempt dilam! go and try!")
                        life = life + 3
                    else:
                        print("vule gela naki?!....but vulso toh morso! You are gone baby!")
                        life = 0
                else:
                    print("Khub na favour chao??? Ekhn?! Nijer bf k etao bolte paro na! chii! Vago!")
                    life = 0
            else:
                print("Yeh ashse! ja life chilo tao gelo! vagooo!")
                life = 0

print("You Have Lost!")