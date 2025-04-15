print("Welcome!")
h=float(input("pelase enter your height in meter unit: "))
w=float(input("please enter your weight: "))
bmi=w/h**2
if bmi < 18.5:
    print(f"your bmi is:{bmi} and you are under weight!")
elif bmi <= 24.9:
    print(f"your bmi is:{bmi} and you are in ideal weight!")
else:
    print(f"your bmi is:{bmi} and you are over weight!")