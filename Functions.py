
class Student:
    school = "dav"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3
    def get_m1(self):
        return self.m1

    @classmethod
    def getschool(cls):
        return cls.school

s1 = Student(20,19,18)
s2 = Student(20,29,28)

print(s1.avg())
print(s2.avg())
print(s2.get_m1())
print(Student.getschool())



# def function(x):
#     return 5 * x
#
# print(function(3))
#


# def my_function(fname):
#     print(fname + " refsnes ")
#
# my_function("emil")
# my_function("tobias")
# my_function("linus")





# a = int(input("give number"))
# b = int(input("give 2nd number"))
# c = int(input("give 3rd number"))
#
# def add2num(a,b,c):
#     print(a+b+c)
# add2num(a,b,c)