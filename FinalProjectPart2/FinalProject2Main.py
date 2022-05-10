# Huy Nguyen
# PSID 1346435
import csv
from datetime import datetime


class StudentRoster:
    def __init__(self, studentlist):
        self.studentlist = studentlist

    def majors(self):
        students = self.studentlist
        majors = []
        for i in students:
            major = students[i]['major']
            if major not in majors:
                majors.append(major)
        majors = [i.lower() for i in majors]
        return majors

    def studentSearch(self, imajor, minGPA, maxGPA):
        students = self.studentlist
        todays_date = datetime.now().date()
        for i in students:
            studentID = i
            major = students[i]['major']
            lastname = students[i]['lastname']
            firstname = students[i]['firstname']
            gpa = students[i]['gpa']
            grad = students[i]["graduation"]
            discipline = students[i]["discipline"]
            graddate = datetime.strptime(grad, '%m/%d/%Y').date()
            if (major.casefold() == imajor.casefold()) & (float(gpa) <= maxGPA) & (float(gpa) >= minGPA) & (graddate > todays_date) & (discipline != 'Y'):
                return "{}, {} {}, {} GPA\n".format(studentID,firstname,lastname,float(gpa))


    def failedStudentSearch(self, imajor):
        students = self.studentlist
        todays_date = datetime.now().date()
        for i in students:
            studentID = i
            major = students[i]['major']
            lastname = students[i]['lastname']
            firstname = students[i]['firstname']
            gpa = students[i]['gpa']
            grad = students[i]["graduation"]
            discipline = students[i]["discipline"]
            graddate = datetime.strptime(grad, '%m/%d/%Y').date()
            if (major.casefold() == imajor.casefold()) & (graddate > todays_date) & (discipline != 'Y'):
                return "{}, {} {}, {} GPA\n".format(studentID,firstname,lastname,gpa)

    def getStudent(self, major, gpa):
        student_data = self.studentSearch(major, gpa - 0.1, gpa + 0.1)
        extra_students = self.studentSearch(major, gpa - 0.25, gpa + 0.25)
        if student_data == None:
            if extra_students == None:
                print(major + " students: ")
                print(self.failedStudentSearch(major))
        else:
            print("Your student(s): ")
            print(student_data)

        if extra_students != None:
            print("You may, also, consider: ")
            print(extra_students)

    def query(self):
        EXIT = False
        while not EXIT:
            print("Please enter Major and GPA or Press 'q' to exit")
            qinput = input()
            if qinput.lower() == "q":
                EXIT = True
                print("Exiting the program")
                continue
            else:
                major_input = " ".join(qinput.split(" ")[:-1])
                try:
                    gpa_input = float(qinput.split(" ")[-1])
                except:
                    print("Invalid Input")
                    continue
                numMajors = 0
                if major_input.lower() in self.majors():
                    numMajors += 1

                if numMajors != 1:
                    print(self.majors())
                    print("No such student")
                else:
                    self.getStudent(major_input, gpa_input)


if __name__ == "__main__":
    students = {}
    filelist = ["StudentsMajorsList.csv", "GPAList.csv", "GraduationDatesList.csv"]
    for i in filelist:
        with open(i, "r") as file:
            filereader = csv.reader(file, delimiter=',')
            for j in filereader:
                studentID = j[0]
                if i == filelist[0]:
                    students[studentID] = {}
                    lastname = j[1]
                    firstname = j[2]
                    major = j[3]
                    discipline = j[4]
                    students[studentID]['lastname'] = lastname
                    students[studentID]['firstname'] = firstname
                    students[studentID]['major'] = major.strip()
                    students[studentID]['discipline'] = discipline
                elif i == filelist[1]:
                    gpa = j[1]
                    students[studentID]['gpa'] = gpa
                elif i == filelist[2]:
                    grad = j[1]
                    students[studentID]['graduation'] = grad

    roster = StudentRoster(students)
    roster.query()



