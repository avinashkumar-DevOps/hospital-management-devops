import mysql.connector

def get_db_connection():

    connection = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="hospital"
    )

    return connection