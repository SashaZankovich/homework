"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""

def brackets(text):
    br = 0
    for symbol in text:
        if symbol == "(":
            br = br + 1
        elif symbol == ")":
            br = br - 1
        if br < 0:
            return False
    return br == 0

print(brackets('(()())'))
print(brackets('(()()()'))
print(brackets('(hello(2)ver()(33)python)'))
print(brackets('(hello(2()ver(33)python))'))
print(brackets('(hello(2()ver(33)python)'))