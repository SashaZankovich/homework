"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""


def yes_or_no(spisok):
    a = any(type(sp) is not int for sp in spisok)
    yn = ['yes' if spisok[:i].count(spisok[i]) else 'no' for i in range(len(spisok))]
    if a == True:
        return False
    else:
        return yn
    
print(yes_or_no([1, 2, 3, 4, 5, 1, 3, 7]))
print(yes_or_no([1, 2, 3, 'yes']))
print(yes_or_no([1, 2, 3, 4.5]))
    

