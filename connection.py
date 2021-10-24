import mysql.connector

def connect(host, user, password, database):
    connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()
    try:
        cursor.execute('USE internship_portal')
        print("Conected to database")
        return cursor
    except:
        print("Error while connecting")

