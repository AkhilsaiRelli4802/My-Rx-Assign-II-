# Design an immutable class with following attributes 
# String name; 
# String Id, 
# Date dateOfJoining 
# List<Address> addresses; 

from datetime import date
from typing import List

class Address:
    def __init__(self, street: str, city: str, zip_code: str):
        self._street = street
        self._city = city
        self._zip_code = zip_code

    @property
    def street(self):
        return self._street

    @property
    def city(self):
        return self._city

    @property
    def zip_code(self):
        return self._zip_code

    def __repr__(self):
        return f"Address(street='{self._street}', city='{self._city}', zip_code='{self._zip_code}')"

class Employee:
    def __init__(self, name: str, emp_id: str, date_of_joining: date, addresses: List[Address]):
       
        self._name = name
        self._emp_id = emp_id
        self._date_of_joining = date_of_joining
   
        self._addresses = [Address(addr.street, addr.city, addr.zip_code) for addr in addresses]


    @property
    def name(self):
        return self._name

    @property
    def emp_id(self):
        return self._emp_id

    @property
    def date_of_joining(self):
        return self._date_of_joining

    @property
    def addresses(self):
        return [Address(addr.street, addr.city, addr.zip_code) for addr in self._addresses]

    def __repr__(self):
        return f"Employee(name='{self._name}', emp_id='{self._emp_id}', date_of_joining='{self._date_of_joining}', addresses={self._addresses})"

address1 = Address("1234 Elm St", "Springfield", "12345")
address2 = Address("5678 Oak St", "Shelbyville", "67890")
employee = Employee("John Doe", "E123", date(2020, 5, 15), [address1, address2])

print(employee)


