from datetime import date


class Employee:
    def __init__(self, firstname, lastname, birth_date):
        self.firstname = firstname
        self.lastname = lastname
        self.birth_date = birth_date

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)

    def calculate_age(self):
        year_now = date.today().year
        birth_year = self._birth_date.year
        return year_now - birth_year


try:
    employee1 = Employee("arhiya", "shabdin", "2004-01-28")
    print(f"{employee1.firstname} {employee1.lastname} (Age: {employee1.calculate_age()})")
except ValueError as error:
    print(error.args[0])
