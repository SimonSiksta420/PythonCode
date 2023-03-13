DATABASE = 'database.db'

import os, sqlite3

conn = sqlite3.connect('example.db')

conn.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             email TEXT NOT NULL,
             age INTEGER);''')

conn.execute("INSERT INTO users (name, email, age) VALUES ('John', 'john@example.com', 30)")
conn.execute("INSERT INTO users (name, email, age) VALUES ('Jane', 'jane@example.com', 25)")

conn.commit()

cursor = conn.execute("SELECT * FROM users")
for row in cursor:
    print(row)

conn.close()