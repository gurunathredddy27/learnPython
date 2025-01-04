
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfun(self):
        print("hello my name is "+ self.name)

p1= Person("jhon", 22)
p1.age = 20
p1.myfun()
print(p1.age)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfun(self):
#         print("hello my name is "+ self.name)
#
# p1 = Person("jhon", 22)
# p1.myfun()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}{self.age}"
# p1 = Person("jhon", 22)
#
# print(p1)
#




# class Mobile:
#     def __init__(self, brand, ram, price):
#         self.brand = brand
#         self.ram = ram
#         self.price = price
#     def display(self):
#         print("brand ", self.brand)
#         print("ram ", self.ram)
#         print("price ", self.price)
#
# obj = Mobile('aaple', '6', '1000')
# obj.display()




# class Mobile:
#     def __init__(self):
#         print("this is init")
#     def display(self):
#         print("this is method")
# obj= Mobile()   #here init method declares variables and
#                   #automatically execute when object is created
# obj.display()    #we need to create obj and call the menthod to execute



# class Car:
#     wheel = 4
#     def __init__(self):
#         self.mil = 10
#         self.com = "BMW"
#
# c1 = Car()
# c2 = Car()
# Car.wheel = 2
#
# c1.mil = 7
# print(c1.com, c1.mil, c1.wheel)
# print(c2.com, c2.mil, c2.wheel)
#
#



# class Computer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram
#
#     def config(self):
#         print("config is ", self.cpu, self.ram)
#
# com1 = Computer('i5', 16)
# com2 = Computer('ryzen 3', 8)
#
# com1.config()
# com2.config()


# class My_class:
#     x = 5
# print(My_class)
# p1 = My_class()
# print(p1.x)
#






# class Orange:
#     d = 12
#     print("this is classs")
#     def display(self):
#         a = 10
#         b= 12
#         print(a,b)
# obj = Orange()
# obj.display()
# print(obj.d)