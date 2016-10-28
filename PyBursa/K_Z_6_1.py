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


st_lena = Student("Lena", {"lab_max": 10, "lab_num": 3})
st_lena.name
st_lena.labs
st_lena.set_lab(5, 1)
print(st_lena.labs)
st_lena.set_lab(9)
print(st_lena.labs)
st_lena.set_lab(15)
print(st_lena.labs)
print(st_lena.average_score())
st_lena.set_lab(7, 0)
print(st_lena.labs)
print(st_lena.average_score())