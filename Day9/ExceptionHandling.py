#Code, try ,finally
#try block
#Eg:
#try:
 #   number = int(input('Enter a number'))
  #  result = 100/number
   # print result()
#except ZeroDivisionError:
 #   print('Can not divide by zero')
#
#except ValueError:
#print('Invalid number entered.')



class UnderAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise UnderAgeError("Must be 18 years or older.")

    print("You are eligible to drive.")

except UnderAgeError as e:
    print("Error:", e)