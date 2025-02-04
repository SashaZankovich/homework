"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""

d = {'one':11, 'two':22, 'hello':'python', True:False}

c = list(d.items())

user_data = int(input("Введите номер элемента, который необходимо удалить "))

del c[user_data]

print(c)




