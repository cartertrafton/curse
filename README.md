# C.U.R.S.E.
Course User Registration System Emulator.

Built for Prof. Carpenter's ***Applied Programming Concepts*** Course for WIT Summer 2020.

## Program Structure
- ``curse.py`` - Main program to run, includes UI and ```main()``` loop.
- ``curse_c.py`` - File containing class definitions.
- ``curse_db.py`` - File containing database queries to run to set up.

#### Flowchart
![flowchart](https://github.com/cartertrafton/curse/blob/master/process_models/flowchart.png?raw=true)



## Features
- Database of users 
- Database of courses
- Three types of users (Student, Instructor, Admin)
- User functions:
   - All:
        - Login, logout
        - Search for courses (all or based on some parameter)
   - Student:
        - Add/remove course from semester schedule (based on course ID number)
        - Check conflicts in course schedule
        - Print individual schedule
   - Instructor:
        - Print course teaching schedule
        - Print/search course roster(s)
   - Admin:
        - Add courses to the system
        - Remove courses from the system
        - Add instructor/students
        - Link (or unlink) instructor/student to course 

## Authors

* [**Carter Trafton**](https://github.com/cartertrafton) - cartertrafton@gmail.com

* [**Brandon Merluzzo**](https://github.com/merluzzob) - merluzzob@wit.edu

