class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class FullTimeEmployee(Employee):
    def __init__(self, name, salary, benefits):
        super().__init__(name, salary)
        self.benefits = benefits

    def display_info(self):
        super().display_info()
        print(f"Benefits: {self.benefits}")

class ContractEmployee(Employee):
    def __init__(self, name, salary, contract_duration):
        super().__init__(name, salary)
        self.contract_duration = contract_duration

    def display_info(self):
        super().display_info()
        print(f"Contract Duration: {self.contract_duration}")



employee1 = FullTimeEmployee("Alice", 60000, "Health insurance, Paid time off")
employee2 = ContractEmployee("Bob", 40000, "6 months")

employee1.display_info()
print("-------------------------------------")
employee2.display_info()