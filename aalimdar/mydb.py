import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Asad@169'
)

cursorObject = database.cursor()

cursorObject.execute('CREATE DATABASE aalimdar_database')

print('All done')

