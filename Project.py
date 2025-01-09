from math import sqrt
from random import randint
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
                solution = float(input('Введите х: '))
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
print("В программе существует 4 уровня сложности.\n первый - сложение\n второй - умножение\n третий - уравнение\n четвертый - квадратные уравнения")
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
                print(f'Правильно. {a} + {b} = {addition}')         
            else:
                print(f'Неверно. {a} + {b} = {addition}')  
        case '2':                         
            a = randint(0,50)
            b = randint(1,20)
            multiply = a * b
            determine = 1
            print(f'Введите произведение чисел {a} и {b}: ')
            if player_solution() == multiply:
                print(f'Правильно. {a} * {b} = {multiply}')
            else:
                print(f'Неправильно. {a} * {b} = {multiply}')      
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
            print(f'{a}x{sing}{b} = 0', 'округлите x до первого знака после запятой', sep='\n')
            if player_solution() == round(x, 1):
                print(f'Правильно. Корень уровнения равен {round(x, 1)}')
            else:
                print(f'Неравильно. Корень уровнения равен {round(x, 1)}')
        case '4':    
            a = randint(1,9)
            b = randint(-9,9)
            c = randint(-9,9)
            list = tuple(range(1, 101)) 
            D = (b ** 2) - (4 * a * c)         
            if D > 0:                               
                if sqrt(D) not in list:
                    while True:              
                        j = randint(-1,1)               #изменяю a b c для удовлетворительного значения D
                        a += j 
                        b += j 
                        c += j 
                        D = (b ** 2) - (4 * a * c)
                        if D > 0:
                            if sqrt(D) in list and a > 0:
                                break
                            else:
                                pass      
                        else:
                            break    
                if D > 0:
                    if sqrt(D) in list:
                        x1 = (-b - sqrt(D)) / (2 * a)
                        x2 = (-b + sqrt(D)) / (2 * a)
                        determine = 1
                        sign1 = '+'
                        sign2 = '+'
                        if b < 0:
                            sign1 = ''
                        if c < 0:
                            sign2 = ''    
                        print(f'{a}x^2 {sign1}{b}x {sign2}{c} = 0', 'Введите дискриминант уравнения:', sep='\n')
                        if player_solution() == D:     
                            print(f'Верно. Дискриминант равен {D}', 'Tеперь введите первый корень уравнения в порядке возрастания:', sep='\n')
                            determine = 3
                            link = input()
                            if player_solution() == int(x1) or player_solution() == round(x1, 1):
                                print(f'Правильно. первый корень уровнения равен {x1}, теперь введите второй корень уравнения')
                                link = input()
                                if player_solution() == int(x2) or player_solution() == round(x2, 1):
                                    print(f'Правильно. второй корень уровнения равен {x1}')
                                else: 
                                    print(f'Неправильно. второй корень уровнения равен {x1}')
                            else:
                                print(f'Неправильно. первый корень уровнения равен {x1}')        
                        else:               
                            print(f'Неправильно. Дискриминант равен {D}.')
            if D < 0:
                sign1 = '+'
                sign2 = '+'
                if b < 0:
                    sign1 = ''
                if c < 0:
                    sign2 = ''    
                print(f'{a}x^2 {sign1}{b}x {sign2}{c} = 0')
                determine = 1
                if D == player_solution():
                    print(f'Правильно. Дискриминант равен {D}. Корней нет')
                else:
                    print(f'Неправильно. Дискриминант равен {D}. Корней нет')
            if D == 0:
                sign1 = '+'
                sign2 = '+'
                if b < 0:
                    sign1 = ''
                if c < 0:
                    sign2 = ''    
                print(f'{a}x^2 {sign1}{b}x {sign2}{c} = 0')
                determine = 1
                if D == player_solution():
                    determine = 3
                    print('Введите корень:')
                    match x1:
                            case player_solution():
                                print(f'Правильно. Корень уровнения равен {x1}')
                            case _:
                                print(f'Неправильно. Корень уровнения равен {x1}')
                else:
                    print(f'Неправильно. Дискриминант равен {D}.')
        case _:
            print('Выберете один из существующих уровней сложности!')
    end_cycle = input('Хотите попробовать еще раз? да/нет\n')
    match end_cycle:
        case 'да':
            continue
        case 'нет':
            break
        

