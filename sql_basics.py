import sqlite3

conn = sqlite3.connect('Company.db')

conn.execute('''DROP TABLE IF EXISTS CUSTOMERS;''')

conn.execute('''CREATE TABLE CUSTOMERS
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT,
            DOB DATE NOT NULL);''')

myTuple = """INSERT INTO CUSTOMERS (id, name, age, DOB) VALUES (?,?,?,?)""";

records_to_insert = [[2, 'Jon', 27, '2018-01-11'],
                     [3, 'Jane', 28, '2017-12-11'],
                     [4, 'Bill', 35, '2018-03-23'],
                     [5, 'Jon', 42, '2018-01-11'],
                     [6, 'Jane', 21, '2017-12-11']]

conn.executemany(myTuple, records_to_insert)

record = conn.execute("SELECT id, name, age, DOB FROM CUSTOMERS")

for row in record:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("DOB = ", row[3], '\n')

conn.close()
