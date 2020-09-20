
class Register:
    stuList = 0

    def __init__(self):
        self.stuList = {}

    def createStudent(self):
        stu = Student()
        stu.stId = input("Enter id")
        stu.name = input("Enter name")
        stu.email = input("Enter email")
        stu.password = input("Enter password")
        stu.address = input("Enter address")
        stu.contactNumber = input("Enter contact number")
        self.studentRegister(stu)

    def studentRegister(self, student):
        self.stuList[student.getStdID()] = student