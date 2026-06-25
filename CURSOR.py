import sqlite3

def start():
    connection = sqlite3.connect('wickets.db')
    return connection

def stop(connection):
    connection.commit()
    connection.close()

def define_cursor(connection):
    return connection.cursor()



