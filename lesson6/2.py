'''
запросить у пользователя логин пароль и возраст
вывести доступ разрешен:
    логин:admin   пароль:123456    возраст: любой    
    логин:vasya   пароль: vas123   возраст: менее 60
    логин:guest   пароль: любой    возраст:более 18
    
в остальных случаях - "доступ запрещен".

'''

login = input("Логин ")
password = input('Пароль ')
age = int(input('Возраст '))

if (login == "admin" and password == "123456") or \
        (login == "vasya" and password == "vas123" and age < 60) or \
        (login == 'guest' and age > 18):
    print('доступ разрешен')
else:
    print('доступ запрещен')