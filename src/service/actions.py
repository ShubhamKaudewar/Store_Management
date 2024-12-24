from src.dao import ProductManager, EmployeeManager


class Actions():
    def __init__(self):
        self.pm = ProductManager()
        self.emp = EmployeeManager()

    def get_all_product_list(self):
        details = self.pm.fetch_all_product_details()
        return details

    def get_all_employee_list(self):
        details = self.emp.fetch_all_employee_details()
        return details

    def update_product_price(self, data):
        operation = data.get('operation', 'single')
        if operation == 'single':
            model_id = data.get('model')
            new_price = data.get('price')
            result = self.pm.update_product_price_single(model_id, new_price)
            return result

    def create_new_product(self, name, model, price):
        self.pm.add_product(name, model, price)
        return "Success !"

    def check_employee_id(self, employee_id):
        name = self.emp.verify_employee_id(employee_id)
        if name:
            print(f'You are signed in {name}')
            return True
        return False

    def create_new_employee(self, firstname, surname, phone, address):
        employee_id = self.emp.add_employee(firstname, surname, phone, address)
        print(f'Welcome {firstname} {surname}, Here is your employee ID: {employee_id}')
        return "Success !"
