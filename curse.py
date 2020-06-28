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
    try:
        cursor.execute("""SELECT * FROM COURSE""")
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)
    except:
        print("\nERROR... try again\n")
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

        # STUDENT LOGIN
        elif select == 1:
            inputID = str(input("Enter Student ID #: "))
            cursor.execute("""SELECT COUNT(*) FROM STUDENT WHERE ID=""" + inputID)


            if studentIDexists:
                print(cursor.fetchall()[0])


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

                studentSelect = studentMenu()
                # if studentSelect == 0:
                #
                # elif studentSelect == 1:
                #
                # elif studentSelect == 2:

            else:
                print("\nERROR: ID# NOT FOUND OR DOES NOT MATCH LOGIN TYPE\n")

        # INSTRUCTOR LOGIN
        elif select == 2:
            try:
                # gather data from database to create current user object
                cursor.execute("""SELECT NAME FROM STUDENT WHERE ID=""" + inputID)
                iName = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT SURNAME FROM STUDENT WHERE ID=""" + inputID)
                iSurname = str(cursor.fetchall())[2:-2].replace(",", "")
                cursor.execute("""SELECT ID FROM STUDENT WHERE ID=""" + inputID)
                iID = str(cursor.fetchall())[2:-2].replace(",", "")



                # create current user object
                currentUser = Instructor(iName, iSurname, iID, sGradyear, sMajor, sEmail)

                instructorSelect = instructorMenu()
                if instructorSelect == 0:
                    # log out and exit
                elif instructorSelect == 1:
                    # print schedule
                elif instructorSelect == 2:
                    # print roster
                elif instructorSelect == 3:
                    # search courses

            except:
                print("\nERROR: ID# NOT FOUND OR DOES NOT MATCH LOGIN TYPE\n")

        # ADMIN FUNCTIONS
        elif select == 3:

            adminSelect = adminMenu()
            if adminSelect == 0:
                # log out and exit
            elif adminSelect == 1:
                # add course
            elif adminSelect == 2:
                # remove course
            elif adminSelect == 3:
                # add/remove users
            elif adminSelect == 4:
                # override
            elif adminSelect == 5:
                # search/print schedule

        else:
            print("Unrecognized selection!")


    return


######################### calling main
if __name__=="__main__":
    main()