#Use it When you need to change items (add, remove, update).
Marks = [10,11,32,25,28, "Absent"]
print (Marks)


Marks.append(18)#insert
Marks.insert(2,"Lost")#Insert into(Index)
Marks[4]="lost"#Update
print(Marks)

Marks.remove(32)
print(Marks)
Marks.pop()
print(Marks)
Marks.pop(3)
print(Marks)

Food = list(("Beans","Maize","peanut"))
print(Food)
food = list("Beans")
print(food)