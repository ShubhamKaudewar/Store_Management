from src.service.actions import Actions

def do_action(action_id):
    if action_id == 1:
        return Actions().get_all_product_list()
    elif action_id == 2:
        employee_id = int(input("Provide your employee id: "))

        # employee_id = 1234567890
        verified = Actions().check_employee_id(employee_id)
        if not verified:
            return "You don't have access to perform this action."

        model = str(input("Enter the product model: "))
        new_price = int(input("Enter the new price: "))
        # model = "QN65Q800TAFXZA"
        # new_price = 78000
        data = {"model": model, "price": new_price}
        return Actions().update_product_price(data)
    elif action_id == 3:
        firstname = str(input("Enter firstname: "))
        surname = str(input("Enter surname: "))
        phone = str(input("Enter phone: "))
        address = str(input("Enter address: "))
        # firstname = "Ray"
        # surname = "last"
        # phone = "+91-898978593"
        # address = "ABS, CIG, USA"
        return Actions().create_new_employee(firstname, surname, phone, address)
    elif action_id == 4:
        name = str(input("Enter product name: "))
        model = str(input("Enter product model: "))
        price = int(input("Enter product price: "))
        # name = "Mobile"
        # model = "iPhone"
        # price = 67000
        return Actions().create_new_product(name, model, price)
    elif action_id == 5:
        return Actions().get_all_employee_list()
    else:
        return "Wrong action ID provided"

def main():
    print("Hello from shopping-mall!")
    while True:
        print("What do you want to do? Provide number")
        print("1. List all product details")
        print("2. Update Price")
        print("3. Add Employee")
        print("4. Add Product")
        print("5. List all employee details")
        print("6. Exit Store")
        action_id = int(input("Provide Action ID: "))
        # action_id = 4
        if action_id == 6:
            break
        print(do_action(action_id))
        input("Press Anykey to continue...")
    print("Thank you for using Store Management!")

if __name__ == "__main__":
    main()
