"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.
"""

i = 0
b = 0

while True:
    marks = int(input('Введите оценку ученика: '))
    if marks == 0:
        break
    elif 0 <= marks <= 10:
        i += marks
        b += 1
    else:
        print ('ошибка')

print('Средний бал ученика: ', i / b)