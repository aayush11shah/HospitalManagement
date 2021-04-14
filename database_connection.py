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
    check = disp("SHOW DATABASES LIKE 'hospital'")
    if len(check) == 0:    
        create_database(conn, "hospital")
        execute_query("use hospital")
        maketables(conn)
        relate(conn)
        print("Hospital database created")
    else: 
        print("Connection to hospital established")
        execute_query("use hospital")
