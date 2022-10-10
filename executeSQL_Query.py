def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query was successfull....")
    except Error as err:
        print(f"Error: '{err}' ")
        