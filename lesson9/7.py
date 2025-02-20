"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""
spisok = [{"name":"Dima", "login":"Dima1988", "password":"Qwerty123" },
          {"name":"Egor", "login":"Egor2001", "password":"!qaz" },
          {"name":"Oleg", "login":"Oleg1999", "password":"asbbbd" }]


f = filter(lambda x: len(x['password']) < 5, spisok)
print(*f)