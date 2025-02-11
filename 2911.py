def field_of_play(list_play):  #функция создает список для проверки строк, столбцов, диагоналей
    list_play_2 =[]
    for j in range(len(list_play)):   #Создаем элементы для списка по столбцам
        d = []
        for i in range(len(list_play)):
            d.append(list_play[i][j])

        list_play_2.append(d)
    d =[list_play[0][0],list_play[1][1],list_play[2][2]] #Создаем элемент для списка 1 диагонали
    list_play_2.append(d)
    d = [list_play[2][0], list_play[1][1], list_play[0][2]] #Создаем элемент для списка 1 диагонали
    list_play_2.append(d)

    list_play_3=list_play+list_play_2 #Готовый список для проверки
    return list_play_3

def check(list_1): #Функция проверяет наличие совпадений на поле
    global u
    b=[]
    for i in list_1:
        d =all(x == u for x in i)
        b.append(d)
    k = any(x == True for x in b)
    if k:
        m = "вы победили!!!"
    else:
        m = 'Играем дальше?'
    return m
def checking_for_completion(res):# Функция проверяет завершить игру или продолжить
    if res == 'Играем дальше?':
        result1 = True
    else:
        result1 = False
    return result1


def field_console(h):
    return print(f' |0|1|2|\n0 {h[0][0]} {h[0][1]} {h[0][2]}\n1 {h[1][0]} {h[1][1]} {h[1][2]}\n2 {h[2][0]} {h[2][1]} {h[2][2]}')

def checking_values(values):
    #Функция проверяет один раз введенные значения строк и столбцов
    if values == 0 or values == 1 or values == 2:

        return values

    else:
        values = int( input('Не верно ввели, введите заново: '))
        return values



A=input('Введите кто первый ходит, Х или 0: ')
A =(A.upper())

field=[['-','-','-'],['-','-','-'],['-','-','-']]


field_console(field)
r=0
a = True
while r<8 and a: #Максимальное число ходов 8
    if A=='0':
        f1 = checking_values(int(input(f'Введите номер строки для {A}: ')))
        f2 = checking_values(int(input(f'Введите номер столбца для {A}: ')))

        field[f1][f2] = A #Добавляем элемент на игровое поле
        u = '0' #Определяем элемент, по которому будем проверять совпадение в строках, столбцах, диагоналях
        field_console(field)# Выводим поле в консоль
        result =check(field_of_play(field)) #Проверка элементов на поле
        print(result)
        a=checking_for_completion(result) #Проверяем игру на завершение
        A = "X"
    else:
        f1 = checking_values(int(input(f'Введите номер строки для {A}: ')))

        f2 = checking_values(int(input(f'Введите номер столбца для {A}: ')))

        field[f1][f2] = A #Добавляем элемент на игровое поле
        u='X' #Определяем элемент, по которому будем проверять совпадение в строках, столбцах, диагоналях
        field_console(field) # Выводим поле в консоль
        result = check(field_of_play(field)) #Проверка элементов на поле
        print(result)
        a = checking_for_completion(result) #Проверяем игру на завершение
        A ='0'
    r += 1
print('Ой, игра закончилась')








# print(f' |0|1|2|')
# print(f'0 {h[0][0]} {h[0][1]} {h[0][2]}')
# print(f'1 {h[1][0]} {h[1][1]} {h[1][2]}')
# print(f'2 {h[2][0]} {h[2][1]} {h[2][2]}')

