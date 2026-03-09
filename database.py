import sqlite3


def init_db():

    conn = sqlite3.connect("orders.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        restaurant TEXT,
        food TEXT,
        quantity TEXT,
        type TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_order(user_id,restaurant,food,quantity,type):

    conn = sqlite3.connect("orders.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO orders(user_id,restaurant,food,quantity,type) VALUES(?,?,?,?,?)",
        (user_id,restaurant,food,quantity,type)
    )

    conn.commit()

    order_id = cur.lastrowid

    conn.close()

    return order_id


def get_user(order_id):

    conn = sqlite3.connect("orders.db")
    cur = conn.cursor()

    cur.execute("SELECT user_id FROM orders WHERE id=?",(order_id,))
    user=cur.fetchone()

    conn.close()

    return user[0]