'''
Пользователь вводит 3 числа, 
найти среднее арифметическое с точность 3 знака после запятой

'''

number1 = float(input('Введите первое число: '))
number2 = float(input('Введите второе число: '))
number3 = float(input('Введите третье число: '))

sr_arifm = round(((number1 + number2 + number3) / 3), 3)
print('Среднее арифметическое:' + str(sr_arifm))

