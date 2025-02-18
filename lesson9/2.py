'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''

def factorial(n : int):
   if n == 1 or n == 0:
       return 1
   elif n < 0:
       return "Факториал принимает положительные значения"
   else:
       return n*factorial(n-1)



print(factorial(5))
print(factorial(-1))
print(factorial(1))
print(factorial(0))