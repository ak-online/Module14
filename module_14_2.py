import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

""" 
указываем шаблоны  для строковых переменных для использования далее 
"""
total_str = "SELECT COUNT (*) FROM Users"
all_balances_str = "SELECT SUM(balance) FROM Users"

# Удалите из базы данных not_telegram.db запись с id = 6. :
cursor.execute(delete_str)

# Подсчёт кол-ва всех пользователей
cursor.execute(total_str)
total_users = cursor.fetchone()[0]
print(total_users)

# Подсчёт суммы всех балансов
cursor.execute(all_balances_str)
all_balance = cursor.fetchone()[0]
print(all_balance)

# среднее
print(all_balance/total_users)

connection.commit()
connection.close()