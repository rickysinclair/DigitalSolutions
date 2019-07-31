import sqlite3

from guizero import App, TextBox, PushButton

# select database
database = "world.db"

# establish connect to database
conn = sqlite3.connect(database)

# create cursor
cur = conn.cursor()


def query():
    """
    This function executes a SQL query based upon user input into text boxes
    and display ALL results into a separate textbox.
    """
    # assign values from text boxes to variables used as positional arguments
    f0 = field1.value + ", "
    f1 = field2.value

    # execute query using positional arguments
    cur.execute("SELECT {0} {1} FROM Country".format(f0, f1))

    # fetch all results and append to text box
    for rows in cur.fetchall():
        text.append(rows)


# create App
app = App()

# display field text boxes
field1 = TextBox(app)
field2 = TextBox(app)

# display button and call query function
button = PushButton(app, command=query)

# display results text box
text = TextBox(app, width=300, height=300, multiline=True, scrollbar=True)

# display app window
app.display()

# close connection
conn.close()
