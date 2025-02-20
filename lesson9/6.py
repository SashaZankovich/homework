"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""

temp = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

s1 = dict(sorted(temp.items(), key = lambda x:x[1]))
print(s1)
s2 = dict(sorted(temp.items(), key = lambda x:x[1], reverse=True))
print(s2)