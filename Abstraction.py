
#ABSTRACTION

from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("the mileage of tesla is 30kmph")
class Suzuki(Car):
    def mileage(self):
        print("The mileage of suzuki is 25kmph")
class Renault(Car):
    def mileage(self):
        print("The mileage of renault is 27kmph")

t = Tesla()
t.mileage()