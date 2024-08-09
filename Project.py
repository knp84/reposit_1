from math import sqrt
from random import randint
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
        case 3:                              
            player_x = link
            try:
                player_x = float(player_x)
                if player_x == int(player_x):
                    return int(player_x)
                else:
                    return round(player_x, 1)
            except:
                print('err') 
                return player_x 
while True:
    choise_dif = input('Выберите сложность задачи от 1 до 4: ') 
    match choise_dif: 
        case '1':                                   
            a = randint(0,100)
            b = randint(0,100)
            determine = 1
            addition = a + b
            print(f'Введите сумму чисел {a} и {b}: ')
            if player_solution() == addition:                
                print(f'да, {a} + {b} = {addition}')         
            else:
                print('Неверный ответ!', addition)  
        case '2':                         
            a = randint(0,10)
            b = randint(1,10)
            multiply = a * b
            determine = 1
            print(f'Введите произведение чисел {a} и {b}: ')
            if player_solution() == multiply:
                print(f'да, {a} * {b} = {multiply}')
            else:
                print('Неверный ответ!', multiply)      
        case '3':
            a = randint(1,10)
            b = randint(-100,100)
            determine = 2
            z = -b
            x = z / a               # решения уравнения 
            if b > 0:
                sing = '+'
            else:
                sing = ''              # знаки в уравнении 
            print(f'{a}x{sing}{b} = 0', 'Введите х: ', sep='\n')
            if player_solution() == round(x):
                print('Верный ответ!')
            else:
                print('Неверный ответ!', x)
        case '4':    
            a = randint(1,9)
            b = randint(-9,9)
            c = randint(-9,9)
            spic = tuple(range(1, 101)) 
            D = (b ** 2) - (4 * a * c)         
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
                                
                                break
                            else:
                                pass
                                
                        else:
                            
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
                            print('Верно, теперь введите корни')
                            determine = 3
                            link = input()
                            if player_solution() == int(x1) or player_solution() == round(x1, 1):
                                link = input()
                                if player_solution() == int(x2) or player_solution() == round(x2, 1):
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
        case _:
            print('Выберете один из существующих уровней сложности!')
    end_cycle = input('Хотите попробовать еще раз? ')
    match end_cycle:
        case 'да':
            continue
        case _:
            break