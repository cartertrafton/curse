#####################################
# curse_c.py
# classes for CURSE project
#####################################


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
# 	can search courses, add/drop courses, print schedule.
class Student(user):
    # constructor
    def __init__(self, f, l, i):
        user.__init__(self, f, l, i)

    # printing method using __str__ and __repr__
    def __str__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

    def __repr__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))


# Instructor:
#	can print schedules/rosters, search courses.
class Instructor(user):
    # constructor
    def __init__(self, f, l, i):
        user.__init__(self, f, l, i)

    # printing method using __str__ and __repr__
    def __str__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

    def __repr__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))


#  Admin:
# 	can add courses to the system, remove courses from the system,
#  	add/remove users, force student in or out of course/rosters,
#  	search/print rosters/courses
class Admin(user):
    # constructor
    def __init__(self, f, l, i):
        user.__init__(self, f, l, i)

    # printing method using __str__ and __repr__
    def __str__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

    def __repr__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))
