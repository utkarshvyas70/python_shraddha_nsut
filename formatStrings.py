quantity=3
itemno=567
price=49.95
myorder="I want {} pieces of item {} for {} dollars."
myorder2="I want {2} dollars for {0} pieces of items {1}"
print(myorder.format(quantity,itemno,price))
print(myorder2.format(quantity,itemno,price))