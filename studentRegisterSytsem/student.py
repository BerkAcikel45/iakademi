class Student:

    def __init__(self, Name, Surname, Password, Email, Address, conctactNumber, studentId):
        self.Name = Name
        self.Surname = Surname
        self.Password = Password
        self.Email = Email
        self.Address = Address
        self.conctactNumber = conctactNumber
        self.studentId = studentId
        print(self.Name, self.Surname, self.Password, self.Email, self.Address, self.conctactNumber, self.studentId)