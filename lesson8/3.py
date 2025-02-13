'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''

def factorial(n : int):

    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))