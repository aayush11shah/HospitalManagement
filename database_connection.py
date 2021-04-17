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
