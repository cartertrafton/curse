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
    # input search term
    searchTerm = str(input("Enter a term to search by: "))

    # check for match in ID, TITLE, CRN, DEPT, INSTRUCTORID, TIME, DAYS, SEMESTER, YEAR, CREDITS
    command = "SELECT * FROM COURSE WHERE ID LIKE '%" + searchTerm + "%' or TITLE LIKE '%" + searchTerm + "%' or CRN LIKE '%" \
              + searchTerm + "%' or DEPT LIKE '%" + searchTerm + "%' or INSTRUCTORID LIKE '%" + searchTerm + "%' or TIME LIKE '%" + searchTerm \
              + " %' or DAYS LIKE '%" + searchTerm + "%' or SEMESTER LIKE '%" + searchTerm + "%' or YEAR LIKE '%" + searchTerm + "%' or CREDITS LIKE '%" + searchTerm + "%'"

    cursor.execute(command)
    query_result = cursor.fetchall()
    print("===========================================")
    print("ID, TITLE, CRN, DEPT, INSTRUCTORID, TIME, DAYS, SEMESTER, YEAR, CREDITS")
    print("===========================================")
    for i in query_result:
        print(i)
    print("===========================================")
    return


# search courses
def searchCoursesMenu():
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
    return


# add/drop courses from schedule
def student_add_drop(currentUser):
    s = str(input("Enter Semester (FALL, SPRING, OR SUMMER):"))
    print("===========================================")
    print("Courses Offered:")
    print("ID, TITLE, CRN, DEPT, INSTRUCTORID, TIME, DAYS, SEMESTER, YEAR, CREDITS")
    print("===========================================")
    cursor.execute("""SELECT * FROM COURSE WHERE SEMESTER = '%s'""" % (s))
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)      

    i = 0
    while i == 0:
        print("===========================================")
        temp = input("Enter 1 to Add a Course, 2 to Remove Course, and 0 to Exit:")
        if(temp == '1'):
            print("===========================================")
            print("Student Schedule:")
            currentUser.print_schedule()
            print("===========================================")
            crn = input("Enter CRN to add course:")
            currentUser.add_course(crn)
            print("===========================================")
            print("Updated Student Schedule:")
            currentUser.print_schedule()
            i = 0

        if(temp == '2'):
            print("===========================================")
            print("Student Schedule:")
            currentUser.print_schedule()
            print("===========================================")
            crn = input("Enter CRN to drop course:")
            currentUser.remove_course(crn)
            print("===========================================")
            print("Updated Student Schedule:")
            currentUser.print_schedule()
            i = 0
        if(temp == '0'):
            i = 1
    return   


# add course to system
def admin_add_course():
    print("Enter Course Information")
    CRN = str(input("CRN of Course:"))
    Id = str(input("ID of Course:"))
    In_Id = str(input("ID of Instructor for Course:"))
    title = str(input("Course Title:"))
    dept = str(input("Course Department:"))
    time = str(input("Course Time:"))
    days = str(input("Course Days:"))
    semester = str(input("Course Semester:"))
    year = str(input("Course Year:"))
    credit = str(input("Amount of credits:"))
    print("===========================================")
    print("Course Added")
    cursor.execute("""INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (Id, title, CRN, dept, In_Id, time, days, semester, year, credit))
    return

# remove course from system
def admin_remove_course():
    temp = input("Enter CRN to remove course:")
    cursor.execute("""DELETE FROM COURSE WHERE CRN = '%s';""" % (temp))
    print("===========================================")
    print("Course removed")
    return

# print roster
def instructor_print_roster(user, student_list):
    print("===========================================")
    print("Students in classes taught by: " + user.firstName.replace("'", "") + " " + user.lastName.replace("'", ""))
    print("===========================================")
    for s in student_list:
        for x in s.instructors:
            if str(user.ID) == str(x):
                print(s)

    # s = str(input("Enter Semester (FALL, SPRING, OR SUMMER):"))
    # print("===========================================")
    # print("Courses this semester:")
    # print("ID, TITLE, CRN, DEPT, INSTRUCTORID, TIME, DAYS, SEMESTER, YEAR, CREDITS")
    # print("===========================================")
    # cursor.execute("""SELECT * FROM COURSE WHERE SEMESTER = '%s'""" % (s))
    # query_result = cursor.fetchall()
    # for i in query_result:
    #     print(i)
    # print("===========================================")
    # temp = input("Enter CRN to print class roster:")
    # cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%s'""" % (temp))
    # query_result = cursor.fetchall()
    # out = any(check in schedule for check in query_result)
    # if out:
    #     print("True")
    # else :
    #     print("False")

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
    # create example students and fill their schedules
    student1 = Student("John", "Locke", 10012, 1960, "BSEE", "lockej")
    student1.set_schedule(48155, 48152, 48151)
    student1.instructors = [20002, 20006, 20003]

    student2 = Student("Ada", "Lovelace", 10010, 1832, "BCOS", "lovelacea")
    student2.set_schedule(48155, 48153, 48151)
    student2.instructors = [20002, 20004,  20003]

    student3 = Student("Scott", "Pilgrim", 10011, 1980, "BSCO", "pilgrims")
    student3.set_schedule(48155, 48152, 48153)
    student3.instructors = [20002, 20006, 20004]


    # add example students to a list
    student_list = [student1, student2, student3]

    active = 1

    while active == 1:
        # prompt user for log in input
        select = mainMenu()

        # exit program
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

            # if student ID exists in table, create student object with info from db
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
                    # prompt student for menu
                    studentSelect = studentMenu()
                    if studentSelect == 0:
                        print("Logging out...")
                        break
                    elif studentSelect == 1:
                        # search
                        searchCoursesMenu()
                    elif studentSelect == 2:
                        # add/drop
                        student_add_drop(currentUser)
                        print()
                    elif studentSelect == 3:
                        # print schedule
                        currentUser.print_schedule()
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

            # if employee ID exists in table, create instructor object with info from db
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
                        currentUser.print_schdule()
                        print()
                    elif instructorSelect == 2:
                        # print roster
                        instructor_print_roster(currentUser, student_list)
                    elif instructorSelect == 3:
                        # search
                        searchCoursesMenu()
                    else:
                        print("Unrecognized selection!")
            else:
                print("\nERROR: ID# NOT FOUND OR DOES NOT MATCH LOGIN TYPE\n")


        # ADMIN LOGIN
        elif select == 3:
            inputID = str(input("Enter Employee ID #: "))
            cursor.execute("""SELECT COUNT(*) FROM ADMIN WHERE ID=""" + inputID)
            IDcount = str(cursor.fetchall())[2:-2].replace(",", "")
            print("\nLogging in...")

            # if employee ID exists in table, create admin object with info from db
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
                    elif adminSelect == 1:
                        # add course
                        admin_add_course()
                    elif adminSelect == 2:
                        # remove course
                        admin_remove_course()
                    elif adminSelect == 3:
                        # add/remove users
                        ######################## ADD HERE
                        print()
                    elif adminSelect == 4:
                        # override
                        ######################## ADD HERE
                        print()
                    elif adminSelect == 5:
                        # search
                        searchCoursesMenu()
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
