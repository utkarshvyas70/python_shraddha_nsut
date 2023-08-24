year=int(input("Which year do you want to check?"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("It is a laep year.")
        elif year%400!=0:
            print("This is not a leap year.")
    elif year%100!=0:
        print("This is a leap year.")

else:
    print("This is not a leap year.")