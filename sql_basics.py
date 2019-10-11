import sqlite3

# create name of database
database = 'Company.db'

# create connection to database
conn = sqlite3.connect(database)

# drop table if database already exists
conn.execute('''DROP TABLE IF EXISTS CUSTOMERS;''')

# create table with primary key, fields and datatypes
conn.execute('''CREATE TABLE CUSTOMERS
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT,
            DOB DATE NOT NULL);''')

# create command with tuples
myTuple = '''INSERT INTO CUSTOMERS (id, name, age, DOB) VALUES (?,?,?,?);'''

# create list of valuessql_basics.py
records_to_insert = [[2, 'Jon', 27, '2018-01-11'],
                     [3, 'Jane', 28, '2017-12-11'],
                     [4, 'Bill', 35, '2018-03-23'],
                     [5, 'Jon', 42, '2018-01-11'],
                     [6, 'Jane', 21, '2017-12-11']]

# execute command and insert list of values
conn.executemany(myTuple, records_to_insert)

# query database
record = conn.execute('SELECT id, name, age, DOB FROM CUSTOMERS')

# print results of query with formatting
for row in record:
    print('ID = ', row[0])
    print('NAME = ', row[1])
    print('AGE = ', row[2])
    print('DOB = ', row[3], '\n')

# commit changes to db
conn.commit()

# close connection
conn.close()
