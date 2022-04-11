#Huy Nguyen
#PSID 1346435
import csv
from datetime import datetime

class StudentRoster:
    def __init__(self, studentlist):
        self.studentlist = studentlist
    def roster(self):
        with open("FullRoster.csv", 'w') as file:
            students = self.studentlist
            keys = sorted(students.keys(), key=lambda x: students[x]['lastname'])
            for i in keys:
                studentID = i
                major = students[i]['major']
                lastname = students[i]['lastname']
                firstname = students[i]['firstname']
                gpa = students[i]['gpa']
                grad = students[i]["graduation"]
                discipline = students[i]["discipline"]
                file.write("{},{},{},{},{},{},{}\n".format(studentID, major, firstname, lastname, gpa, grad, discipline))

    def majors(self):
        students = self.studentlist
        majors = []
        keys = sorted(students.keys())
        for i in students:
            major = students[i]['major']
            if major not in majors:
                majors.append(major)
        for j in majors:
            maj = "".join(j.split())
            filename = maj + 'Students.csv'
            with open(filename, 'w') as file:
                for k in keys:
                    studentID = k
                    major = students[k]['major']
                    lastname = students[k]['lastname']
                    firstname = students[k]['firstname']
                    grad = students[k]['graduation']
                    discipline = students[k]['discipline']
                    if j == major:
                        file.write("{},{},{},{},{}\n".format(studentID,lastname,firstname,grad,discipline))

    def candidates(self):
        students = self.studentlist
        keys = sorted(students.keys(), key=lambda x: students[x]['gpa'], reverse=True)
        with open("ScholarshipCandidates.csv", "w") as file:
            for i in keys:
                studentID = i
                lastname = students[i]['lastname']
                firstname = students[i]['firstname']
                grad = students[i]["graduation"]
                discipline = students[i]["discipline"]
                gpa = students[i]['gpa']
                date = datetime.now().date()
                graddate = datetime.strptime(grad, '%m/%d/%Y').date()
                eligible = graddate > date
                if eligible:
                    if not discipline:
                        file.write("{},{},{},{},{}\n".format(studentID,lastname,firstname,major,gpa))

    def disciplined(self):
        students = self.studentlist
        keys = sorted(students.keys(), key=lambda x: students[x]['graduation'])
        with open("DisciplinedStudents.csv", "w") as file:
            for i in keys:
                studentID = i
                lastname = students[i]['lastname']
                firstname = students[i]['firstname']
                grad = students[i]["graduation"]
                discipline = students[i]["discipline"]
                if discipline:
                    file.write("{},{},{},{}\n".format(studentID,lastname,firstname,grad))


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
    roster.roster()
    roster.majors()
    roster.candidates()
    roster.disciplined()



