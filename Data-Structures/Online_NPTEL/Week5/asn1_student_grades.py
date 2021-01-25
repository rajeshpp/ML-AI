content = []
students = {}
grade_codes = {'A': 10, 'AB': 9, 'B': 8, 'BC': 7, 'C': 6, 'CD': 5, 'D': 4}
"""
Sample Input:
===================
Courses
TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
CHAR~Charms~1~2011-2012~Filius Flitwick
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Grades
TRAN~1~2011-2012~SLY2301~AB
TRAN~1~2011-2012~SLY2302~B
TRAN~1~2011-2012~SLY2303~B
TRAN~1~2011-2012~SLY2305~A
TRAN~1~2011-2012~SLY2306~BC
TRAN~1~2011-2012~SLY2308~A
TRAN~1~2011-2012~SLY2309~AB
CHAR~1~2011-2012~SLY2301~A
CHAR~1~2011-2012~SLY2302~BC
CHAR~1~2011-2012~SLY2303~B
CHAR~1~2011-2012~SLY2305~BC
CHAR~1~2011-2012~SLY2306~C
CHAR~1~2011-2012~SLY2307~B
CHAR~1~2011-2012~SLY2308~AB
EndOfInput
"""

text = input()
while text not in 'EndOfInput':
    content.append(text)
    text = input()

for index in range(content.index('Students') + 1, content.index('Grades')):
    items = content[index].split('~')
    key = items[0]
    value = items[1]
    students[key] = {value: []}

for line in content[content.index('Grades') + 1:]:
    items = line.split('~')
    rno = items[3]
    grade = items[4]
    for k, v in students[rno].items():
        students[rno][k].append(grade)

for key, value in students.items():
    for k, v in value.items():
        grade_items = [grade_codes[t] for t in v]
        if len(grade_items) >= 2:
            students[key][k] = round(sum(grade_items) / 2, 2)
        else:
            students[key][k] = round(sum(grade_items), 2)
            # print(key,k,[grade_codes[t] for t in v])

for key, value in sorted(students.items()):
    for k, v in value.items():
        if v == 0:
            print(key + '~' + k + '~' + str(v))
        else:
            print(key + '~' + k + '~' + str(float(v)))

