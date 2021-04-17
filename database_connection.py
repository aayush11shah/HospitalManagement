from my_package import *

username = 'admin'
password = 'password'    
conn = create_db_connection("localhost", username, password)

def execute_query(query):
    conn = create_db_connection("localhost", username, password, "hospital")
    Connector.execute_query(conn, query)
    
def disp(query):
    conn = create_db_connection("localhost", username, password,"hospital")
    return Connector.disp(conn, query)

def incr(look = True):
    incr_index = disp(" Select AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'hospital' AND TABLE_NAME = 'patient'")
    # print(incr_index,type(incr_index))
    if(look):
        print("LOOKING",'delete from patient where p_id = '+str(incr_index[0][0]+1))
        insert_patient('password','name','b',0,'g',0,0,999999999,'NULL')
        execute_query('delete from patient where p_id = '+str(incr_index[0][0]+1))
        
    return incr_index[0][0]    

def init():   

    conn = create_db_connection("localhost", username, password)
    check = Connector.disp(conn,"SHOW DATABASES LIKE 'hospital'")
    if len(check) == 0:    
        Connector.create_database(conn, "hospital")
        Connector.execute_query(conn,"use hospital")
        maketables(conn)
        relate(conn)
        print("Hospital database created")
    else: 
        print("Connection to hospital established")
        execute_query("use hospital")
    # dept_q = insert_dept("Opthalmology", 2, 10)
    # execute_query(dept_q)
    # d_q = insert_doctor("2534hed", "YNisarg","Chou",237311, 12, 99180000, 1, "111110000000011111")
    # execute_query(d_q)
    
init()
