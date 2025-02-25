"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""

def error(func):
    def f (*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"В функции {func.__name__} произошла ошибка {e}"
    return f

@ error
def line(text: str):
    return list(text)

print(line('qwerty'))
print(line(5))


@error
def summa(x: int, y: int):
    return x + y

print(summa(2, 3))
print(summa(1))
print(summa('a', 2))