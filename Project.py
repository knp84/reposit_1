from math import sqrt                       #пытаюсь переделать case 4
from random import randint
a = randint(1,9)
b = randint(-9,9)
c = randint(-9,9)
spic = tuple(range(1, 101)) 
D = (b ** 2) - (4 * a * c)
def square_equation():
    sign1 = ''
    sign2 = ''
    print(f'{a}x^2 {sign1}{b}x {sign2}{c} = 0', D)
def player_solution():
    match determine:                                 
        case 1:
            try:
                solution = int(input())     
                return solution                               
            except:                                                            
                return print('Ошибка ввода! Введите число!')                
        case 2:
            try:
                solution = float(input('округлите x до первого знака после запятой '))
                return solution
            except:
                print('Введите число с плавающей точкой!')
        case 3:                                #решил  убрать не нужные точки (1.0, 5.0) и расширить функцию. Работает так себе
            player_x = input()
            try:
                player_x = float(player_x)
                if player_x == int(player_x):
                    return int(player_x)
                else:
                    return round(player_x, 1)
            except:
                print('err')         
if D > 0:                               
    if sqrt(D) not in spic:
        while True:              
            j = randint(-1,1)               #изменяю a b c для удовлетворительного значения D
            a += j 
            b += j 
            c += j 
            D = (b ** 2) - (4 * a * c)
            if D > 0:
                if sqrt(D) in spic and a > 0:
                    print(a, b, c, D)
                    break
                else:
                    pass
                    print(a, b, c)
            else:
                print('pon')
                break    
    if D > 0:
        if sqrt(D) in spic:
            x1 = (-b - sqrt(D)) / (2 * a)
            x2 = (-b + sqrt(D)) / (2 * a)
            determine = 1
            if b >= 0:
                sign1 = '+'
            if c >= 0:
                sign2 = '+'    
            square_equation()
            if player_solution() == D:     
                print(x1, x2, round(x1, 1), round(x2, 1))
                determine = 3
                if player_solution() == round(x1, 1) or player_solution() == int(x1):
                    if player_solution() == round(x2, 1) or player_solution() == int(x2): #странно работает если допустить ошибку в x2
                        print('Верно!')
                    else:
                        print('Неверно!')
                else:
                    print('Неверно!')        
            else:               
                print('Неверно!')
if D < 0:
    square_equation()
    determine = 1
    if D == player_solution():
        print('правильно, корней нет')
    else:
        print('Неверно!')
if D == 0:
    square_equation()
    determine = 1
    if D == player_solution():
        determine = 3
        print('Введите корень:')
        match x1:
                case player_solution():
                    print('Верно!')
                case _:
                    print('Неверно!')
    else:
        print('Неверно')
