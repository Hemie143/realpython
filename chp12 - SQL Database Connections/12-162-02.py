import sqlite3

# get person data from user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

# execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People Values('" + first_name + "', '" + last_name + "', " + str(age) + ")"
    c.execute(line)