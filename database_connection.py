from my_package import *
# from my_package import maketables,disp,relate
# from my_package import create_db_connection,create_database,execute_query


username = 'admin'
password = 'password'    
conn = create_db_connection("localhost", username, password)
    
def init():    
    check = disp(conn, "SHOW DATABASES LIKE 'hospital'")
    if len(check) == 0:    
        create_database(conn, "hospital")
        execute_query(conn, "use hospital")
        maketables(conn)
        relate(conn)
        print("Hospital database created")
    else: 
        print("Connection to hospital established")

    # execute_query(conn,'use hospital')
    # data = disp(conn, "show tables")
    # for a in data:
    #     print(a,end = ' ')
