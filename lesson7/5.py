'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''


v = ['qwertyu', 'asdfggh', 'zxcvbnm', 'yuiop[]', 'hjklasd', 'mnbvnbv']
ind = 0 
el = 1

for a, s in enumerate(v):
    print(el, v[ind], s[0], sep=' - ')
    ind += 1
    el += 1