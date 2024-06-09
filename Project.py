from math import sqrt                       #пытаюсь переделать case 4
from random import randint
a = randint(1,9)
b = randint(-9,9)
c = randint(-9,9)
spic = tuple(range(1, 101)) 
D = (b ** 2) - (4 * a * c)
def player_solution():
    match determine:                                 
        case 1:
            try:
                solution = int(input())                                    
            except:                                                            
                return print('Ошибка ввода! Введите число!')                
        case 2:
            try:
                solution = float(input('округлите x до первого знака после запятой '))
            except:
                print('Введите число с плавающей точкой!')
        case 3:
            solution = input()
            try:
                int(solution)
            except:
                print('Введите строковое значение')
    return solution
if D > 0:                               #не знаю как убрать эти проверки многочисленные, глаз режут
    if sqrt(D) not in spic:
        while sqrt(D) not in spic:              
            j = randint(-1,1)               #изменяю a b c для удовлетворительного значения D
            a += j 
            b += j 
            c += j 
            D = (b ** 2) - (4 * a * c)
            if D > 0:
                if sqrt(D) in spic:
                    print(a, b, c, D)
                    break
                else:
                    pass
                    print(a, b, c)
            else:
                break 
    if sqrt(D) in spic:
        determine = 1
        print('pon')
        sign1 = ''
        sign2 = ''
        if b >= 0:
            sign1 = '+'
        if c >= 0:
            sign2 = '+'    
elif D < 0:
    print('корней нет')
else:
    print('корень 1')