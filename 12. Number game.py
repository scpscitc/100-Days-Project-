import random
num = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print(num)
diff = input("Choose a Difficalty. Type 'easy' or 'hard': ").lower()
if diff == "easy":
    life = 10
    print(f"You have {life} attempt remaining to guess the Number!")
elif diff == "hard":
    life = 5
    print(f"You have {life} attempt remaining to guess the Number!")
else:
    print("You dont wanna play? cool!....Bye~")
    exit()
def checker(guess,num):
    if guess < num + 5 and guess > num - 5:
        print("My Number can listen Your breath! just go a but right-left and You'll be right here! ")
    elif guess < num + 10 and guess > num - 10:
        print("You are too close")
    elif guess < num+20 and guess > num-20:
        print("You are close")
    elif guess < num-50:
        print("Your guess is too small!!!")
    elif guess > num+50:
        print("Your guess is too High!!!")
    elif guess > num:
        print("Your guess is high!")
    elif guess < num:
        print("Your guess is low!")
while life != 0:
    guess = int(input("Guess the number: "))
    if guess == num:
        print("You are right!")
        print("You won!")
        exit()
    else:
        life = life - 1
        checker(guess,num)
        print(f"You have {life} attempt remaining to guess the Number!")

print("You Have Lost!")