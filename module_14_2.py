import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


# Заполните 10 записями:
def add_data():
    insert_str = "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)"
    age_count = 10
    for i in range(1, 11):
        insert_data = (f"User{i}", f"example{i}@gmail.com", age_count, 1000)
        age_count += 10
        cursor.execute(insert_str, insert_data)
    connection.commit()


# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
def update_base():
    update_str = "UPDATE Users SET balance = ? WHERE id = 1 OR ID % 2"
    update_data = (500,)
    cursor.execute(update_str, update_data)


# Удалите каждую 3ую запись в таблице начиная с 1ой:
def del_3rd():
    delete_str = "DELETE FROM Users WHERE id % 3 = 1"
    cursor.execute(delete_str)


# Сделайте выборку всех записей при помощи fetchall()
def list_db():
    list_info = "SELECT username, email, age, balance FROM Users WHERE age != ?"
    list_data = (60,)
    cursor.execute(list_info, list_data)
    users = cursor.fetchall()
    for user in users:
        print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} |  Баланс: {user[3]}')


def del_id6():
    delete_str = "DELETE FROM Users WHERE id  = 6"
    cursor.execute(delete_str)


def sum_records():
    total_str = "SELECT COUNT (*) FROM Users"
    cursor.execute(total_str)
    total_users = cursor.fetchone()[0]
    print('Общее кол-во пользователей : ', total_users)


def sum_balances():
    all_balances_str = "SELECT SUM(balance) FROM Users"
    cursor.execute(all_balances_str)
    all_balance = cursor.fetchone()[0]
    print('Общий баланс:  ', all_balance)


def aver_balance():
    total_str = "SELECT COUNT (*) FROM Users"
    cursor.execute(total_str)
    total_users = cursor.fetchone()[0]
    all_balances_str = "SELECT SUM(balance) FROM Users"
    cursor.execute(all_balances_str)
    all_balance = cursor.fetchone()[0]
    print('Средний баланс : ', all_balance / total_users)


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

#  - - - - - - - - - - -  задачи за предидущего ДЗ 14_1

# Заполните её 10 записями:
# add_data()

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# update_base()

# Удалите каждую 3ую запись в таблице начиная с 1ой:
# del_3rd()

# Сделайте выборку всех записей при помощи fetchall()
# list_db()


#  - - - - - - - - - - - задачи за предидущего ДЗ 14_2

# Удалите из базы данных not_telegram.db запись с id = 6.
# del_id6()

# Подсчитать общее количество записей.
sum_records()

# Посчитать сумму всех балансов
sum_balances()

# Вывести в консоль средний баланс всех пользователей.
aver_balance()

connection.commit()
connection.close()
