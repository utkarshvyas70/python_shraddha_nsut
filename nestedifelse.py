print("Welcome to the rollercoaster.")
height=int(input("Enter your height in cm: "))
if height>=120:
    print("You can ride.")
    age=int(input("Enter your age: "))
    if age<=18:
        print("You have to pay $12")
    elif age<12:
        print("You have to pay $5")
    else:
        print("Invalid input.")
else:
    print("You can't ride.")