import sqlite3

DB_NAME = "orders.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        restaurant TEXT,
        food TEXT,
        quantity INTEGER,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_order(order_id, user_id, restaurant, food, quantity):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?)",
        (order_id, user_id, restaurant, food, quantity, "pending")
    )

    conn.commit()
    conn.close()


def update_status(order_id, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE orders SET status=? WHERE id=?",
        (status, order_id)
    )

    conn.commit()
    conn.close()
def get_orders():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders ORDER BY id DESC")

    orders = cursor.fetchall()

    conn.close()

    return orders