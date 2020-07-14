#####################################
# curse_c.py
# classes for CURSE project
#####################################
# database set up
import sqlite3
db = sqlite3.connect("assignment7.db")
cursor = db.cursor()


# User base class
class User:
    # user attributes
    firstName = ""
    lastName = ""
    ID = 0

    # constructor
    def __init__(self, f, l, i):
        self.firstName = f
        self.lastName = l
        self.ID = i

    # printing method using __str__
    def __str__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

    def __repr__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))


# Student:
class Student(User):
    # student attributes
    gradYear = 0
    major = ""
    email = ""
    schedule = []
    instructors = []

    # constructor
    def __init__(self, f, l, i, g, m, e):
        User.__init__(self, f, l, i)
        self.gradYear = g
        self.major = m
        self.email = e
        self.schedule = []
        self.instructors = []


    # printing method using __str__ and __repr__
    def __str__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

    def __repr__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

    def get_ID(self):
        return self.ID

    def add_course(self, crn):
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%s'""" % (crn))
        query_result = cursor.fetchall()
        for i in query_result:
            self.schedule.append(i)
        return

    def remove_course(self, crn):
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%s'""" % (crn))
        query_result = cursor.fetchall()
        for i in query_result:
                self.schedule.remove(i)
        return

    def set_schedule(self, x, y, z,):
        self.add_course(x)
        self.add_course(y)
        self.add_course(z)
        return

    def print_schedule(self):
        print("(ID, TITLE, CRN, DEPT, INSTRUCTORID, TIME, DAYS, SEMESTER, YEAR, CREDITS)")
        for i in self.schedule:
            print(i)
        return


# Instructor:
class Instructor(User):
    # instructor attributes
    title = ""
    hireYear = 0
    dept = ""
    email = ""
    courses = []

    # constructor
    def __init__(self, f, l, i, t, hy, d, e):
        User.__init__(self, f, l, i)
        self.title = t
        self.hireYear = hy
        self.dept = d
        self.email = e

        cursor.execute("""SELECT CRN FROM COURSE WHERE INSTRUCTORID = '%s'""" % (i))
        query_result = cursor.fetchall()
        for n in query_result:
            self.courses.append(n)

    # printing method using __str__ and __repr__
    def __str__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

    def __repr__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

    def print_schdule(self):
        cursor.execute("""SELECT * FROM COURSE WHERE INSTRUCTORID = '%s'""" % (self.ID))
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)
        return

    def link_course(self, course_ID):
        self.courses.append(course_ID)
        cursor.execute("""UPDATE COURSE SET INSTRUCTORID=%s WHERE ID=%s""" % (self.ID, course_ID))
        return

    def unlink_course(self, course_ID):
        for c in self.courses:
            if c == course_ID:
                self.courses.remove(c)
                cursor.execute("""UPDATE COURSE SET INSTRUCTORID=0 WHERE ID=""" + str(course_ID))
        return

#  Admin:
class Admin(User):
    # instructor attributes
    title = ""
    office = ""
    email = ""

    # constructor
    def __init__(self, f, l, i, t, o, e):
        User.__init__(self, f, l, i)
        self.title = t
        self.office = o
        self.email = e

    # printing method using __str__ and __repr__
    def __str__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

    def __repr__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

