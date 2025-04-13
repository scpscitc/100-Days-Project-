print("Welcome to tip calculator!")
bill= float(input("what was total bill? $"))
tip= float(input("what % you wanna give tip? 10, 12, 15? "))
split= int(input("how many person to split the bill? "))
per_person=(bill+ (bill*tip)/100)/split
print(f"Per person bill is ${round(per_person, 2)}")