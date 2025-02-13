"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""

v = {}
user_name = ''
user_review = ''

while user_name != 'stop' or user_review != 'stop':
    user_name = input('Введите ваше имя: ')
    user_review = input('Введите ваш отзыв: ')
    if user_name != 'stop' and user_review != 'stop':
        v[user_name] = user_review
    else:
        break

print('Количество отзывов: ', len(v))
print('Имена пользователей:', *v.keys(), sep='\n - ')
print('Отзывы пользователей: ', *v.values(), sep='\n - ')
   