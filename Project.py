from math import sqrt                       #пытаюсь переделать case 4
from random import randint
a = randint(1,9)
b = randint(-9,9)
c = randint(-9,9)
spic = tuple(range(1, 101)) 
D = (b ** 2) - (4 * a * c)
def square_equation():
    print(f'{a}x^2 {sign1}{b}x {sign2}{c} = 0')
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
            player_x_1 = input()
            try:
                player_x_1 = float(player_x_1)
                if player_x_1 == int(player_x_1):
                    return int(player_x_1)
                else:
                    return round(player_x_1, 1)
            except:
                print('err')    
        case 4:
            player_x_2 = input()
            try:
                player_x_2 = float(player_x_2)
                if player_x_2 == int(player_x_2):
                    return int(player_x_2)
                else:
                    return round(player_x_2, 1)
            except:
                print('err')      
    
if D > 0:                               
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
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        sign1 = ''
        sign2 = ''
        if b >= 0:
            sign1 = '+'
        if c >= 0:
            sign2 = '+'    
        determine = 1
        square_equation()
        if player_solution() == D:     
            print(x1, x2, round(x1, 1), round(x2, 1))
            determine = 3
            if player_solution() == round(x1, 1) or player_solution() == int(x1):
                determine = 4
                if player_solution() == round(x2, 1) or player_solution() == int(x2):
                    print('Верно!')
                else:
                    print('Неверно!')
            else:
                print('Неверно!')        
        else:               
            print('Неверно!')
elif D < 0:
    print('корней нет')
else:
    print('корень 1')