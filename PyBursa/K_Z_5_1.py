from datetime import datetime, date
class Person:
    def __init__(self, surname, first_name, birth_date, nickname=''):
        self.surname = surname
        self.first_name = first_name
        if nickname == '':
            self.nickname = surname
        else:
            self.nickname = nickname
        self.birth_date = date(datetime.strptime(birth_date, "%Y-%m-%d").year, datetime.strptime(birth_date, "%Y-%m-%d").month, datetime.strptime(birth_date, "%Y-%m-%d").day)
    def get_age(self):
        y = datetime.today().year - self.birth_date.year
        if datetime.today().month < self.birth_date.month: y -= 1
        elif datetime.today().month == self.birth_date.month and datetime.today().day < self.birth_date.day:
            y -= 1
        return str(y)
    def get_fullname(self):
        return self.surname + ' ' + self.first_name

ivanoff = Person("Ivanov", "Ivan", "2000-10-20")
ivanoff.birth_date
print(ivanoff.get_age())
