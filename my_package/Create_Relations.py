from .Connector import execute_query

alter_dept = """
ALTER TABLE department
ADD CONSTRAINT FK_DOCTOR  
FOREIGN KEY(hod_doc_id)
REFERENCES doctor(doc_id)
ON DELETE SET NULL;
"""

alter_doctor = """
ALTER TABLE doctor
auto_increment = 100,

ADD FOREIGN KEY(dept_id)
REFERENCES department(dept_id)
ON DELETE SET NULL;
"""

### There is no dependency for Patient table 
alter_patient = """
ALTER TABLE patient
auto_increment = 1000;
"""


### There is no dependency for Expense table 

alter_transact = """
ALTER TABLE transact

ADD FOREIGN KEY(item_id)
REFERENCES expense(item_id),

ADD FOREIGN KEY(p_id)
REFERENCES patient(p_id);
"""

alter_room = """
ALTER TABLE room
ADD FOREIGN KEY(p_id)
REFERENCES patient(p_id);
"""

### There is no dependency for Staff table 

alter_job = """
ALTER TABLE job
ADD FOREIGN KEY(ss_id)
REFERENCES staff(ss_id)
ON DELETE SET NULL;
"""

alter_appointment = """
ALTER TABLE appointment

ADD FOREIGN KEY(p_id)
REFERENCES patient(p_id),

ADD FOREIGN KEY(doc_id)
REFERENCES doctor(doc_id);
"""

#   PRIMARY KEY(participant_id, course_id),
#   FOREIGN KEY(participant_id) REFERENCES participant(participant_id) ON DELETE CASCADE, -- it makes no sense to keep this rtelation when a participant or course is no longer in the system, hence why CASCADE this time
#   FOREIGN KEY(course_id) REFERENCES course(course_id) ON DELETE CASCADE

def relate(connection):
	# execute_query(connection, alter_dept)
	execute_query(connection, alter_doctor)
	execute_query(connection, alter_patient)
	# execute_query(connection, alter_expense)
	execute_query(connection, alter_transact)
	execute_query(connection, alter_room)
	# execute_query(connection, alter_staff)
	execute_query(connection, alter_job)
	execute_query(connection, alter_appointment)
	print("Intricate relations have been established elegantly.")
