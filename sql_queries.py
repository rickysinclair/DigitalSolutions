import sqlite3

# select database
database = "world.db"

# establish connect to database
conn = sqlite3.connect(database)

# create cursor
cur = conn.cursor()

# user input for selected field queries
p1 = input("First field: ")
p2 = input("Second field: ")

# format for multiple selections
para1 = p1
para2 = ", " + p2

# execute command with format
cur.execute("SELECT {0} {1} FROM Country".format(para1, para2))

# display all results
for rows in cur.fetchall():
    print(rows)

# close connection
conn.close()
