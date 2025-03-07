"""
Написать функцию счетчик которая с помощью замыкания (без глобальных переменных)
будет хранить в себе количество запусков и каждый раз возвращать число на 1 больше.
Функция должна принимать число с которого начинается отсчет.

Пример:
с1 = counter(1)
с10 = counter(10)

print(c1()) -> 2
print(c1()) -> 3
print(c1()) -> 4 

print(c10()) -> 11 
print(c10()) -> 12 
print(c10()) -> 13 

"""

def counter (num : int):
    i = 0

    def f_close():
        nonlocal i
        i += 1
        return num + i
    return f_close

num_1 = counter(1)
print(num_1())
print(num_1())
print(num_1())


num_10 = counter(10)
print(num_10())
print(num_10())
print(num_10())
