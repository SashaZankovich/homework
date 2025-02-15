'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''
def count_char(text : str):

    d = {c:text.count(c) for c in set(text) if c != ' ' and c != ','} 
    return d


# Примеры использования
print(count_char('Hello, Python')) 
print(count_char('aaaaaaa bbbb'))