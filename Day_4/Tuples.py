#Immutable ordered collection of elements
#Use it When data should not change after creation.

student = ("Patrick", 21, "Software Engineering")

print(student)

Food= ('Beans','Peanut','Irish')

print(type(Food))


#Update
food=list(Food)
print(type(food))
food[1]="Matooke"
food=tuple(food)
print(type(food))
print (food)

#Concatination
conc = Food +student
print(conc)