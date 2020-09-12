# number = int(input("Enter Number"))
#
# if number == 0:
#     print("Number equal to 0")
#
# if number < 0:
#     print("Number is negative")
#
# if number > 0:
#     print("Number is positive")
#
#
# if number == 0:
#     print("Number equal to 0")
#
# elif number < 0:
#     print("Number is negative")
#
# else:
#     print("Number is positive")
#
#
# if bool(number):
#     print("Number is equal zero")
#
# if number > 5 and number < 8:
#     print("number between 5 and 8")
#
# if 8 > number > 5:
#     print("number between 5 and 8")
#
# if number > 5 or number < 10:
#     print(number)
#
# list1 = []
# list2 = []
# list3 = list1
#
# if list1 == list2:
#     print("True")
# else:
#     print("False")
#
# if list1 is list2:
#     print("True")
# else:
#     print("False")
#
# if list1 is list3:
#     print("True")
# else:
#     print("False")
#
# firstName = "Berk"
# arr = [1, 6, 7]
# for data in arr:
#     print(data * 10)
#
# print(firstName[0])
# print(firstName[3])
#
# for letter in firstName:
#     if letter == "i":
#         print(firstName + " contains i")
#
#
# if "i" in firstName:
#     print(firstName + " contains i")
# else:
#     print(firstName + " not contains i")

# number = 0
# alpahabet = "abcdef"
# print(len(alpahabet))
# for i, qwe in enumerate(alpahabet):
#     print(qwe)
#     print(i)
#
# arr = [0, 2, 4]
# print(len(arr))

# for number in range(1, 10, 2):
#     print(number, end=" ")

number = 0
# while True:
#     number += 1
#     if number % 10 == 0:
#         print(number)
#     if number == 30:
#         break
#
# while number < 30:
#     number += 1
#     if number % 10 == 0:
#         print(number)
#

""""
TC alın bunun dığruluğunu kontrol edin.

11 karakteri geçmicek
0 başlayamaz

tcnin 1,3,5,7 ve 9. hanelerindeki rakamların toplamı 7 ile çarpımından
çıkan sonucu 2,4,6 ve 8. hanelerinin rakamları toplamından çıkartıldığında 
geriye kalanın 10 böldüğümüze kalanı 10. haneyi verir.


"""

#
# tc = input("Enter tc")
# if len(tc) != 11:
#     print("TC Yanlış")
# if tc[0] == 0:
#     print("TC Yanlış")
# index = 1
# evenTotal = 0
# oddTotal = 0
# numberTotal = 0
#
# for number in tc:
#     numberTotal += int(number)
#     if index > 9:
#         break
#     if int(number) % 2 == 0:
#         evenTotal += int(number)
#     else:
#         oddTotal += int(number)
#     if (oddTotal * 7 - evenTotal) % 10 == int(tc[9]):
#         print("TC doğru")
#     index += 1
#

userInput = input("Enter string")
alphabet = "abcdefghlmnkqwerty"
newString = ""
count = 0

for letter in userInput:
    count = userInput.count(letter)

    if letter not in newString:
        newString = newString + str(count) + letter

print(newString)

"Anne, I vote more cars race Rome-to-vienna"

userIn = input("enter")
removedChars = ""
for letter in userIn:
    if letter.isalnum():
        removedChars = removedChars + letter