import pandas as pd

# Read CSV file
df = pd.read_csv("employee.csv")

print("Employee Data:\n")
print(df)

# (a) Print list of employees working in "Automotive" domain
print("\n(a) Employees working in Automotive domain:\n")
automotive_employees = df[df["Domain"] == "Automotive"]
print(automotive_employees)

# (b) Print details of an employee using Employee ID
emp_id = int(input("\nEnter Employee ID to search: "))

employee_details = df[df["Employee ID"] == emp_id]

if not employee_details.empty:
    print("\n(b) Employee Details:\n")
    print(employee_details)
else:
    print("\nEmployee not found!")

# (d) Print list of all Developers of Infosys
print("\n(d) List of all Developers of Infosys:\n")
infosys_developers = df[(df["Company"] == "Infosys") & (df["Designation"] == "Developer")]
print(infosys_developers)