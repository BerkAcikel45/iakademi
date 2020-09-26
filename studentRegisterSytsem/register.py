from studentRegisterSytsem.courses import Course
from studentRegisterSytsem.student import Student


class Register:
    stuList = 0

    def __init__(self):
        self.stuList = {}
        self.courseList = {}

    def createStudent(self):
        name = input("İsminizi giriniz")
        surname = input("Soyadınızı giriniz")
        password = input("Şifrenizi giriniz")
        email = input("Emailinizi giriniz")
        address = input("Adresinizi giriniz")
        concactNumber = input("Telefonun numaranızı giriniz")
        studentId = input("Öğrenci numaranızı giriniz")
        student = Student(name, surname, password, email, address, concactNumber, studentId)
        self.studentRegister(student)

    def studentRegister(self, student):
        self.stuList[student] = student
        print(self.stuList)

    def display(self):

        for item in self.stuList:
            print(item.Name, item.Surname, item.Password, item.Email, item.Address, item.conctactNumber, item.studentId)

    def createCourse(self):
        courseCode = input("Kurs Kodunu giriniz")
        courseName = input("Kurs İsmini giriniz")
        courseStartDate = input("Kurs başlangıcı giriniz")
        courseEndDate = input("Kurs sonunu giriniz")
        facultyCode = input("Kurs fakulte kodunu giriniz")
        course = Course(courseCode, courseName, courseStartDate, courseEndDate, facultyCode)
        self.courseList[course] = course

    def courseDisplay(self):
        for item in self.courseList:
            print(item.courseCode, item.courseName)

    def get_changedList(self):
        courseCode = input("Kurs Kodunu giriniz")
        courseName = input("Kurs İsmini giriniz")
        courseStartDate = input("Kurs başlangıcı giriniz")
        courseEndDate = input("Kurs sonunu giriniz")
        facultyCode = input("Kurs fakulte kodunu giriniz")
        changedlist= {
            "courseName": courseName,
            "courseStartDate": courseStartDate,
            "courseEndDate": courseEndDate,
            "facultyCode": facultyCode,
        }

        return changedlist

    def modifyCourse(self, courseCode):
        changedList = self.get_changedList()
        for data in self.courseList:
            print(f' eski kurs kodu: {data.courseCode}   eski kurs ismi: {data.courseName} eski kurs başlangıç tarihi: {data.courseStartDate} eski kurs bitiş tarihi: {data.courseEndDate} eski kurs fakulte kodu: {data.facultyCode} ')
            if data.courseCode == courseCode:
                data.courseName = changedList.get("courseName")
                data.courseStartDate = changedList.get("courseStartDate")
                data.courseEndDate = changedList.get("courseEndDate")
                data.facultyCode = changedList.get("facultyCode")
                print(f'Yeni kurs kodu: {data.courseCode}  yeni kurs ismi: {data.courseName} yeni kurs başlangıç tarihi:{data.courseStartDate} yeni kurs bitiş tarihi: {data.courseEndDate} yeni kurs fakulte kodu: {data.facultyCode} ')
                break



