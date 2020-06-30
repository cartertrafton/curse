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

#add/drop courses from schedule
def add_drop():
    schedule = [] 
    s = str(input("Enter Semester (FALL, SPRING, OR SUMMER):"))
    print("===========================================")
    print("Courses Offered:")
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
            crn = input("Enter CRN to add course:")
            cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%s'""" % (crn))
            query_result = cursor.fetchall()
            for i in query_result:
                schedule.append(i)
            i = 0
        if(temp == '2'):
            print("===========================================")
            print("Student Schedule:")
            print(schedule)
            print("===========================================")
            crn = input("Enter CRN to drop course:")
            cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%s'""" % (crn))
            query_result = cursor.fetchall()
            for i in query_result:
                schedule.remove(i)
                print("===========================================")
                print("Updated Student Schedule:")
                print(schedule)
            i = 0
        if(temp == '0'):
            i = 1
    return   

#add course to system
def add_course():
        print("Enter Course Information")
        CRN = input("CRN of Course:")
        Id = input("Id of Course:")
        In_Id = input("ID of Instructor for Course:")
        title = input("Course Title:")
        dept = input("Course Department:")
        time = input("Course Time:")
        days = input("Course Days:") 
        semester = input("Course Semester:")
        year = input("Course Year:")
        credit = input("Amount of credits:")
        print("===========================================")
        print("Course Added")

        cursor.execute("""INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s', '%s', '%s');""" % (Id, title, CRN, dept, In_Id, time, days, semester, year, credit))

#remove course from system        
def remove_course():
    temp = input("Enter CRN to remove course:")
    cursor.execute("""DELETE FROM COURSE WHERE CRN = '%s';""" % (temp))
    print("===========================================")
    print("Course removed")
    
#print roster
def print_roster(schedule, St_ID, C_ID):
    
    cursor.execute("""SELECT * FROM COURSE WHERE ID = '%s'""" % (C_ID))
    query_result = cursor.fetchall()
    out = any(check in schedule for check in query_result) 
    if out: 
         cursor.execute("""SELECT SURNAME, NAME FROM STUDENT WHERE ID = '%s'""" % (St_ID))
         query_result = cursor.fetchall()
         for i in query_result:
               print(i)
         return
    else: 
    
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

    s1 = Student('Isaac', 'Newton', 10001, 1668, 'BSAS', 'newtoni')
    schedule1 = s1.set_schedule('48151', '48152', '48153')
    s2 = Student('Marie', 'Curie', 10002, 1903, 'BSAS', 'curiem')
    schedule2 = s2.set_schedule('48151', '48154', '48155')
    s3 = Student('Nikola', 'Tesla', 10003, 1878, 'BSEE', 'teslan')
    schedule3 = s3.set_schedule('48152', '48154', '48155')
    s4 = Student('Thomas', 'Edison', 10004, 1879, 'BSEE', 'notcool')
    schedule4 = s4.set_schedule('48152', '48153', '48154')
    s5 = Student('Grace', 'Hopper', 10006, 1928, 'BCOS', 'hopperg')
    schedule5 = s5.set_schedule('48151', '48152', '48153')
    student1 = s1.get_ID()
    student2 = s2.get_ID()
    student3 = s3.get_ID()
    student4 = s4.get_ID()
    student5 = s5.get_ID()
    
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
                        print("===========================================")
                        print("Your Courses:")
                        cursor.execute("""SELECT * FROM COURSE WHERE INSTRUCTORID = '%s'""" % (iID))
                        query_result = cursor.fetchall()
  
                        for i in query_result:
                                    print(i)  
                                    
                        print("===========================================")
                        temp = input("Enter Course Id to print roster:")
                        print("===========================================")
                        print("Roster:")
                        print_roster(schedule1, student1, temp)
                        print_roster(schedule2, student2, temp)
                        print_roster(schedule3, student3, temp)
                        print_roster(schedule4, student4, temp)
                        print_roster(schedule5, student5, temp)                      

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
