"""
Запросить любое число не менее 10. 
Вывести на экран сумму квадратов каждой цифры составляющей это число. 
Например: дано 236 => 2*2 + 3*3 + 6*6 = 49 

"""


num = input('Введите любое число не менее 10: ')
t = 0

for i1, i2 in enumerate(num):
    if int(num) >= 10: 
        a = int(i2) * int(i2)
        t += a

if t >= 1:
    print('Сумма квадратов каждой цифры числа: ', t)
else:
    print('Ошибка')

