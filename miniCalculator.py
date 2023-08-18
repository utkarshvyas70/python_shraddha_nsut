first=input("First number: ")
operator=input("Opertaor (+.-,*,/,%): ")
second=input("Enter number: ")

first=int(first)
second=int(second)
if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="/":
    print(first/second)
elif operator=="%":
    print(first%second)
else:
    print("invalid number")