'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''

spisok = [False, 'python', True, 'hello', 123]

f1 = filter(lambda x: type(x) == str, spisok)
print(list(f1))

f2 = filter(lambda x: type(x) == bool, spisok)
print(list(f2))
