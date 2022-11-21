import math
# Домашняя работа к семинару 1, для выбора необходимой программы запустите код и введите номер программы для проверки.

# Задача 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def IsDayWeekend(day):
    if day in range(1, 6):
        return 'Будний день'
    else:
        return 'Выходной'

def PorgramOne():
    print('Введите № дня недели')
    day = int(input('День недели = '))
    print(IsDayWeekend(day))
    MainProgram()

# Задача 2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def ProgramTwo():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not (x or y or z) == (not x and not y and not z):
                    print('Утверждение истинно')
                else:
                    print('Утверждение ложно')
                print(x, y, z)
    MainProgram()

# Задача 3 Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def CheckQuarterAxis(x, y):
    if x > 0 and y > 0:
        return 'в 1 четверти.'
    elif x < 0 and y > 0:
        return 'в 2 четверти.'
    elif x < 0 and y < 0:
        return 'в 3 четверти.'
    elif x > 0 and y < 0:
        return 'в 4 четверти.'
    elif x == 0 and y != 0:
        return 'на оси абсцисс.'
    elif x != 0 and y == 0:
        return 'на оси ординат.'
    elif x == 0 and y == 0:
        return 'в центре графика.'
    else:
        return 'не находится xD'

def ProgramThree():
    print('Введите координату X')
    x = int(input('X = '))
    print('Введите координату Y')
    y = int(input('Y = '))
    print('Координаты находятся ', CheckQuarterAxis(x, y))
    MainProgram()

# Задача 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y). P.S. Как максимум взято 100/-100.

def CheckQuarterRange(numberOfQuarter):
    quartersX = {
        1: (1, 100),
        2: (-1, -100),
        3: (-1, -100),      
        4: (1, 100)
    }
    quartersY = {
        1: (1, 100),
        2: (1, 100),
        3: (-1, -100),
        4: (-1, -100)
    }
    rangeXY = (quartersX[numberOfQuarter], quartersY[numberOfQuarter])
    return rangeXY

def ProgramFour():
    print('Введите номер четверти графика')
    numberOfQuarter = int(input('Четверть = '))
    rangeXY = CheckQuarterRange(numberOfQuarter)
    print('Диапазон значений X =',
          rangeXY[0], ', диапазон значений Y =', rangeXY[1])
    MainProgram()

# Задача 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def CheckDistance(x, y):
    result = math.sqrt(((x[0] - y[0])**2) + ((x[1] - y[1])**2))
    return result

def ProgramFive():
    print('Введите координаты точки X')
    x = (float(input('Первая координата = ')), float(input('Вторая координата = ')))
    print('Введите координаты точки Y')
    y = (float(input('Первая координата = ')), float(input('Вторая координата = ')))
    print('Расстояние между точками =', round(CheckDistance(x, y), 3))
    MainProgram()

def MainProgram():
    print('Введите номер программы (1-5), либо введите "Q" для выхода.')
    program = input('Программа № = ')
    if program.lower() == 'q':
        print('До свидания!')
    elif program.isdigit():
        if int(program) == 1:
            PorgramOne()
        elif int(program) == 2:
            ProgramTwo()
        elif int(program) == 3:
            ProgramThree()
        elif int(program) == 4:
            ProgramFour()
        elif int(program) == 5:
            ProgramFive()
        else:
            print('Введен некорректный номер, попробуйте еще раз.')
            MainProgram()
    else:
        print('Ввод некорректен, пожалуйста, попробуйте еще раз.')
        MainProgram()

print('Здравствуйте!')
MainProgram()