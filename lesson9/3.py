'''
Написать рекурсивную функцию, которая принимает 2 аргумента 
(целые числа - a и b) и высчитывает суммы всех чисел от a до b (включительно). 
Пример: a = 3, b = 5 -> 12 (3+4+5)
Пример: a = 5, b = 9 -> 35 (5+6+7+8+9)"

'''

# без рекурсии
def f1(a : int, b : int):
    spisok = list(range(a, b + 1))
    if a == b:
        pass
    elif a > b:
        return "Число 'а' должно быть меньше числа 'b'"
    else:
        return sum(spisok)
    
print(f1(3, 5))
print(f1(5, 9))

# c рекурсией
def f2(a : int, b : int):
    if a == b:
        pass
    elif a > b:
        return "Число 'а' должно быть меньше числа 'b'"
    else:
        return a + f2(a + 1, b)
    
print(f2(3, 5))
print(f2(5, 9))