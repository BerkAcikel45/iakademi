from studentRegisterSytsem.register import Register


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

    if selection == "3":
        a.createCourse()
        selection = menu()
    if selection == "4":
        a.courseDisplay()
        selection = menu()

    if selection == "7":
        courseCode = input("Hangi kursu değiştrimek istiyorsanız kodunu giriniz")
        a.modifyCourse(courseCode)
        selection = menu()

    if selection == "8":
        courseCode = input("Hangi kursu silmek istiyorsanız kodunu giriniz")
        a.removeCourse(courseCode)
        selection = menu()