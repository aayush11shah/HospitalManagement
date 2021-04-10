import mysql.connector
from mysql.connector import Error

''' A function to create and return a connection with localhost '''
def create_db_connection(host_name, user_name, user_password, db_name = None):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


''' A funtion to create a database of a given name via a connection '''
def create_database(connection, name):
    cursor = connection.cursor()
    try:
        cursor.execute("create database " + name)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


''' A function to exectute a query in a connection '''
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        # print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

''' A debugging function to display output '''
def disp(connection, query):
    # print("The output of the " + query + " query is")
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    data = cursor.fetchall()
    return data
