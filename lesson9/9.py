"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""

def dict_from_args(*args, **kwargs):
    l_args = list(args)
    a = all(type(arg) is int for arg in l_args)
    l_kwargs = list(kwargs.values())
    k = all(type(kwarg) is str for kwarg in l_kwargs)
    if a == True:
        a1 = sum(l_args)
    else:
        raise TypeError("Все позиционные аргументы должны быть целыми")
    if k == True:
        k1 = len(max(l_kwargs))
    else:
        raise TypeError("Все аргументы - ключевые слова должны быть строками")
    return {'args_sum':a1, 'kwargs_max_len':k1}
    

print(dict_from_args(1, 2, 3, 4, 5, 1, name = "Sasha", age = '25', title = "economist"))




