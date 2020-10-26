import sqlite3
from random import randint as randint
import os.path
random_id_number = randint(1,1000000)

class Database():
    
    def createDatabase(self):
        if os.path.isfile('agenda.db'):
            connection = sqlite3.connect("agenda.db")
            print("DB already exists")
            connection.close()
        else:
            connection = sqlite3.connect("agenda.db")
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE contacts (id_number INTEGER, name TEXT, surname TEXT, phone TEXT, address TEXT, email TEXT, notes TEXT)")
            print("Created DB")
            connection.close()

    def getDatabase(self):
        connection = sqlite3.connect("agenda.db")
        cursor = connection.cursor()
        for row in cursor.execute('SELECT * FROM contacts ORDER BY id_number'):
            print(row)
        connection.close()

    def addRecordInDatabase(self,id_number,name,surname,phone,address,email,notes):
        data_tuple = (id_number,name,surname,phone,address,email,notes)
        insert_string = """INSERT INTO contacts (id_number, name, surname, phone,address,email,notes) VALUES (?,?,?,?,?,?,?)"""
        cursor.execute(insert_string, data_tuple)
        connection.commit()

        
    def updateDatabase():
        pass

