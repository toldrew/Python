from datetime import datetime, date
import csv
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

def find_oldest_person(filename):
    persons=[]
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for n, row in enumerate(spamreader):
            if n>0:
                try:
                    persons.append(Person(row[0],row[1],row[2],row[3]))
                except:
                    persons.append(Person(row[0], row[1], row[2]))
    max_age=persons[0]
    for i in persons:
        if max_age.get_age() < i.get_age():
            max_age = i
    return max_age.get_fullname()

print(find_oldest_person('person.csv'))
ivanoff = Person("Ivanov", "Ivan", "2000-10-20")
ivanoff.birth_date
print(ivanoff.get_age())
