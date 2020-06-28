#####################################
# curse_db.py
# file to set up database for CURSE project
#####################################

import sqlite3

# database file connection
database = sqlite3.connect("assignment7.db")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
cursor = database.cursor()

allTables = ["STUDENT", "INSTRUCTOR", "ADMIN", "COURSE"]

###################################################################### create tables
# Create STUDENT table in the database
cursor.execute("""DROP TABLE IF EXISTS STUDENT;""")
cursor.execute("""CREATE TABLE STUDENT (  
ID 		INT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
GRADYEAR	INT 	NOT NULL,
MAJOR		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL);""")

# Create INSTRUCTOR table in the database
cursor.execute("""DROP TABLE IF EXISTS INSTRUCTOR;""")
cursor.execute("""CREATE TABLE INSTRUCTOR (  
ID 		INT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
HIREYEAR	INT 	NOT NULL,
DEPT		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL);""")

# Create ADMIN table in the database
cursor.execute("""DROP TABLE IF EXISTS ADMIN;""")
cursor.execute("""CREATE TABLE ADMIN (  
ID 		INT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
OFFICE		TEXT 	NOT NULL,
EMAIL		text	NOT NULL);""")

# Create COURSE table in the database
cursor.execute("""DROP TABLE IF EXISTS COURSE;""")
cursor.execute("""CREATE TABLE COURSE (
ID 				INT 	PRIMARY KEY 	NOT NULL,
TITLE			TEXT	NOT NULL,
CRN				INT 	NOT NULL,
DEPT			CHAR(4) NOT NULL,
INSTRUCTORID	INT 	FORIEGN KEY		NOT NULL,
TIME			INT		NOT NULL,
DAYS			TEXT	NOT NULL,
SEMESTER		TEXT	NOT NULL,
YEAR			INT		NOT NULL,
CREDITS			INT		NOT NULL);""")

###################################################################### insert examples

# Student list
cursor.execute("""INSERT INTO STUDENT VALUES(00010001, 'Isaac', 'Newton', 1668, 'BSAS', 'newtoni');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010002, 'Marie', 'Curie', 1903, 'BSAS', 'curiem');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010003, 'Nikola', 'Tesla', 1878, 'BSEE', 'telsan');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010004, 'Thomas', 'Edison', 1879, 'BSEE', 'notcool');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010005, 'John', 'von Neumann', 1923, 'BSCO', 'vonneumannj');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010006, 'Grace', 'Hopper', 1928, 'BCOS', 'hopperg');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010007, 'Mae', 'Jemison', 1981, 'BSCH', 'jemisonm');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010008, 'Mark', 'Dean', 1979, 'BSCO', 'deanm');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010009, 'Michael', 'Faraday', 1812, 'BSAS', 'faradaym');""")
cursor.execute("""INSERT  INTO STUDENT VALUES(00010010, 'Ada', 'Lovelace', 1832, 'BCOS', 'lovelacea');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010011, 'Scott', 'Pilgrim', 1980, 'BSCO', 'pilgrims');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010012, 'John', 'Locke', 1960, 'BSEE', 'lockej');""")

# Instructor list
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020001, 'Joseph', 'Fourier', 'Full Prof.', 1820, 'BSEE', 'fourierj');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020002, 'Nelson', 'Mandela', 'Full Prof.', 1994, 'HUSS', 'mandelan');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020003, 'Galileo', 'Galilei', 'Full Prof.', 1600, 'BSAS', 'galileig');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020004, 'Alan', 'Turing', 'Associate Prof.', 1940, 'BSCO', 'turinga');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020005, 'Katie', 'Bouman', 'Assistant Prof.', 2019, 'BCOS', 'boumank');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020006, 'Daniel', 'Bernoulli', 'Associate Prof.', 1760, 'BSME', 'bernoullid');""")

# Admin list
cursor.execute("""INSERT INTO ADMIN VALUES(00030001, 'Barack', 'Obama', 'President', 'Dobbs 1600', 'obamab');""")
cursor.execute("""INSERT INTO ADMIN VALUES(00030002, 'Malala', 'Yousafzai', 'Registrar', 'Wentworth 101', 'yousafzaim');""")

# Course List
cursor.execute("""INSERT INTO COURSE VALUES(00090000, "INTRO TO TIME TRAVEL", 48151, 'BSAS', 20003, 10, 'MWF', 'FALL', 2020, 3);""")
cursor.execute("""INSERT INTO COURSE VALUES(00090001, "INTERMEDIATE WORMHOLES", 48152, 'BSME', 20006, 12, 'TR', 'FALL', 2020, 4);""")
cursor.execute("""INSERT INTO COURSE VALUES(00090002, "THEORY OF EVERYTHING", 48153, 'BSCO', 20004, 14, 'MW', 'FALL', 2020, 4);""")
cursor.execute("""INSERT INTO COURSE VALUES(00090003, "NU-CALCULUS", 48154, 'BSAS', 20003, 14, 'MTR', 'FALL', 2020, 4);""")
cursor.execute("""INSERT INTO COURSE VALUES(00090004, "UFOLOGY: A DEEP DIVE", 48155, 'HUSS', 20002, 8, 'MW', 'FALL', 2020, 4);""")

# close the connection

database.commit()
database.close()
