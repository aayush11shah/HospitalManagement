
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


def loadbasicdata():
    dept = []
    dept.append(insert_dept("Pediatrics",5,5,1))
    dept.append(insert_dept("Gynecology",2,2,6))
    dept.append(insert_dept("Physicians",3,3,8))
    dept.append(insert_dept("Dermatology",1,1,11))
    dept.append(insert_dept("ENT",1,2,12))
    dept.append(insert_dept("Neurology",1,1,14))
    
    doc = []
    doc.append(insert_doctor("pass","Obediah","Stane",801578520,'A1',90000,1,'111111101110010011'))
    doc.append(insert_doctor("pass","Tom","Wayne",703232406,'A2',90000,1,'010010110100000110'))
    doc.append(insert_doctor("pass","Robert","Stark",365391356,'A3',90000,1,'010101100101100101'))
    doc.append(insert_doctor("pass","Ansel","Meddik",582629954,'A4',90000,1,'001001010101001001'))
    doc.append(insert_doctor("pass","Albert","Stone",313126212,'A5',90000,1,'100010001111010110'))

    doc.append(insert_doctor("pass","Joseph","Wilhem",343920949,'B1',100000,2,'100101101011001100'))
    doc.append(insert_doctor("pass","Callam","Curle",463017246,'B2',100000,2,'100110000100101010'))
    doc.append(insert_doctor("pass","John","Berty",626267533,'C1',80000,3,'100000100110110001'))
    doc.append(insert_doctor("pass","Harry","Potter",321742660,'C1',80000,3,'000011111001001000'))
    doc.append(insert_doctor("pass","Celine","Angless",314790474,'C1',80000,3,'110111010000011001'))
    
    doc.append(insert_doctor("pass","Katleen","Everglades",677879146,'D1',70000,4,'111011101100101111'))
    doc.append(insert_doctor("pass","Arthur","Curry",817963674,'E1',70000,5,'000110100100111011'))
    doc.append(insert_doctor("pass","Dasya","Fisher",697301369,'E2',120000,5,'110001001011000111'))
    doc.append(insert_doctor("pass","Jennifer","Ezzel",546322847,'F1',120000,6,'011000100101010000'))
    doc.append(insert_doctor("pass","Lois","Lane",554275045,'F2',120000,6,'001111000111010010')) 
    #insert_patient("pass",name,'A+',12,'F',94856034390,"",aadhar_id,p_history):
    #doc.append(insert_doctor("pass","Lois","Lane",554275000425,'F2',1,'001111000111010010')
    item = []
    item.append("insert into expense values (1, 'Consultation', 1, 2000)") 
    item.append("insert into expense values (2, 'Room charges', 1, 7000)") 
    item.append("insert into expense values (3, 'Food charges', 1, 3300)") 
    item.append("insert into expense values (4, 'Eucalyptus Oil', 100, 2000)") 
    item.append("insert into expense values (5, 'Sanitizer', 25, 2000)") 
    item.append("insert into expense values (7, 'Crutches', 10, 2000)")
    item.append("insert into expense values (6, 'Mask', 1000, 80)")
    item.append("insert into expense values (8, 'Paracetamol', 800, 300)") 
    item.append("insert into expense values (9, 'Eucalyptus Oil', 100, 2000)") 
    item.append("insert into expense values (10, 'Vitamin Tablets', 25, 200)") 
     
    
    return dept,doc,item
    

