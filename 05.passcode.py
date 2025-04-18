import random
letters= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbol= ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}"]
print("Welcome to random passcode genarator!")
l=int(input("how many letters code do you need?"))
n=int(input("how many numbers code do you need?"))
s=int(input("how many symbols code do you need?"))
m=int(input("how many random passcode do you need?"))
for i in range(1,m+1):
    initial = []
    for char in range(0, l):
        initial.append(random.choice(letters))
    for num in range(0, n):
        initial.append(random.choice(numbers))
    for sym in range(0, s):
        initial.append(random.choice(symbol))
    random.shuffle(initial)
    pas = ""
    for each in initial:
        pas = pas + each
    print(str(i)+".", pas)
