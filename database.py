import sqlite3
from random import randint as randint
import os.path

class Database():
    
    random_id_number = randint(1,1000000)
    random_id_number_tupple = (random_id_number,)
    #random_id_number = 654721
    #random_id_number_tupple = (654721,)
    def randomizeNumber(self):
        connection = sqlite3.connect("agenda.db")
        cursor = connection.cursor()
        
        
        #checking that no other contact shares the username of the contact about to be created:
        a = cursor.execute('SELECT * FROM contacts WHERE id_number=?', (self.random_id_number_tupple))
        rows = cursor.fetchall() 
        if rows:
            print("This number already exists")
            self.random_id_number = randint(1,1000000)
            self.random_id_number_tupple = (self.random_id_number,)
            self.randomizeNumber()
            print("We did something")
            print(self.random_id_number,self.random_id_number_tupple)

        else:
            print("Random number for ID does not exist")
            pass
        

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
        #for row in cursor.execute('SELECT * FROM contacts ORDER BY id_number'):
        #    print(row)
        cursor.execute('SELECT * FROM contacts ORDER BY name')
        records = cursor.fetchall()
        return records
        connection.close()
        

    def addRecordInDatabase(self,name,surname,phone,address,email,notes):
        connection = sqlite3.connect("agenda.db")
        cursor = connection.cursor()
        
        data_tuple = (self.random_id_number,name,surname,phone,address,email,notes)
        insert_string = """INSERT INTO contacts (id_number, name, surname, phone,address,email,notes) VALUES (?,?,?,?,?,?,?)"""
        cursor.execute(insert_string, data_tuple)
        connection.commit()
        connection.close()

    def deleteRecordInDatabase(self,id_number):
        connection = sqlite3.connect("agenda.db")
        cursor = connection.cursor()
        
        data_tuple = (id_number)
        delete_string = """DELETE FROM contacts WHERE id_number=?"""
        print("successfully deleted %s" % (id_number))
    
    def retrieveIdNumber(self,name):
        connection = sqlite3.connect("agenda.db")
        cursor = connection.cursor()
        data_tuple = [name]
        retrieve_string = """SELECT * FROM contacts WHERE name=?"""
        cursor.execute(retrieve_string,data_tuple)
        records = cursor.fetchall()
        return records
        connection.close()

    def retrieveName(self,id_number):
        connection = sqlite3.connect("agenda.db")
        cursor = connection.cursor()
        data_tuple = [id_number]
        retrieve_string = """SELECT * FROM contacts WHERE id_number=?"""
        cursor.execute(retrieve_string,data_tuple)
        records = cursor.fetchall()
        return records
        connection.close()

    def retrieveContact(self,name):
        connection = sqlite3.connect("agenda.db")
        cursor = connection.cursor()
        data_tuple = [name]
        retrieve_string = """SELECT * FROM contacts WHERE name=?"""
        cursor.execute(retrieve_string,data_tuple)
        records = cursor.fetchall()
        return records
        connection.close()






