# index = 1
# while index <= 5:
#     print(index)
#     index = index + 1
# print("Done")

# for index in range(1, 6):
#     print(index)
# print("Done")

# import random
#
# randomNumber = random.randint(1, 5)
# index = 0
# while index < 3:
#     guess = int(input("Enter your guess"))
#     index += 1
#     if guess == randomNumber:
#         print("You won")
#         break
# else:
#     print("Sorry Failed")

# numbers = [13, 15, 12, 75, 34, 98, 65, 23, 80]
# print(numbers)
# for number in numbers:
#     if number % 2 == 0:
#         print(number, "is even number")
#     else:
#         print(number, "is odd number")

# for outterIndex in range(1, 6):
#     if outterIndex == 2:
#         continue
#     for InnerIndex in range(1, 6):
#         if InnerIndex == 2:
#             continue
#         print(f"{outterIndex*InnerIndex:4}", end="")


# def greetUser(firstName, lastName):
#     print(firstName + " " + lastName + " welcome!")
#
# greetUser(lastName="Açıkel", firstName="Berk")

# def calculateSum(num1:int, num2:int) -> int:
#     sum = num1 + num2
#     return sum
#
# sum = calculateSum(5,6,)
# print(sum)

# def validateEmail(email):
#     if email.count("@") != 1:
#         return False
#     numberOfdots = email.count(".", email.find('@'))
#     if numberOfdots != 1:
#         return False
#     return True
#
# email = input("Enter your Email")
# if validateEmail(email):
#     print("Valid email")
# else:
#     print("Invalid email")

# message = "c"
#
# def greet(name):
#     global message
#     message = "a"
#
# greet("berk")
# print(message)
#
# from random import randint, choice
# chars = "abdcdfelmnqprsozx!-+%123456789"
# password = ""
# for index in range(randint(8, 16)):
#     password += choice(chars)
# print(password)


"""
2020 yılından başlayarak 1900 yılına kadar olan artık yılları listeleyin.
Artık yıllar 4 e tam bölünen ancak 100e tam bölünen yılların artık yıl olabilemesi
için ek olarak 400e tam bölünmesi gerekiyor
2000 yıl bir artık yıldır.
"""
# def artikyil(yil):
#     if yil % 4 == 0:
#         if yil % 100 == 0:
#             if yil % 400 == 0:
#                 return True
#         else:
#             return True
#     else:
#         return False
#
# for year in range(2020,1900,-1):
#     if artikyil(year):
#         print(year, "bir artık yıldır")


# list = list()
# list1 = [1, 2, 5, 4, 6]
#
# print(len(list1))
# print(list1[4])
# list1.append(8)
# print(list1[4])
# print(list1)

#
# for index in list1:
#     print(index)

#
# list = [5,78,42,64,3,456]
# print(list[0:4])
# print(list[:4])
# print(list[3:])
# print(list[::-1])

list = [54,44,21,64,12]
# max = 0
# min = 0
# for item in list:
#     if item > max:
#         max = item
#     if item < max:
#         min = item
# print(max)
# print(min)

def max(list):
    max = 0
    for item in list:
        if item > max:
            max = item
    return max

def min(list):
    min = list[0]
    for item in list:
        if item < min:
            min = item
    return min

print(max(list))
print(min(list))