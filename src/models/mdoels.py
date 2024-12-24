from dataclasses import dataclass

# Define the dataclasses
@dataclass
class Employee:
    id: int
    employee_id: int
    firstname: str
    surname: str
    phone: str
    address: str

@dataclass
class Product:
    id: int
    name: str
    model: str
    price: int

