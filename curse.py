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



######################### functions
# search all courses (no parameters)
def searchAllCourses():
    cursor.execute("""SELECT * FROM COURSE""")
    query_result = cursor.fetchall()
    print("===========================================")
    print("ID, TITLE, CRN, DEPT, INSTRUCTORID, TIME, DAYS, SEMESTER, YEAR, CREDITS")
    print("===========================================")
    for i in query_result:
        print(i)
    print("===========================================")

    return

# search all courses (with parameters)
def searchAllCoursesWithParam():
    command = ''
    try:
        cursor.execute(command)
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)
    except:
        print("\nERROR... try again\n")
    return



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
    print(" [ 1 ] to Print Teaching Schedule")
    print(" [ 2 ] to Print Class Roster")
    print(" [ 3 ] to Search Courses")
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
    print(" [ 5 ] to Search Courses")
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

        # STUDENT LOGIN
        elif select == 1:

            inputID = str(input("Enter Student ID #: "))
            cursor.execute("""SELECT COUNT(*) FROM STUDENT WHERE ID=""" + inputID)
            IDcount = str(cursor.fetchall())[2:-2].replace(",", "")
            print("\nLogging in...")

            if IDcount == "1":
                print("Success!\n\n")

                # gather data from database to create current user object
                cursor.execute("""SELECT NAME FROM STUDENT WHERE ID=""" + inputID)
                sName = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT SURNAME FROM STUDENT WHERE ID=""" + inputID)
                sSurname = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT ID FROM STUDENT WHERE ID=""" + inputID)
                sID = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT GRADYEAR FROM STUDENT WHERE ID=""" + inputID)
                sGradyear = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT MAJOR FROM STUDENT WHERE ID=""" + inputID)
                sMajor = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT EMAIL FROM STUDENT WHERE ID=""" + inputID)
                sEmail = str(cursor.fetchall())[2:-2].replace(",", "")

                # create current user object
                currentUser = Student(sName, sSurname, sID, sGradyear, sMajor, sEmail)
                print("Welcome, " + currentUser.firstName.replace("'", "") + " " + currentUser.lastName.replace("'", ""))

                while(select != 0):
                    studentSelect = studentMenu()
                    if studentSelect == 0:
                        print("Logging out...")
                        break

                    elif studentSelect == 1:
                        # search
                        print("===========================================")
                        print(" [ 1 ] to Search All Courses")
                        print(" [ 2 ] to Search Courses by Parameter")
                        print("===========================================")
                        searchSelect = int(input())
                        if searchSelect == 1:
                            searchAllCourses()
                        elif searchSelect == 2:
                            searchAllCoursesWithParam()
                        else:
                            print("Unrecognized choice...")

                    elif studentSelect == 2:
                        # add/drop
                        print()

                    elif studentSelect == 3:
                        # print schedule
                        print()

                    else:
                        print("Unrecognized selection!")
            else:
                print("\nERROR: ID# NOT FOUND OR DOES NOT MATCH LOGIN TYPE\n")

        # INSTRUCTOR LOGIN
        elif select == 2:
            inputID = str(input("Enter Employee ID #: "))
            cursor.execute("""SELECT COUNT(*) FROM INSTRUCTOR WHERE ID=""" + inputID)
            IDcount = str(cursor.fetchall())[2:-2].replace(",", "")
            print("\nLogging in...")

            if IDcount == "1":
                print("Success!\n\n")

                # gather data from database to create current user object
                cursor.execute("""SELECT NAME FROM INSTRUCTOR WHERE ID=""" + inputID)
                iName = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT SURNAME FROM INSTRUCTOR WHERE ID=""" + inputID)
                iSurname = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT ID FROM INSTRUCTOR WHERE ID=""" + inputID)
                iID = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT TITLE FROM INSTRUCTOR WHERE ID=""" + inputID)
                iTitle = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT HIREYEAR FROM INSTRUCTOR WHERE ID=""" + inputID)
                iHireYear = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT DEPT FROM INSTRUCTOR WHERE ID=""" + inputID)
                iDept = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT EMAIL FROM INSTRUCTOR WHERE ID=""" + inputID)
                iEmail = str(cursor.fetchall())[2:-2].replace(",", "")

                # create current user object
                currentUser = Instructor(iName, iSurname, iID, iTitle, iHireYear, iDept, iEmail)
                print("Welcome, " + currentUser.firstName.replace("'", "") + " " + currentUser.lastName.replace("'", ""))

                while (select != 0):
                    instructorSelect = instructorMenu()
                    if instructorSelect == 0:
                        # log out
                        print("Logging out...")
                        break

                    elif instructorSelect == 1:
                        # print schedule
                        print()

                    elif instructorSelect == 2:
                        # print roster
                        print()

                    elif instructorSelect == 3:
                        # search
                        print("===========================================")
                        print(" [ 1 ] to Search All Courses")
                        print(" [ 2 ] to Search Courses by Parameter")
                        print("===========================================")
                        searchSelect = int(input())
                        if searchSelect == 1:
                            searchAllCourses()
                        elif searchSelect == 2:
                            searchAllCoursesWithParam()
                        else:
                            print("Unrecognized choice...")

                    else:
                        print("Unrecognized selection!")
            else:
                print("\nERROR: ID# NOT FOUND OR DOES NOT MATCH LOGIN TYPE\n")


        # ADMIN FUNCTIONS
        elif select == 3:
            inputID = str(input("Enter Employee ID #: "))
            cursor.execute("""SELECT COUNT(*) FROM ADMIN WHERE ID=""" + inputID)
            IDcount = str(cursor.fetchall())[2:-2].replace(",", "")
            print("\nLogging in...")

            if IDcount == "1":
                print("Success!\n\n")

                # gather data from database to create current user object
                cursor.execute("""SELECT NAME FROM ADMIN WHERE ID=""" + inputID)
                aName = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT SURNAME FROM ADMIN WHERE ID=""" + inputID)
                aSurname = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT ID FROM ADMIN WHERE ID=""" + inputID)
                aID = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT TITLE FROM ADMIN WHERE ID=""" + inputID)
                aTitle = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT OFFICE FROM ADMIN WHERE ID=""" + inputID)
                aOffice = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT EMAIL FROM ADMIN WHERE ID=""" + inputID)
                aEmail = str(cursor.fetchall())[2:-2].replace(",", "")

                # create current user object
                currentUser = Admin(aName, aSurname, aID, aTitle, aOffice, aEmail)
                print("Welcome, " + currentUser.firstName.replace("'", "") + " " + currentUser.lastName.replace("'", ""))

                while (select != 0):
                    adminSelect = adminMenu()
                    if adminSelect == 0:
                        # log out
                        print("Logging out...")
                        break

                    if adminSelect == 0:
                        # log out and exit
                        print(adminSelect)

                    elif adminSelect == 1:
                        # add course
                        print()

                    elif adminSelect == 2:
                        # remove course
                        print()

                    elif adminSelect == 3:
                        # add/remove users
                        print()

                    elif adminSelect == 4:
                        # override
                        print()

                    elif adminSelect == 5:
                        # search
                        print("===========================================")
                        print(" [ 1 ] to Search All Courses")
                        print(" [ 2 ] to Search Courses by Parameter")
                        print("===========================================")
                        searchSelect = int(input())
                        if searchSelect == 1:
                            searchAllCourses()
                        elif searchSelect == 2:
                            searchAllCoursesWithParam()
                        else:
                            print("Unrecognized choice...")

                    else:
                        print("Unrecognized selection!")
            else:
                print("\nERROR: ID# NOT FOUND OR DOES NOT MATCH LOGIN TYPE\n")

    return


######################### calling main
if __name__=="__main__":
    print("\n Welcome to......")
    print("     . | '''.| '||'  '|' '||''|.    .|'''. | '||''''|   ")
    print("    .|'     '   ||    |   ||   ||   ||..  '   ||  .     ")
    print("    ||          ||    |   ||''|'     ''|||.   ||''|     ")
    print("    '|.      .  ||    |   ||   |.  .     '||  ||        ")
    print("     ''|....'    '|..'   .||.  '|' |'....|'  .||.....|  ")
    print("------------------------------------------------------------------")
    print("           Course User Registration System Emulator")
    print("------------------------------------------------------------------")


    main()