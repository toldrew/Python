import csv, json
j_in = open('nums.json', 'r').read()
d = json.loads(j_in)
print(d)

d = json.get(j_in)
print(d)