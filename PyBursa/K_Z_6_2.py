import csv
class Student:
    def __init__(self, name, conf ):
        self.name = name
        self.conf = conf
        self.labs = [0 for i in range(conf['lab_num'])]


    def set_lab(self, score, number=-1):
        try:
            score = min(score, self.conf['lab_max'])
            if number == -1:
                self.labs[self.labs.index(0)] = score
            else:
                self.labs[number] = score

        except:
            return 'error'

    def average_score(self):
        sc = 0
        for i in self.labs: sc += i
        return round(sc/len(self.labs), 1)

def find_best_student(filename):
    students=[]
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for n, row in enumerate(spamreader):
            if n > 0:
                students.append(Student(row[0], {'lab_max': int(row[1]), 'lab_num': int(row[2])}))
                for i in row[3:]:
                    students[n-1].set_lab (int(i))

    max_av_sc = students[0]
    for i in students:
        if max_av_sc.average_score() < i.average_score():
            max_av_sc = i
    return max_av_sc.name

print(find_best_student('student.csv'))