'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''

def rectangle(side1 : float, side2 : float, square_perimetr : str):
    if square_perimetr == 'square':
        print('Площадь прямоугоьника: ', side1 * side2)
    elif square_perimetr == 'perimetr':
        print('Периметр прямоугольника: ', (side1 + side2) * 2)
    else:
        print('Введены некоректные данные, параметр param равен "square" либо "perimetr"')


rectangle(3.5, 2.1, square_perimetr='perimetr')