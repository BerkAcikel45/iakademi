# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#
#     def walk(self):
#         pass
#
#     @abstractmethod
#     def run(self):
#         pass
#
#
# class Bird(Animal):
#     def __init__(self):
#         print("Bird class created")
#
#     def run(self):
#         print("Bird run")
#
# a = Bird()
# a.walk()


# class Animal:
#
#     def toString(self):
#         print("Animal")
#
#
# class Monkey(Animal):
#     def __init__(self):
#         print("Monkey Created")
#
#     def toString(self):
#         print("Monkey")
#
#
# a = Animal()
# a.toString()
#
# m1 = Monkey()
# m1.toString()


# class Employee:
#     def raisee(self):
#         raise_rate = 0.1
#         return 100 + 100 * raise_rate
#
#
# class ComputerEnggineer(Employee):
#     def raisee(self):
#         raise_rate = 0.2
#         return 100 + 100 * raise_rate
#
#
# class Manager(Employee):
#     def raisee(self):
#         raise_rate = 0.3
#         return 100 + 100 * raise_rate
#
# e = Employee()
# print(e.raisee())
#
# c = ComputerEnggineer()
# print(c.raisee())
#
# m = Manager()
# print(m.raisee())

from abc import ABC, abstractmethod


# class Shape:
#
#     def area(self):
#         pass
#
#     def perimeter(self):
#         pass
#
#
# class Square(Shape):
#
#     def __init__(self, edge):
#         self.edge = edge
#
#     def area(self):
#         return self.edge**2
#
#     def perimeter(self):
#         return  self.edge*4
#
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14*self.radius**2
#
#     def perimeter(self):
#         return 3.14*self.radius*2
#
#
# s = Square(5)
# print(s.area())
# print(s.perimeter())
#
# c = Circle(10)
# print(c.area())
# print(c.perimeter())
#
#
import register


def menu():
    print("""Please select action from menu:
    1) Create Student #name, password, email, address, conctactNumber, stID
    2) Display Students
    3) AddCourses
    4) DisplayCourses
    5) DropCourses
    6) CreateNewCourse
    7) ModifyCourses
    8) RemoveCourse
    9) SelectCourse
    10) ViewRegisteredCourses
    11) ViewCourseOfferingRoster
    12) Exit
    """)

    selection = input("Select action")
    return selection


selection = menu()
while selection != 12:

    if selection == "1":
        a = register.Register()
        a.createStudent()
        menu()
    if selection == "2":
        pass


