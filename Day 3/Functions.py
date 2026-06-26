lenth = int(input("Enter the lenth: "))
width = int(input("Enter the width: "))

def area_of_rectangle(length,width):
    area = length*width
    print(f"The area of rectangle is {area} cm")
    return area

area_of_rectangle(lenth,width)

#What is a parameter? It's variable listed inside the function definition.
def greet(name):
    print(f"Hello {name}")

#Arguments are actual values passed to the function.
def greet(name):
    print(f"Hello {name}")
