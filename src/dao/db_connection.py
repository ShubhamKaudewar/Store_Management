import sqlite3


def create_connection():
    conn = sqlite3.connect('store.db')
    return conn


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Create the employees table
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        employee_id INTEGER,
                        firstname TEXT,
                        surname TEXT,
                        phone TEXT,
                        address TEXT
                    )''')

    # Create the products table
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        model TEXT,
                        price INTEGER
                    )''')

    # Check if products table is empty
    cursor.execute('SELECT COUNT(*) FROM products')
    if cursor.fetchone()[0] == 0:  # No records in the table
        products = [
            ('TV', 'QN65Q800TAFXZA', 78000),
            ('TV', 'UN55NU8000FXZA', 85000),
            ('TV', 'QN75Q90TAFXZA', 95000),
            ('TV', 'UN43TU8000FXZA', 345)
        ]
        cursor.executemany('INSERT INTO products (name, model, price) VALUES (?, ?, ?)', products)

    # Check if employees table is empty
    cursor.execute('SELECT COUNT(*) FROM employees')
    if cursor.fetchone()[0] == 0:  # No records in the table
        employees = [(1852853323, 'Ray', 'last', '+91-898978593', 'ABS, CIG, USA')]
        cursor.executemany('INSERT INTO employees (employee_id, firstname, surname, phone, address) VALUES (?, ?, ?, ?, ?)', employees)

    conn.commit()
    conn.close()


# Create tables and populate with sample data (if empty)
create_tables()
