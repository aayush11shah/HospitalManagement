
def insert_patient(password,name,blood_grp,age,gender,ph_no,address,aadhar_id,p_history):
    query1 = "insert into patient(password,p_name,blood_grp,age,gender,ph_no,address,aadhar_id,p_history) "
    query2 = "values('{}','{}','{}',{},'{}',{},'{}',{},'{}')".format(password,name,blood_grp,str(age),gender,str(ph_no),address,str(aadhar_id),p_history)
    return(query1+query2)
    
def insert_doctor(password,fname,lname,aadhar_id,chamber,sal,dept_id,timeslot):
    query1 = "insert into doctor(password,first_name,last_name,aadhar_id,chamber,salary,dept_id,timeslot) "
    query2 = "values('{}','{}','{}',{},'{}',{},{},'{}')".format(password,fname,lname,aadhar_id,chamber,sal,dept_id,timeslot)
    return(query1+query2)

def insert_dept(dept_name, available_docs, total_docs, hod_doc_id = 0):
    query1 = "insert into department(dept_name, available_docs, total_docs) "
    query2 = "values('{}','{}','{}')".format(dept_name, available_docs, total_docs)
    return(query1+query2)


    

