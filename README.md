# C.U.R.S.E.
Course User Registration System Emulator.

Built for Prof. Carpenter's ***Applied Programming Concepts*** Course for WIT Summer 2020.

## Program Structure
- ``curse.py`` - Main program to run, includes UI and ```main()``` loop.
- ``curse_c.py`` - File containing class definitions.
- ``curse_db.py`` - File containing database queries to run to set up.
- ``assignment7.db`` - Database file used to hold tables.
- ``/process_models/`` - Folder containing modeling diagrams.
- ``/tests/`` - Folder containing test code and files


#### Flowchart
![flowchart](https://github.com/cartertrafton/curse/blob/master/process_models/flowchart.png?raw=true)



## Features
- Database of users 
- Database of courses
- Three types of users (Student, Instructor, Admin)
- User functions:
   - All:
        - [x] Login, logout
        - [x] Search for courses (all or based on some parameter)
   - Student:
        - [x] Add/remove course from semester schedule (based on course ID number)
        - [ ] Check conflicts in course schedule
        - [x] Print individual schedule
   - Instructor:
        - [x] Print course teaching schedule
        - [x] Print/search course roster(s)
   - Admin:
        - [x] Add courses to the system
        - [x] Remove courses from the system
        - [x] Add instructor/students
        - [x] Link (or unlink) instructor/student to course 

## Authors

* [**Carter Trafton**](https://github.com/cartertrafton) - cartertrafton@gmail.com

* [**Brandon Merluzzo**](https://github.com/merluzzob) - merluzzob@wit.edu

