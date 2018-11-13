class Employee:
    """
    the base class
    """

    def __init__(self, name):
        pass  # delete this line and replace with your code here

    def get_name(self):
        pass  # delete this line and replace with your code here

    def weekly_pay(self, hours_worked):
        return 0


class Nonexempt_Employee(Employee):

    def __init__(self, name, hourly_rate):
        pass  # delete this line and replace with your code here

    # Overrides the superclass method.
    def weekly_pay(self, hours_worked):
        pass  # delete this line and replace with your code here


class Exempt_Employee(Employee):
    pass  # delete this line and replace with your code here


class Manager(Exempt_Employee):
    pass  # delete this line and replace with your code here


def main():
    all_employees = []
    all_employees.append(Nonexempt_Employee("Aaron Wendell", 40.0))
    all_employees.append(Exempt_Employee("Alden Pexton", 60000.0))
    all_employees.append(Manager("Allison Fernandez", 94000.0, 50.0))

    for employee in all_employees:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.weekly_pay(hours)
        print("Salary: ", pay)


if __name__ == '__main__':
    main()
