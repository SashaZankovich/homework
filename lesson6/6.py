"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""

a1, a2, a3, a4 = 3.3, '2', 2, 3

a = [a1, a2,a3, a4]

print(all(isinstance(x, float) for x in a))
print(any(isinstance(x, str) for x in a))

pairs = [[a1, a3], [a2, a4], [a3, a4]]

print(any(isinstance(x, int) and isinstance(y, int) for x, y in pairs))

