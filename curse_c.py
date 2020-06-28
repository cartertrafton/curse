#####################################
# curse_c.py
# classes for CURSE project
#####################################

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

    # constructor
    def __init__(self, f, l, i, g, m, e):
        User.__init__(self, f, l, i)
        self.gradYear = g
        self.major = m
        self.email = e

    # printing method using __str__ and __repr__
    def __str__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

    def __repr__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))


# Instructor:
class Instructor(User):
    # instructor attributes
    title = ""
    hireYear = 0
    dept = ""
    email = ""

    # constructor
    def __init__(self, f, l, i, t, hy, d, e):
        User.__init__(self, f, l, i)
        self.title = t
        self.hireYear = hy
        self.dept = d
        self.email = e

    # printing method using __str__ and __repr__
    def __str__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))

    def __repr__(self):
        return str('Name: ' + self.firstName + ', ' + self.lastName + '.    ID: ' + str(self.ID))


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



