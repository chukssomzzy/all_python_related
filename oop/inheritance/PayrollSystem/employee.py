class Employee():
    """Defines an abstract class Employee"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    """Implements the SalaryEmployee subclass that derives from Employee"""

    def __init__(self, id, name, weekly_salary):
        """Calls the __init__ with id and name and defines the weekly_salary

        Args:
            id: unique int or string
            name (str): name of employee
            weekly_salary (int): employee weekly salary
        """
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        """Returns the payroll amount for SalaryEmployee subclass"""
        return self.weekly_salary


class HourlyEmployee(Employee):
    """Implement Employee subclass HourlyEmployee"""

    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        """Return check amount"""
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    """Defines an implementation of Commision Employee"""

    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        """Return check amount"""
        return super().calculate_payroll() + self.commission
