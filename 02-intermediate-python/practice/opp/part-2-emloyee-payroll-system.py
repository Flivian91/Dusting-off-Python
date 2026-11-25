class Employee:
    # Class attributes
    company_name = "Tech Solutions"
    tax_rate = 0.10
    total_employees = 0
    
    def __init__(self, employee_id, name, salary, department, is_active=True):
        # Instance attributes
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")
        self.department = department
        self.is_active = is_active

        # Increment total employees
        Employee.total_employees += 1
        
        # Methods
    def display_info(self):
        return f"Employee ID: {self.employee_id}\nEmployee Name: {self.name}\nSalary: {self.salary}\nDepartment: {self.department}\nActive: {self.is_active}\n"
    
    def calculate_tax(self):
        return self.salary * Employee.tax_rate
    
    def calculate_net_salary(self):
        return self.salary - self.calculate_tax()
    
    def calculate_annual_salary(self):
        return self.salary * 12
    
    def give_raise(self, raise_rate=5):
        self.salary = self.salary * (1 + raise_rate/100 )
        if self.is_active and self.department == "IT":
            self.salary = self.salary * 1.1
        
    def deactivate(self):
        self.is_active = False

# List of Objects
employees = [
    Employee(101, "Alex", 50000, "IT", True),
    Employee(102, "Mary", 65000, "Finance", True),
    Employee(103, "John", 45000, "IT", False),
    Employee(104, "Sarah", 80000, "Management", True),
    Employee(105, "David", 40000, "Support", True)
]
# e1 = Employee(101, "Alex", 50000, "IT", True)
# e1.give_raise()
# print(e1.salary)

# Test shared attributes(confirmed)
# Employee.tax_rate = 0.15

# Process employee data
# Active employees
active_employees = list(filter(lambda employee: employee.is_active, employees))

# active employees names
active_employee_names = [employee.name for employee in active_employees]
# print(active_employee_names)

# active employee mapped with salary
active_employee_salary_lookup = {employee.name: employee.calculate_net_salary() for employee in active_employees}
# print(active_employee_salary_lookup)

# Gross payroll
total_monthly_payroll = sum(employee.salary for employee in active_employees)
print(total_monthly_payroll)

# get all departments
departments = {employee.department for employee in employees}
# print(departments)

# Sort employees by salary
sorted_employee_names = list(employee.name for employee in sorted(active_employees, key=lambda employee: employee.salary, reverse=True))
# print(sorted_employee_names)