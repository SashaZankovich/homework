'''
Запросить количество секунд. 
Вывести на экран время в формате ЧЧ:ММ:СС равное эти секундам.
Пример: 35457 -> 09:50:57
Сделать 2 варианта с форматной строкой и без.
'''

user_seconds = int(input('Введите количество секунд '))

hours = user_seconds // 3600
minutes = user_seconds // 60 % 60
seconds = user_seconds % 60

print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')