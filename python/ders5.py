# try:
#     number = int(input("Enter a number"))
# except ValueError:
#     print("Bir Hata oluştu")

# try:
#     age = int(input("Yaşınızı giriniz"))
#     print(age + "yaşındasınız")
# except ValueError:
#     print("Yanlış yaş değeri girdiniz")
# except TypeError:
#     print("Bir hata oluştu")


# while True:
#     try:
#         age = int(input("Yaşınızı giriniz"))
#     except ValueError:
#         print("Yanlış Değer girdiniz")
#     else:
#         print(age, "yaşındasınız")
#         print("Döngü çalıştı")
#         break

#
# try:
#     number = int(input("Enter a number"))
#     if number > 0:
#         result = number / 0
#     elif number < 0:
#         raise ValueError("Number must be greater than zero")
# except ValueError as valueEr:
#     print(valueEr)
# except ZeroDivisionError as zde:
#     print(f'Error: {zde}')
# finally:
#     print("This line always wiil be executed")
#
def sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def subs(numbers):
    result = 0
    for number in numbers:
        result -= number
    return result

def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def division(numbers):
    result = 1
    for number in numbers:
        result /= number
    return result

def getNumbers():
    numbers = list()
    while True:
        try:
            number = int(input("Enter number"))
        except ValueError:
            break
        numbers.append(number)
    print(numbers)
    return numbers

def selectOperation(numbers):
    print(numbers)
    operation = input("Please select an operation: \n"+
                      " + for addition\n" +
                      " - for substraction\n" +
                      " * for multiplication\n"+
                      " / for division\n"
                      )
    if operation == "+":
        print(f'Sum: {sum(numbers)}')
    if operation == "-":
        print(f'Sum: {subs(numbers)}')
    if operation == "*":
        print(f'Sum: {multiply(numbers)}')
    if operation == "/":
        print(f'Sum: {division(numbers)}')

while True:
    selectOperation(getNumbers())
    select = input("To continue select Y-N")
    if select == "Y":
        continue
    else:
        print("Bye Bye..")
        break

