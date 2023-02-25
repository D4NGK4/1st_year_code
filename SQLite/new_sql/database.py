import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#create a table
#c.execute("""CREATE TABLE customers (
#    Fname text,
#    Lname text,
#    Email text
#)""")

#Datatypes --->
#NULL
#INTEGER
#REAL(Decimal)
#TEXT
#BLOB(images, files)
# <----

#c.execute("INSERT INTO customers VALUES('Dan Joshua', 'Tagaan', 'tagaan@gmail.com')")

#lstof_customers = [
#('EJ','Duallo', 'EJ@gmail.com'),
#('Ken', 'Navares','KN@gmail.com'),
#('Kent', 'Organiza', 'KO@gmail.com'),
#('Joshua','Valmoria','JoshVal@gmail.com')]

#c.executemany("INSERT INTO customers VALUES (?,?,?)", lstof_customers)



c.execute("SELECT * FROM customers")
#print(c.fetchone())
#print(c.fetchone()[0])
#print(c.fetchall())

items = c.fetchall()

for item in items:
    #print(item)
    print(item[0] + " " + item[1] + "\t" + item[2])





print("Command executed succesfully!")

#commit command
conn.commit()

#close connection
conn.close()