from math import sqrt
from random import randint
while True:
    choise_dif = input('Выберите сложность задачи от 1 до 4: ') 
    match choise_dif: 
        case '1':    
            a = randint(0,100)
            b = randint(0,100)
            plus = a + b
            print(f'Введите сумму чисел {a} и {b}: ')
            try:
                player_choise = int(input())
                if player_choise == plus:
                    print(f'да, {a} + {b} = {plus}')
                else:
                    print('Неверный ответ!', plus)  
            except:
                print('Вы уверены что ввели число? ') 
            end_cycle = input('Хотите попробовать еще раз? ')   
            match end_cycle:
                case 'да':
                    continue
                case _:
                    break   
        case '2':                         
            a = randint(0,10)
            b = randint(1,10)
            mult = a * b
            print(f'Введите произведение чисел {a} и {b}: ')
            try:
                player_choise = int(input())
                if player_choise == mult:
                    print(f'да, {a} * {b} = {mult}')
                else:
                    print('Неверный ответ!', mult)
            except:
                print('Вы уверены что ввели число?')    
            end_cycle = input('Хотите попробовать еще раз? ')
            match end_cycle:
                case 'да':
                    continue
                case _:
                    break   
             
        case '3':
            a = randint(1,10)
            b = randint(-100,100)
            z = -b
            x = z / a               # решения уравнения 
            if b > 0:
                k = '+'
            else:
                k = ''              # знаки в уравнении 
            print(f'{a}x{k}{b} = 0')
            prov = float(input('Введите x: '))
            if prov == round(x):
                print('Верный ответ!')
            else:
                print('Неверный ответ!', x)
            end_cycle = input('Хотите попробовать еще раз? ')
            match end_cycle:
                case 'нет':
                    break 
        case '4':
            a = randint(-9,9)
            b = randint(-9,9)
            c = randint(1,9)
            sign1 = ''
            sign2 = '+'
            if b >= 0:
                sign1 = '+'
            rand = randint(1,2)
            spic = tuple(range(1, 101)) 
            D = (b ** 2) - (4 * a * c)
            if D > 0:
                x1 = (-b - sqrt(D)) / (2 * a)
                x2 = (-b + sqrt(D)) / (2 * a)
                if sqrt(D) in spic:                #ограничивает дискриминант
                    print(f'{a}x^2 {sign1}{b}x {sign2}{c} = 0')
                    x1x2 = f'{min(x1, x2)}, {max(x1, x2)}'
                    player_choise1 = input('Введите дискриминант квадратного уравнения: ')
                    if player_choise1 == str(D):
                        player_choise2 = input('Верно! Введите x1 и x2 в порядке возрастания через запятую: ')
                        if player_choise2 == x1x2:
                            print('Правильно!', x1x2) 
                        else:
                            print('Неправильно!', x1x2)
                    else:
                        print(f'Неверно, дискриминант равен {D}')  
            elif D == 0:
                x = -b / (2 * a)
                print(f'{a}x^2 {sign1}{b}x {sign2}{c} = 0')
                try:
                    player_choise1 = int(input('Введите дискриминант квадратного уравнения: '))
                    if player_choise1 == D:
                        player_choise2 = input('Введите x1 и x2 квадратного кравнения: ')
                        if player_choise2 == str(x):
                            print('Вы правильно решили квадратное уравнение!') 
                        else:
                            print('Вы неправильно решили квадратное уравнение! Попробуйте сонва!')
                    else:
                        print(f'Неверно, дискриминант равен {D}')
                except:
                    print('Вы уверены что ввели число?') 
            elif D < 0:
                x = 'Корней нет'
                print(f'{a}x^2 {sign1}{b}x {sign2}{c} = 0')
                try:
                    player_choise1 = int(input('Введите дискриминант квадратного уравнения: '))
                    if player_choise1 == D:
                        print('Правильно! Корней нет')
                    else:
                        print(f'Неверно, дискриминант равен {D}')
                except:
                    print('Вы уверены что ввели число?')
            else:
                print('error') #подстраховка
            end_cycle = input('Хотите попробовать еще раз? ')
            match end_cycle:
                case 'да':
                    continue
                case _:
                    break 
        case _:
            print('Выберете один из существующих уровней сложности!')