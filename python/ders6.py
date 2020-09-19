
# class Footballer:
#     #attributes
#     name = "Messi"
#     club = "Barça"


# f1 = Footballer()
# print(f1.name)
# print(f1.club)
#
# f1.club = "A team"
# print(f1.club)
# print(f1)
# print(type(f1))

# class Square(object):
#     # edge = 5
#
#     def area(self):
#         return self.edge * self.edge
#
#     def __init__(self, edge):
#         self.edge = edge
#
# s1 = Square(5)
# s2 = Square(7)
# s3 = Square(10)
#
# print(s1.edge)
# print(s1.area())
# print(s2.edge)
# print(s2.area())
# print(s3.edge)
# print(s3.area())


# class Animal:
#     def __init__(self, a, b, c, d):
#         self.name = a
#         self.age = b
#         self.birthday = c
#         self.species = d
#
#
# k1 = Animal("Kangoroo", 3, "19/09/2017", "familya")
# k2 = Animal("Dog", 1, "19/09/2019", "memeli")
# k3 = Animal("Cow", 1, "19/09/2019", "memeli")
#
# print(k1.name)
# print(k1.age)
# print(k2.name)

# class Calc:
#     def __init__(self,a,b):
#         self.num1 = a
#         self.num2 = b
#
#     def add(self):
#         return self.num1 + self.num2
#
#     def subs(self):
#         return self.num1 - self.num2
#
#     def mult(self):
#         return self.num1 * self.num2
#
#     def div(self):
#         return self.num1 / self.num2
#
# while True:
#     try:
#         a = int(input("Enter first number"))
#         b = int(input("Enter second number"))
#     except ValueError:
#         print("Wrong variable")
#         continue
#     selection = input("Enter + - * / for calc if you want to exit press enter")
#     calcObject = Calc(a, b)
#     if selection == "+":
#         print(calcObject.add())
#     if selection == "-":
#         print(calcObject.subs())
#     if selection == "*":
#         print(calcObject.mult())
#     if selection == "/":
#         print(calcObject.div())
#     if selection == "":
#         break

# class BankAccount:
#     def __init__(self, name, money, address):
#         self.name = name #global
#         self.__money = money #private
#         self.address = address
#
#     def getMoney(self):
#         return self.__money
#
#     def setMoney(self, amount):
#         self.__money = amount

# b1 = BankAccount("Messi", 1000, "address")
# b2 = BankAccount("Neymar", 500, "address")
#
# print(b1.__money)
# print(b2.money)
# print("-------")
# b2.money = b1.money + b2.money
# b1.money = 0
#
# print(b1.money)
# print(b2.money)

# print(b1.getMoney())
# print(b2.getMoney())
# b2.setMoney(1500)
# print(b2.getMoney())
#


# class Animal:
#     def __init__(self):
#         print("Animal object created")
#
#     def toString(self):
#         print("Animal")
#
#     def walk(self):
#         print("Animal walk")
#
# class Monkey(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Monkey created")
#
#     def toString(self):
#         print("Monkey")
#
#     def climb(self):
#         print("Monkey climbing")
#
# class Bird(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Bird create")
#     def fly(self):
#         print("Bird can fly")
#
#
# m1 = Monkey()
# b1 = Bird()
# m1.walk()
# m1.climb()
# m1.toString()
#
#
# b1.walk()
# b1.fly()


# class Website:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def login(self):
#         print(self.name, self.surname)
#
#
# class WebsiteWithLoginId(Website):
#
#     def __init__(self,name,surname, id):
#         # super(WebsiteWithLoginId, self).__init__(name, surname,)
#         Website.__init__(self, name, surname)
#         self.id = id
#
#     def loginId(self):
#         print(self.name, " ", self.surname, " ", self.id)
#
#
# class WebsiteWithLoginemail(Website):
#     def __init__(self,name, surname, email):
#         Website.__init__(self, name, surname)
#         self.email = email
#
#     def loginEmail(self):
#         print(self.name, " ", self.surname, " ", self.email)
#
#
# w1 = Website("Berk", "Açıkel")
# w2 = WebsiteWithLoginId("Berk", "Açıkel","444")
# w3 = WebsiteWithLoginemail("Berk", "Açıkel","@email")
# w1.login()
# w2.loginId()
# w3.loginEmail()


"""
getter ve setter da kullanın

Vehicle parent objesi oluşturun:
id,
model,
color,
year,
price

calculatepricewithTax
    1.18


Bus:
top kaç kişi alıyor

Motorbike:
kaç cc
su soğutmalımı yoksa hava soğutmalı mı
calculatepricewithTax 1.32


Car:
sunrof
calculatepricewithTax 1.64


"""





