from .Connector import execute_query

create_deptartment_table = """
CREATE TABLE department (
	dept_id INT PRIMARY KEY AUTO_INCREMENT,
	dept_name VARCHAR(40) NOT NULL,
	available_docs INT,
	total_docs INT,
	hod_doc_id INT
);
"""

create_doctor_table = """
CREATE TABLE doctor (
	doc_id INT PRIMARY KEY AUTO_INCREMENT,
	Password VARCHAR(40),
	first_name VARCHAR(40) NOT NULL,
	last_name VARCHAR(40) NOT NULL,
	aadhar_id INT UNIQUE NOT NULL,
	chamber VARCHAR(3) NOT NULL,
	salary INT ,
	dept_id INT ,
	timeslot VARCHAR(18)
	);
"""

create_patient_table = """
CREATE TABLE patient (
	p_id INT PRIMARY KEY AUTO_INCREMENT,
	Password VARCHAR(40) NOT NULL,
	p_name VARCHAR(40) NOT NULL,
	blood_grp VARCHAR(3),
	age INT NOT NULL,
	gender VARCHAR(5),
	ph_no VARCHAR(10) NOT NULL,
	address VARCHAR(80) NOT NULL,
	aadhar_id INT UNIQUE NOT NULL,
	p_history VARCHAR(100)
);
"""

create_expense_table = """
CREATE TABLE expense (
	item_id INT PRIMARY KEY,
	item_name VARCHAR(40) NOT NULL,
	qty INT ,
	price INT NOT NULL
);
 """

create_transact_table = """
CREATE TABLE transact (
	transact_id int,
	p_id INT ,
	item_id INT ,
	pay_status INT,
	qty_bought INT,
	dt DATETIME,
	primary key (transact_id)
);
"""

create_room_table = """
CREATE TABLE room (
	room_id INT PRIMARY KEY,
	isAvailable VARCHAR(2),
	p_id INT
);
"""

create_staff_table = """
CREATE TABLE staff (
	ss_id INT PRIMARY KEY,
	ss_name VARCHAR(40) NOT NULL,
	Address VARCHAR(80) NOT NULL,
	Job VARCHAR(20) NOT NULL,
	Salary INT
);
"""
create_job_table = """
CREATE TABLE job (
	ss_id INT ,
	room_id INT 
);
"""
create_appointment_table = """
CREATE TABLE appointment (
	p_id INT ,
	doc_id INT ,
	start_date DATE,
	time INT,
	primary key (p_id, doc_id)
);
"""

create_appointment2_table = """
CREATE TABLE appointment (
	p_id INT ,
	doc_id INT ,
	start_date DATE,
	time INT,
	primary key (Doc_id, p_id, time)
);
"""


''' A function to make all the tables for the database '''
def maketables(connection):

	execute_query(connection, create_deptartment_table)
	execute_query(connection, create_doctor_table)
	execute_query(connection, create_patient_table)
	execute_query(connection, create_expense_table)
	execute_query(connection, create_transact_table)
	execute_query(connection, create_room_table)
	execute_query(connection, create_staff_table)
	execute_query(connection, create_job_table)
	execute_query(connection, create_appointment2_table)

	print("Robust Tables have been created..")