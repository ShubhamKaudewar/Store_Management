from .db_connection import create_connection, create_tables
from src.models import Product, Employee
from dataclasses import asdict
from json import dumps
from tabulate import tabulate
import pprint as pp


# Create tables if they don't exist
create_tables()

class EmployeeManager:
    def __init__(self):
        self.conn = create_connection()
        self.cursor = self.conn.cursor()

    def fetch_all_employee_details(self):
        self.cursor.execute('SELECT * FROM employees')
        try:
            employees = self.cursor.fetchall()
            employee_list = [Employee(*employee) for employee in employees]

            # Prepare data and headers for tabulate
            headers = list(Employee.__annotations__.keys())
            data = [[getattr(emp, field) for field in headers if field != "employee_id"] for emp in employee_list]
            print(tabulate(data, headers=headers, tablefmt="grid"))
            return "Success"

        except Exception as e:
            print(str(e))
            self.cursor.rollback()
        self.cursor.close()

    def add_employee(self, firstname, surname, phone, address):
        import time
        employee_id = int(round(time.time() * 10))
        self.cursor.execute(
            'INSERT INTO employees (employee_id, firstname, surname, phone, address) '
            'VALUES (?, ?, ?, ?, ?)',
            (employee_id, firstname, surname, phone, address))
        self.conn.commit()

        try:
            self.cursor.execute('''SELECT * FROM employees WHERE employee_id = ?''', (employee_id,))
            employee_obj = self.cursor.fetchone()
            employee = Employee(*employee_obj)

            # Prepare data and headers for tabulate
            headers = list(Employee.__annotations__.keys())
            data = [[getattr(emp, field) for field in headers] for emp in [employee]]
            print(tabulate(data, headers=headers, tablefmt="grid"))
            return employee_id

        except Exception as e:
            print(str(e))
            self.cursor.rollback()
        self.cursor.close()


    def verify_employee_id(self, employee_id):
        self.cursor.execute('SELECT * FROM employees WHERE employee_id = ?', (employee_id,))
        employee_obj = self.cursor.fetchone()
        if not employee_obj:
            return False
        employee = Employee(*employee_obj)
        return employee.firstname

    def close_connection(self):
        self.conn.close()


class ProductManager:
    def __init__(self):
        self.conn = create_connection()
        self.cursor = self.conn.cursor()

    def fetch_all_product_details(self):
        self.cursor.execute('SELECT * FROM products')
        try:
            products = self.cursor.fetchall()
            product_list = [Product(*product) for product in products]

            # Prepare data and headers for tabulate
            headers = list(Product.__annotations__.keys())
            data = [[getattr(prod, field) for field in headers] for prod in product_list]
            print(tabulate(data, headers=headers, tablefmt="grid"))
            return "Success"

        except Exception as e:
            print(str(e))
            self.cursor.rollback()
        self.cursor.close()


    def add_product(self, name, model, price):
        self.cursor.execute(
            'INSERT INTO products (name, model, price) '
            'VALUES (?, ?, ?)',
            (name, model, price))
        self.conn.commit()

        try:
            return_id = self.cursor.lastrowid
            self.cursor.execute('''SELECT * FROM products WHERE id = ?''', (return_id,))
            product_obj = self.cursor.fetchone()
            product = Product(*product_obj)

            # Prepare data Product headers for tabulate
            headers = list(Product.__annotations__.keys())
            data = [[getattr(prod, field) for field in headers] for prod in [product]]
            print(tabulate(data, headers=headers, tablefmt="grid"))
            return

        except Exception as e:
            print(str(e))
            self.cursor.rollback()
        self.cursor.close()


    def update_product_price_single(self, model_id, new_price):
        x = self.cursor.execute('''UPDATE products SET price = ? WHERE model = ?''', (new_price, model_id))
        try:
            self.conn.commit()
            self.cursor.execute('''SELECT * FROM products WHERE model = ?''', (model_id,))
            product_obj = self.cursor.fetchone()
            product = Product(*product_obj)

            # Prepare data and headers for tabulate
            headers = list(Product.__annotations__.keys())
            data = [[getattr(prod, field) for field in headers] for prod in [product]]
            print(tabulate(data, headers=headers, tablefmt="grid"))

            return "Success"
        except Exception as e:
            print(str(e))
            self.cursor.rollback()
        self.cursor.close()