def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def devide(n1,n2):
    return n1/n2
Dictonary = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": devide,
}
def calculator():
    over = False
    n1 = float(input("Enter the first num"))
    while over != True:
        opp = input("+ \n-\n*\n/\n")
        n2 = float(input("Enter the 2nd Number"))
        ans = Dictonary[opp](n1, n2)
        print(f"{n1} {opp} {n2} = {Dictonary[opp](n1, n2)}")
        choice = input(f"Type 'c' to continue calculation with {ans} or type 'n' to to start a new calculation or to end type 'e'" )
        if choice == "c":
            n1 = ans
        elif choice == "n":
            over = True
            print("\n"*20)
            calculator()
        else:
            over = True

calculator()