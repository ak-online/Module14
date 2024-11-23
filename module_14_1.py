import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

""" 
указываем шаблоны  для строковых переменных для использования далее 
"""
insert_str = "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)"

update_str = "UPDATE Users SET balance = ? WHERE id = 1 OR ID % 2"
update_data = (500,)

delete_str = "DELETE FROM Users WHERE id % 3 = 1"

list_info = "SELECT username, email, age, balance FROM Users WHERE age != ?"
list_data = (60,)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Заполните 10 записями:
age_count = 10
for i in range(1, 11):
      insert_data = (f"User{i}", f"example{i}@gmail.com", age_count, 1000)
      age_count += 10
      cursor.execute(insert_str, insert_data)


# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
cursor.execute(update_str, update_data)

# Удалите каждую 3ую запись в таблице начиная с 1ой:
cursor.execute(delete_str)

# Сделайте выборку всех записей при помощи fetchall()
cursor.execute(list_info, list_data)
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} |  Баланс: {user[3]}')

connection.commit()
connection.close()