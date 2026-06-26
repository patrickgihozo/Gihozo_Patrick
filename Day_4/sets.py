#Unique items and membership checks
Cars = {"Suzuki","Honda","Mazida","Subaru","Benz"}
#print (Cars)
#print(type(Cars))

Name ={1,3,"Patrick","Iron","Aissa",3.4,4,3,1,}
print(Name)
Cars.add("Iron")
#print(Cars)

w =Cars.union(Name)
#print (w)
z=Cars.intersection(Name)
#print(z)
Name.remove("Aissa")
Name.update(["Natasha","Leon"])#
print(Name)

