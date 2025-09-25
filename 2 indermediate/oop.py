# # 1. Class (blueprint)
# class Car:
#     # Constructor method to initialize attributes
#     def __init__(self, brand, color):
#         # 3. Attributes (variables tied to the object)
#         self.brand = brand
#         self.color = color

#     # 4. Method (function tied to the object)
#     def drive(self): #self means this object
#         print(f"The {self.color} {self.brand} is driving 🚗")

#     def stop(self):
#         print(f"The {self.brand} has stopped 🛑")


# # 2. Objects (instances of the class)
# car1 = Car("Toyota", "red")
# car2 = Car("BMW", "black")

# # Access attributes
# print(car1.brand)   # Toyota
# print(car2.color)   # black

# # Call methods
# car1.drive()   # The red Toyota is driving 🚗
# car2.stop()    # The BMW has stopped 🛑

#!=====================================================================
# from turtle import Turtle, Screen
# #object = class

# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')

# timmy.forward(100)

# my_screen = Screen()
# my_screen.exitonclick()
#!=====================================================================
from prettytable import PrettyTable

table = PrettyTable()
#class.method(field name(header), [field values])
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) 
table.add_column("Type", ["Electric", "Water", "Fire"])

#class.attribute
table.align = "l" #left align
print(table)