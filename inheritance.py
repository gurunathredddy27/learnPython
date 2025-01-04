
#SINGLE INHERITANCE
# class Parent:
#     def fun(self):
#         print("this is parent class")
# class Child(Parent):
#     def fun2(self):
#         print("this is child class")
#
# obj= Child()
# obj.fun2()
# obj.fun

#MULTILEVEL INHERITANCE

# class Parent:
#     def fun1(self):
#         print("this is parent class")
# class Child(Parent):
#     def fun2(self):
#         print("this is child class")
# class Grandchild(Child):
#     def fun3(self):
#         print("this is grandchild class")
#
# obj= Grandchild()
# obj.fun2()
# obj.fun1()
# obj.fun3()

#HIRARCHEAL INHERITANCE

# class Parent:
#     def fun1(self):
#         print("this is parent class")
# class Child1(Parent):
#     def fun2(self):
#         print("this is child one")
# class Child2(Parent):
#     def fun3(self):
#         print("this is child two")
#
# obj = Child1()
# obj.fun1()
# obj.fun2()
# obj = Child2()
# obj.fun1()
# obj.fun3()


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("name iss "+ self.firstname+ " "+self.lastname)
class Student(Person):
    def __init__(self,fname, lname):
        Person.__init__(self, fname, lname)
        self.graduation = 2020
    def printname1(self):
        print("this is child(student) class")



obj = Student("ram", "krishna")
obj.printname1()
print(obj.graduation)







