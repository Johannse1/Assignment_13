

import sqlite3
from sqlite3 import Error


def create_connections(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to  SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
        print(f"Please try another location")
        create_connections(input(">>"))

    return conn


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Querry executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_delete(connection, query):
    cursor = connection.cursor()
    try:
        connection.commit()
        sql_delete_query = """DELETE from SqliteDb_developers where id = 6"""
        cursor.execute(sql_delete_query)
        print("Record deleted successfully ")
        cursor.close()

    except Error as e:
        print(f"The error '{e}' occurred")



def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

