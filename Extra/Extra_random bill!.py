#random bill!!!
import random
print("hehe! guess who's going to pay the bill today?")
friends = []
x= input("Write names of you friend(Use coma between them!)").split(",")
friends.extend(x)
print(f"Todays bill goes to {random.choice(friends)}")
