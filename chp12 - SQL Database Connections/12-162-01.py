import sqlite3

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    people_values = (
        ('Ron', 'Obvious', 42),
        ('Luigi', 'Vercotti', 43),
        ('Arthur', 'Belling', 28),
    )
    c.executescript("""
        DROP TABLE IF EXISTS People;
        CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
        """)
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)
