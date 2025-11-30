#  Write a Python program to create a class and access its properties using an object.

class myCclass:
    a=2


c1=myCclass()
print(c1.a)


# Write Python programs to demonstrate different types of inheritance (single, multiple,
# multilevel, etc.).

# Single Inheritance
class car:
    def model(self):
        print("Car model")

class bmw(car):
    def no(self):
        print("BMW M5 CS")

c=bmw()
c.model()
c.no()  


# Multiple Inheritance
class car1:
    def model(self):
        print("Car name")

class bmw:
    def no(self):
        print("Bmw M8 CS")

class Child(car1, bmw):
    def color(self):
        print("Red Metalic")


c = Child()
c.model()
c.no()
c.color()

# Multilevel Inheritance
class Grandfather:
    def property(self):
        print("Grandfather: Land & House")

class Father(Grandfather):
    def business(self):
        print("Father: Family Business")

class Son(Father):
    def career(self):
        print("Son: Software Engineer")


s = Son()
s.property()
s.business()
s.career()



