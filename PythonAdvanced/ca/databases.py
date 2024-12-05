import sqlite3


connection = sqlite3.connect('student.db')

cursor = connection.cursor()

# cursor.execute('''
#                CREATE TABLE student (
#                id INTEGER,
#                name TEXT,
#                classification TEXT,
#                gpa REAL)
#                '''
#                )

# rows = [
#     (1, 'Tobi', 'Freshman', 4.0),
#     (2, 'Victor', 'Sophomore', 3.5),
#     (3, 'Mike', 'Junior', 2.0),
#     (4, 'John', 'Senior', 3.0)
# ]
# cursor.execute('''
#                 INSERT INTO student VALUES (0, 'Jane', 'Junior', 2.5)
#                ''')

# cursor.executemany('''INSERT INTO student VALUES (?,?,?,?)''', rows)
all_rows = cursor.execute('''SELECT name,gpa FROM student''').fetchall()
print(all_rows)