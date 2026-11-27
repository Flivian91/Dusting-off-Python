class Employee:
    # Class attributes
    company_name = "Tech Solutions"
    tax_rate = 0.10
    total_employees = 0

    def __init__(self, employee_id, name, salary, department, is_active=True):
        # Validate salary before initializing attributes
        if salary < 0:
            raise ValueError("Salary cannot be negative")

        # Instance attributes
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department
        self.is_active = is_active

        # Increment counter after successful validation
        Employee.total_employees += 1

    def display_info(self):
        """Return formatted employee information."""
        return (
            f"Company: {self.company_name}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Employee Name: {self.name}\n"
            f"Salary: KES {self.salary:,.2f}\n"
            f"Department: {self.department}\n"
            f"Active: {self.is_active}\n"
        )

    def calculate_tax(self):
        """Calculate monthly income tax."""
        return self.salary * Employee.tax_rate

    def calculate_net_salary(self):
        """Calculate monthly salary after tax."""
        return self.salary - self.calculate_tax()

    def calculate_annual_salary(self):
        """Calculate annual gross salary."""
        return self.salary * 12

    def give_raise(self, percentage=5):
        """Increase the employee's gross salary."""
        if percentage < 0:
            raise ValueError("Raise percentage cannot be negative")

        self.salary *= 1 + percentage / 100

    def deactivate(self):
        """Deactivate the employee."""
        self.is_active = False


# ==========================================
# APPLICATION FUNCTIONS
# ==========================================

def apply_department_raise(employees, department, percentage=5):
    """Apply a salary raise to active employees in a department."""

    if percentage < 0:
        raise ValueError("Raise percentage cannot be negative")

    for employee in employees:
        if employee.is_active and employee.department == department:
            employee.give_raise(percentage)


def calculate_total_payroll(employees):
    """Calculate the gross payroll of active employees."""
    return sum(
        employee.salary
        for employee in employees
        if employee.is_active
    )


# ==========================================
# CREATE EMPLOYEE OBJECTS
# ==========================================

employees = [
    Employee(101, "Alex", 50000, "IT"),
    Employee(102, "Mary", 65000, "Finance"),
    Employee(103, "John", 45000, "IT", False),
    Employee(104, "Sarah", 80000, "Management"),
    Employee(105, "David", 40000, "Support")
]


# ==========================================
# PROCESS EMPLOYEE DATA
# ==========================================

print("=== EMPLOYEE PAYROLL SYSTEM ===")

# Total employees created
print(f"\nTotal employees: {Employee.total_employees}")

# Filter active employees
active_employees = list(
    filter(lambda employee: employee.is_active, employees)
)

# Extract active employee names
active_employee_names = [
    employee.name for employee in active_employees
]

print(f"\nActive employees: {active_employee_names}")

# Map employee names to net salaries
active_employee_salary_lookup = {
    employee.name: round(employee.calculate_net_salary(), 2)
    for employee in active_employees
}

print("\nNet salaries before raises:")

for name, salary in active_employee_salary_lookup.items():
    print(f"{name}: KES {salary:,.2f}")

# Calculate gross monthly payroll
total_monthly_payroll = calculate_total_payroll(employees)

print(f"\nGross payroll: KES {total_monthly_payroll:,.2f}")

# Extract unique departments
departments = {
    employee.department for employee in employees
}

print(f"\nDepartments: {departments}")

# Sort active employees by salary in descending order
sorted_employee_names = [
    employee.name
    for employee in sorted(
        active_employees,
        key=lambda employee: employee.salary,
        reverse=True
    )
]

print(f"\nEmployees sorted by salary: {sorted_employee_names}")


# ==========================================
# APPLY DEPARTMENT SALARY RAISES
# ==========================================

print("\n=== SALARY INCREMENT ===")

# Give active IT employees a 10% raise
apply_department_raise(employees, "IT", 10)

# Display updated gross salaries
for employee in employees:
    print(f"{employee.name}: KES {employee.salary:,.2f}")

# Recalculate gross payroll after salary changes
updated_payroll = calculate_total_payroll(employees)

print(f"\nPrevious payroll: KES {total_monthly_payroll:,.2f}")
print(f"Updated payroll: KES {updated_payroll:,.2f}")

# Calculate payroll difference
payroll_difference = updated_payroll - total_monthly_payroll

print(f"Payroll increase: KES {payroll_difference:,.2f}")

# Recalculate net salaries after raises
updated_net_salaries = {
    employee.name: round(employee.calculate_net_salary(), 2)
    for employee in active_employees
}

print("\nUpdated net salaries:")

for name, salary in updated_net_salaries.items():
    print(f"{name}: KES {salary:,.2f}")


# ==========================================
# TEST SHARED CLASS ATTRIBUTES
# ==========================================

print("\n=== TAX RATE UPDATE ===")

Employee.tax_rate = 0.15

print(f"New tax rate: {Employee.tax_rate:.0%}")

for employee in active_employees:
    print(
        f"{employee.name}: "
        f"KES {employee.calculate_net_salary():,.2f}"
    )

# Restore original tax rate
Employee.tax_rate = 0.10


# ==========================================
# TEST EXCEPTION HANDLING
# ==========================================

print("\n=== VALIDATION TESTS ===")

# Test invalid employee creation
try:
    invalid_employee = Employee(106, "Peter", -5000, "IT")

except ValueError as error:
    print(f"Employee creation failed: {error}")

# Confirm invalid employee was not counted
print(f"Total employees: {Employee.total_employees}")

# Test invalid salary raise
try:
    employees[0].give_raise(-10)

except ValueError as error:
    print(f"Salary increment failed: {error}")

# Confirm salary was not modified
print(f"Alex's salary: KES {employees[0].salary:,.2f}")


# ==========================================
# DISPLAY EMPLOYEE INFORMATION
# ==========================================

print("\n=== EMPLOYEE DETAILS ===")

for employee in employees:
    print(employee.display_info())