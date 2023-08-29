print("Welcome to the love calculator.")
name1=input("What is your name: \n")
name2=input("What is their name: \n")

combined=name1+name2
lowerCase=combined.lower()

t=lowerCase.count("t")
r=lowerCase.count("r")
u=lowerCase.count("u")
e=lowerCase.count("e")

true=t+r+u+e

l=lowerCase.count("l")
o=lowerCase.count("o")
v=lowerCase.count("v")
e=lowerCase.count("e")

love=l+o+v+e

score=str(true)+str(love)

print(f"Your score is: {score}")