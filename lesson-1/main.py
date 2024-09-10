import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  age INTEGER NOT NULL, 
                  grade REAL NOT NULL)''')

# cursor.execute("INSERT INTO users (name, age, grade) VALUES(?, ?, ?)", ('Charlie', 19, 2.3))
action = input('Your action: ')

if action == 'add':
  name = input("name: ")
  age = int(input("age: "))
  grade = int(input("grade: "))
  cursor.execute("INSERT INTO users (name, age, grade) VALUES(?, ?, ?)", (name, age, grade))
elif action == 'change':
  name = input("name: ")
  grade = int(input("grade: "))
  cursor.execute("UPDATE users SET grade = ? WHERE name = ?", (grade, name))
elif action == 'delete':
  ask_id = int(input('student ID: '))
  cursor.execute("DELETE from users WHERE id = ?", (ask_id,))
elif action == 'greater 20':
  cursor.execute("SELECT * FROM users WHERE age > ?", (20,))

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
  print(f"ID: {row[0]} name: {row[1]} age: {row[2]} grade: {row[3]}")

conn.close()