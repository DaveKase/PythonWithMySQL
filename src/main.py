'''
Created on 7. juuni 2019

@author: Taavi Kase
'''
#cwd = os.getcwd()
#print(cwd)

import mysql.connector
import os

os.chdir('..\\..')
contents = [line.rstrip('\n') for line in open('db.txt')]

hostName = contents[0]
userName = contents[1]
pwd = contents[2]
pyDb = contents[3]

mydb = mysql.connector.connect(host=hostName, user=userName, passwd=pwd, database=pyDb)

#mycursor = mydb.cursor()

mycursor = mydb.cursor(buffered=True)

#mycursor.execute("CREATE DATABASE pyTestDb") # Already had that db
#mycursor.execute("SHOW DATABASES")

'''
for db in mycursor:
    print(db)
'''

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") # Already exists
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") # Already done

"""
Did this already
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
name = "John"
address = "Highway 21"
val = (name, address)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")



sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

"""

mycursor.execute("SELECT * FROM customers")
results = mycursor.fetchall()

for result in results:
    print(result)

mycursor.execute("SELECT name, address FROM customers")
results = mycursor.fetchall()

for result in results:
    print(result)

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()

print() # Printing empty line
print(myresult)
print()

# Preventing SQL injections
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(type(x))
    print(x)

print()
print()

