#####################################
# curse.py
# main file for CURSE project
#####################################


######################### set up
from curse_c import *

# database set up
import sqlite3

db = sqlite3.connect("assignment7.db")
cursor = db.cursor()
allTables = ["STUDENT", "INSTRUCTOR", "ADMIN", "COURSE"]

######################### printing functions
def mainMenu():
    print("===========================================")
    print(" [ 1 ] for Student Log-in ")
    print(" [ 2 ] for Instructor Log-in ")
    print(" [ 3 ] for Administrator Log-in ")
    print(" [ 0 ] to Exit ")
    print("===========================================")
    select = int(input())
    return select


# student functions menu
def studentMenu():
    print("===========================================")
    print(" [ 1 ] to Search Courses")
    print(" [ 2 ] to Add/Drop Courses")
    print(" [ 3 ] to Print Schedule")
    print(" [ 0 ] to Log Out")
    print("===========================================")
    studentSelect = int(input())
    return studentSelect


# instructor functions menu
def instructorMenu():
    print("===========================================")
    print(" [ 1 ] to Print Schedule/Roster")
    print(" [ 2 ] to Search Courses")
    print(" [ 0 ] to Log Out")
    print("===========================================")
    instructorSelect = int(input())
    return instructorSelect


# admin functions menu
def adminMenu():
    print("===========================================")
    print(" [ 1 ] to to Add Course to System")
    print(" [ 2 ] to Remove Course from System")
    print(" [ 3 ] to Add/Remove Users")
    print(" [ 4 ] to Override Student In/Out of Course or Roster")
    print(" [ 5 ] to Search/Print Schedule or Roster")
    print(" [ 0 ] to Log Out")
    print("===========================================")
    adminSelect = int(input())
    return adminSelect

######################### main loop
def main():
    active = 1

    while active == 1:
        select = mainMenu()

        if select == 0:
            active = 0
            print("Exiting...")
            break

        elif select == 1:
            studentSelect = studentMenu()
            # student functions go here

        elif select == 2:
            instructorSelect = instructorMenu()
            # instructor functions go here

        elif select == 3:
            adminSelect = adminMenu()
            # admin functions go here
        else:
            print("Unrecognized selection!")

    return


######################### calling main
if __name__=="__main__":
    main()