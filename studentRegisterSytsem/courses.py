class Course:
    def __init__(self,courseCode, courseName, courseStartDate, courseEndDate, facultyCode):
        self.courseCode = courseCode
        self.courseName = courseName
        self.courseStartDate = courseStartDate
        self.courseEndDate = courseEndDate
        self.facultyCode = facultyCode
        print(self.courseCode, courseName)