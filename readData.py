from pickle import NONE


def read_query(connection, query):
    cursor=connection.cursor()
    result=NONE
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        
    except Error as err:
        print(f"Error: '{err}'")
    return result

