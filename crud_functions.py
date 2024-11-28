import sqlite3

connection = sqlite3.connect("products.db")
cursor = connection.cursor()


def get_all_products():
    cursor.execute("SELECT title, description, price FROM Products")
    result = cursor.fetchall()
    print(result)
    return result


def intiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        );
    ''')
    connection.commit()

def add_data():
    price = 100
    for i in range(1,11):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f"Продукт-{i}",
                                                                                             f"Описание-{i}", price))
        price += 100
    connection.commit()

intiate_db()
#add_data()
#get_all_products()

#connection.close()
