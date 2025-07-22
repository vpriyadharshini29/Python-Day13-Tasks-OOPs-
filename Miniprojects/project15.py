# Base class
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Full-time employee subclass
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

# Part-time employee subclass
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Payroll class to calculate total salary and apply tax
class Payroll:
    @staticmethod
    def calculate_tax(salary):
        return salary * 0.1  # 10% tax

    @staticmethod
    def generate_payroll(employee):
        salary = employee.calculate_salary()
        tax = Payroll.calculate_tax(salary)
        net_salary = salary - tax
        print(f"Payroll for {employee.name} (ID: {employee.emp_id})")
        print(f"Gross Salary: ₹{salary}")
        print(f"Tax Deducted: ₹{tax}")
        print(f"Net Salary: ₹{net_salary}\n")

# Example usage
emp1 = FullTimeEmployee(101, "John", 50000)
emp2 = PartTimeEmployee(102, "Doe", 200, 80)

Payroll.generate_payroll(emp1)
Payroll.generate_payroll(emp2)
