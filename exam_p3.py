class Employee:
    nextIdNum = 0
    """
    the base class
    """

    def __init__(self, name):
        self.name = name
        self.idNum = Employee.nextIdNum
        Employee.nextIdNum += 1

    def get_name(self):
        return self.name

    def weekly_pay(self, hours_worked):
        return 0


class Nonexempt_Employee(Employee):

    def __init__(self, name, hourly_rate):
        Employee.__init__(self, name)
        self.hourly_rate = hourly_rate

    def weekly_pay(self, hours_worked):
        hourly_rate = self.hourly_rate
        if hours_worked < 40:
            hourly_rate = self.hourly_rate
        else:
            OT_hourly_rate = (hourly_rate + (hourly_rate / 2))
        return ((hours_worked * hourly_rate) + (hours_worked * OT_hourly_rate))



class Exempt_Employee(Employee):

    def __init__(self, name, annual_salary):
        Employee.__init__(self, name)
        self.annual_salary = annual_salary

    def annual_pay(self, annual_salary):
        return self.annual_salary

    def weekly_pay(self, annual_salary):
        week_pay = (annual_salary / 52)
        return week_pay



class Manager(Exempt_Employee):

    def __init__(self, name, annual_salary, bonus):
        Exempt_Employee.__init__(self, name, annual_salary)
        self.bonus = bonus

    def annual_pay(self, annual_salary, bonus):
        return self.annual_salary + self.bonus

    def weekly_pay(self, annual_salary, bonus):
        week_pay = ((annual_salary + bonus) / 52)
        return week_pay
    


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
