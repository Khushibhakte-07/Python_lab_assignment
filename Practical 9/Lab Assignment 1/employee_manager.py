class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0.0
        self.address = ""

    def get_data(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.address = input("Enter Address: ")
        self.salary = float(input("Enter Salary: "))

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)
        print("Salary:", self.salary)


class Manager(Employee):
    pass   # Inherits everything from Employee


# Main program
managers = []

for i in range(10):
    print(f"\nEnter details of Manager {i+1}")
    m = Manager()
    m.get_data()
    managers.append(m)

print("\nManager Details:")
for i, m in enumerate(managers, start=1):
    print(f"\nManager {i}")
    m.display()