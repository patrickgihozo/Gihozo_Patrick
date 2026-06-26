# #Inbuilt and Extenal to be accessed using import keyword . They are used to reuse ready made tools, keep it organized, avoid clutter
# #import entire module
# import math
# pi =math.pi
# print(pi)

# #To use external module, you usntall the module first using pip install module_name
# #eg: pandas,numpy,scipy,etc

# #We can also import specific functions 
# from math import pi

# from math import sqrt

# print(sqrt(16))

# #import multiple functions
# from math import sqrt,pow

# # importing module with aliases
# import math as m 
# result =m.sqrt(16)
# print("Square root of 1 : ",result)
import sys

print(sys.builtin_module_names)