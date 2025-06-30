# class abi:
#     x = 5

# a = abi()
# print(a.x)

#inheritance

# class person:
#     def __init__(self, fname,lname):
#         self.fname = fname
#         self.lname = lname

#     def displayname(self):
#         print(self.fname + self.lname)
    
# class son(person):
#         pass

# x = son("Abi","sheck")
# x.displayname()

#polymorphism in python

# class car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print(self.brand)
# class bike:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print(self.brand)

# c1 = car("BMW", "X5")
# b1 = bike("Yamaha", "mt15")

# for x in (c1, b1):
#     x.move()  # This will call the move method of each object
#     # Output: BMW
#     #         Yamaha


#real code of poly lyes in one parent and multi child class

class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(self.brand)
class car(vehicle):
    def move(self):
        print(self.brand)
class bike(vehicle):
    def move(self):
        print(self.brand)
c1 = car("BMW", "X5")
b1 = bike("Yamaha", "mt15")
for x in (c1, b1):
    x.move()  # This will call the move method of each object
    # Output: BMW
    #         Yamaha