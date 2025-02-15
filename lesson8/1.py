"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""

def full_name(text : str, param = True):
    
    a = text.split()
    if param == True:
        t = f"{a[0]} {a[1][0]}.{a[2][0]}."
        return t
    else:
        f = f"{a[1][0]}.{a[2][0]}.{a[0]}"
        return f



print(full_name('Николаев Иван Сергеевич'))