'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''

def rectangle(side1 : float, side2 : float, square_perimetr : str):
    if square_perimetr == 'square':
        return 'Площадь прямоугоьника: ', side1 * side2
    elif square_perimetr == 'perimetr':
        return 'Периметр прямоугольника: ', (side1 + side2) * 2
    else:
        return 'Введены некоректные данные, параметр param равен "square" либо "perimetr"'


print(rectangle(3.5, 2.1, square_perimetr='perimetr'))