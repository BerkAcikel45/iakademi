# number = [1, 2, 3, 4, 5]
# letters = ["a", "b", "c", "d"]
#
# sum = letters + number
# number = number * 2
# print(sum)
# print(number)

numbers = [1,2,3,4,5,6,7,8,9,10]
squares = []

# for number in numbers:
#     squares.append(number**2)
# print(squares)
#
# squares2 = [number**2 for number in numbers]
# print(squares2)

# numbers = [number for number in range(2, 1001, 2) if number % 3 == 0]
# print(numbers)
#
# number2 = []
# for number in range(2, 1001, 2):
#     if number % 3 == 0:
#         numbers.append(number2)
# print(numbers)


# names = ["Orçun", "Jale","Berk", "osman", "Onur"]
# startWihtO = []

# for name in names:
#     if name.startswith("O") or name.startswith("o") :
#         startWihtO.append(name)

# startWihtO = [name for name in names if name.upper().startswith("O")]
# print(startWihtO)

# list = [20,30,40]
# list2 = [2,3,4,5]
# newList = []
# unique = []
#
# for x in list:
#     for y in list2:
#         newList.append(x*y)
# print(newList)
#
# newlist2 = [x*y for x in list for y in list2 if x*y <= 100]
# print(newlist2)


""""
Kullanıcand en 5 farklı isim girmesini ve eğer isim daha önce kullanıcı tarafında
girldiyse hata vermesini girilmemiş ise listeye eklnemesini istiyoruz
"""
# index = 0
# names = []
# while True:
#     name = input("Enter name")
#     if name == "" and index > 5:
#         break
#     if name in names:
#         print(name, "already exist")
#     else:
#         names.append(name)
#         index += 1
# print(names)
#

"""
Verilen bir cümlenin kaç farklı kelimeden oluştuğunu sayın ve bu liste  printleyin
"""
#
# string = "This is a python exersice python python python"
#
# uniq = list()
# string = string.split(" ")
# for word in string:
#     if word not in uniq:
#         uniq.append(word)
#
# print(len(uniq), "tane kelime bulunuyor")
# print(uniq)


# print(tuple)
# print(type(tuple))
# tuple2 = (1,)
# print(tuple2)
# print(type(tuple2))
#
#
# import sys
# import timeit
#
# evenNumbers = [number for number in range(2, 1000001, 2)]
# evenTuple = tuple(evenNumbers)
#
# print("List size", sys.getsizeof(evenNumbers))
# print("Tuple size", sys.getsizeof(evenTuple))
#
# print("List time test", timeit.timeit(stmt="number = [1,2,3,4,5]"))
# print("Tuple time test", timeit.timeit(stmt="number = (1,2,3,4,5)"))


# tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# del tuple1
# print(tuple1)


"""
Programın kullanıcının girdiği cümlede bulunan yasaklı kelimelirin yerine
nokta işareti koyarak terminale bastırın yasaklı kelimelere örnek aq amk 
"""

# bannedWords = ["aq", "amk"]
# while True:
#     string = ""
#     userInput = input("Bir cümle giriniz.")
#     words = userInput.split(" ")
#     if userInput == "":
#         break
#
#     for word in words:
#         if word in bannedWords:
#             string += " . "
#         else:
#             string += " " + word
#
#     print(string)

# dict1 = {}
# print(type(dict1))
#
# customers = {
#             "name": "Berk Açıkel",
#             "email": "berkacikel@gmail.com",
#             "phoneNumber": "5432031474",
# }
# print(customers)
# customers1 = dict(name="Berk Açıkel", email="berkacikel@gmail.com", phoneNumber="5432031474")
#
# print(customers1)
# print(customers1["email"])
#
# customers1["tc"] = "54546465465464"
# print(customers1)

# dictin = \
# {
#     0:{
#         "name": "Berk Açıkel",
#         "email": "berkacikel@gmail.com",
#         "phoneNumber": "5432031474",
#     },
#     1:{
#         "name": "AAA ççç",
#         "email": "aaa@gmail.com",
#         "phoneNumber": "5432031474",
#     }
# }
#
# dictin[0]["tc"] = "3413413431"
# print(dictin)

dictList = {"Numbers":
                {
                    "number": 1, "numbers2": 2, "numbers3": 3
                },
            "Cities": {
                        "city1": "Izmir", "city2": "İstanbul", "city3": "Ankara"
                      }
            }

print(dictList["Cities"]["city1"])
print(dictList.get("Cities", 0).get("city1"))





