marks=['95','98','99']
print(marks)
print(marks[0],marks[1],marks[2])
print(marks[-1],marks[-2],marks[-3])
print(marks[1:2])
for score in marks:
    print(score)

marks.append(96)
marks.insert(0,77)
print(marks)
print(95 in marks)
print(len(marks))
marks2=[34,22,33]
marks.extend(marks2)
print(marks)
marks3=[]
for x in marks:
    if '99' in x:
        marks3.append(x)
print(marks3)