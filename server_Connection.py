from ssl import _PasswordType
import mysql.connector from mysql.connector
import Error
import pandas as pd


def create_server_connection(host_name, username, user_passwd):
    connection=None
    try:
        connection=mysql.connector.connect(host=host_name, user=username, password=user_passwd)
        print("MySQL Database Connection SUCCESSFUL....")
    except Error as err:
        print(f"Error: '{err}' ")
    return connection

#Put your MySQL Terminal _Password

pw="abcd"     #Put your own password

#Database name to be created

db="mysql_Python"

connection = create_server_connection("localhost", "root", pw)