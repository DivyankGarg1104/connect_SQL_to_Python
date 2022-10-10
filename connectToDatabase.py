def create_server_connection(host_name, username, user_passwd,db_name):       #Here the database name is also added as a parameter in the function
    connection=None
    try:
        connection=mysql.connector.connect(host=host_name, user=username, password=user_passwd, database= db_name)
        print("MySQL Database Connection SUCCESSFUL....")
    except Error as err:
        print(f"Error: '{err}' ")
    return connection
    