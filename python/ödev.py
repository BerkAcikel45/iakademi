class CreateStudent:

    def __init__(self, Name, Surname, Password, Email, Address, conctactNumber, studentId):
          self.Name = Name
          self.Surname = Surname
          self.Password = Password
          self.Email = Email
          self.Address = Address
          self.conctactNumber = conctactNumber
          self.studentId = studentId
          print(self.Name, self.Surname, self.Password, self.Email, self.Address, self.conctactNumber, self.studentId)


class Register:
    stuList = 0


    def __init__(self):
        self.stuList = {}

    def createStudent(self):
        name = input("İsminizi giriniz")
        surname = input("Soyadınızı giriniz")
        password = input("Şifrenizi giriniz")
        email = input("Emailinizi giriniz")
        address = input("Adresinizi giriniz")
        concactNumber = input("Telefonun numaranızı giriniz")
        studentId = input("Öğrenci numaranızı giriniz")
        student = CreateStudent(name, surname, password, email, address, concactNumber, studentId)
        self.studentRegister(student)

    def studentRegister(self, student):
        self.stuList[student] = student
        print(self.stuList)

    def display(self):

        for item in self.stuList:
            print(item.Name, item.Surname, item.Password, item.Email, item.Address, item.conctactNumber, item.studentId)


def menu():
    print("""Please select action from menu:
    1)  Create Student
    2)  Display Students
    3)  AddCourses
    4)  DropCourses
    5)  DisplayCourses
    6)  CreateNewCourse
    7)  ModifyCourse 
    8)  RemoveCourse
    9)  SelectCoursesToTeach
    10) ViewRegisteredCourses
    11) ViewCourseOfferingRoster
    12) Exit""")
    selection = input("Select action: ")


    return selection
selection = menu()
a = Register()

while selection != 12:
    if selection == "1":
        a.createStudent()
        selection = menu()

    if selection == "2":
        a.display()
        selection = menu()