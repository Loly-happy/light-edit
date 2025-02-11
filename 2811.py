# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # добавим новый элемент в список
# clients.append('Oscar Martinez')
#
# # выведем получившийся список
# print(clients)
#
#
# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # добавим несколько элементов в список
# clients.extend(['Oscar Martinez', 'Creed Bratton', 'Andy Bernard'])
#
# # выведем получившийся список
# print(clients)
#
#
# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # добавим элемент по индексу 1
# clients.insert(1, 'Oscar Martinez')
#
# # выведем получившийся список
# print(clients)


#
#
#
# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
# print(f'Список клиентов: {clients}')
#
# # считываем элемент, который нужно удалить
# name = input('Введите клиента, которого нужно удалить: ')
#
# # проверка на вхождение элемента в список
# if name in clients: # элемент есть в списке
#  # удаляем элемент из списка
#  clients.remove(name)
#  print('Клиент удален из списка.')
# else: # элемента в списке нет
#  print('Данного клиента в списке нет.')
#
# # выведем получившийся список
# print(f'Список клиентов: {clients}')
#
#
#
#
#
# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
#
# # удаляем клиента по индексу 0
# first_client = clients.pop(0)
#
# print(f'Удаленный клиент: {first_client}')
# print(f'Список клиентов: {clients}')
#
#
#
#
#
# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # удаляем последний элемент из списка
# clients.pop()
#
# print(f'Список клиентов: {clients}')
#
#
#
#
# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # удаляем все элементы из списка
# clients.clear()
#
# print(f'Список клиентов: {clients}')
# print(type(clients))
#
#
#
# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # найдем индекс элемента Michael Scott
# index = clients.index('Michael Scott')
# print(f'Индекс элемента Michael Scott: {index}')
#
#
#
# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # сортируем список в порядке возрастания
# clients.sort()
# print(f'Сортировка в порядке возрастания: {clients}')
#
# # сортируем список в порядке убывания
# clients.sort(reverse=True)
# print(f'Сортировка в порядке убывания: {clients}')
#
# print('Введите количество дел')
# n = int(input())
# todo = []
# print('Введите новое дело для списка')
# for i in range(n):
#
#     d = input(f'{i + 1}) ')
#     todo.append(d)
# print(f'Список дел на сегодня {todo}')
#
# n = int(input('Введите номер дала, которое нужно отредактировать: '))
# todo.pop(n-1)
#
# todo.insert(n-1, input('Введите отредактированное дело: '))
# print(todo)
#
# n = int(input('Введите дело, которое нужно удалить: '))
# todo.pop(n-1)
# print(todo)



# n = int(input('Введите количество дел на сегодня: '))
# todo = []
#
# print('Введите задачи на сегодня: ')
# for i in range(n):
#     task = input(f'{i + 1}) ')
#     todo.append(task)
#
# print('Список дел на сегодня:')
# print(todo)
#
# n = int(input('Введите номер дела, которое нужно отредактировать: '))
# task = input('Введите новое описание для дела: ')
# todo[n - 1] = task
#
# n = int(input('Введите индекс дела, которое нужно удалить: '))
# todo.pop(n)
#
# print('Список дел на сегодня:')
# print(todo)

#
# # генерируем пустой одномерный массив
# array = [0]*5
# # выводим полученный массив
# print(array)
#
#



# # считываем количество строк массива
# rows = int(input('Введите количество строк массива: '))
# # считываем количество столбцов массива
# columns = int(input('Введите количество столбцов массива: '))
# # создаем пустой массив
# array = []
# # цикл по строкам массива
# for i in range(rows):
#     # каждая строка массива состоит из columns элементов
#     array.append([0]*columns)
# # выводим сгенерированный массив
# print(array)
#
#



# numbers = [[1,2,3],
#         [4,5,6],
#         [7,8,9],
#         [10,11,12]]
# # считываем номер строки элемента
# rows = int(input('Введите номер строки 0-3: '))
# # считываем номер столбца элемента
# columns = int(input('Введите номер столбца 0-2: '))
# # выводим элемент по заданному индексу
# print(f'Искомый элемент: {numbers[rows][columns]}')

# # считываем количество строк массива
# rows = int(input('Введите количество строк массива: '))
# # считываем количество столбцов массива
# columns = int(input('Введите количество столбцов массива: '))
# # создаем пустой массив
# array = []
#
# # цикл по строкам массива
# for i in range(rows):
#     # каждая строка массива состоит из columns элементов
#     array.append([0] * columns)
# # выводим сгенерированный массив
# print(f'Сгенерирован пустой массив: {array}')
#
# # Заполним массив элементами с помощью вложенного цикла for
# for i in range(rows):  # цикл по строкам
#     for j in range(columns):  # цикл по столбцам
#         print()
#         print(f'Строка:{i} Столбец:{j}')
#         array[i][j] = int(input(f'array[{i}][{j}] = '))
#
# # выводим заполненный массив
# print()
# print(f'Заполненный массив: {array}')





# numbers = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9],
#            [10, 11, 12]]
# # считываем искомое число
# num = int(input('Введите число: '))
# # флаг на наличие элемента в массиве
# in_array = False
#
# # цикл по строкам двумерного массива
# for array in numbers:
#     # если число есть в строке
#     if num in array:
#         # записываем в флаг значение Истина
#         in_array = True
#
# # Если число было в одной из строке
# if in_array:
#     print('Данное число есть в массиве')
# # Если числа не было ни в одной из строк
# else:
#     print('Данного числа в массиве нет')
#



numbers = [[1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]]
print(len(numbers))
# # считаем номер столбца, который нужно удалить
# column = int(input('Введите столбец, который нужно удалить 0-2:'))
# # цикл по элементам двумерного массива
# for a in numbers:
#     # удаляем элемент массива по индексу
#     a.pop(column)
# # выводим заполненный массив
# print(f'Полученный массив: {numbers}')
# # цикл по длине массива
# for i in range(len(numbers)):
#     # считываем элемент
#     num = int(input(f'Введите новое значение для {i} строки: '))
#     # добавляем полученный элемент по индексу column
#     numbers[i].insert(column, num)
# # выводим итоговый массив
# print(f'Итоговый массив: {numbers}')

#
# for i, array in enumerate(numbers):
#     num = int(input(f"Введите число для {i} строки")
#     array.insert(column, num)

#
# numbers = [1,2,3]
# n = int(input())
# if n in numbers:
#     print('да')
# else:
#     print('нет')


array = [1, 'd', 4, [], '12', 5, {1: 3}, 'game over']
print(sum(map(lambda x: isinstance(x, str), array)))



print(sum(isinstance(i, str) for i in array))

array = [3, 6, 31, 41, 67, 193]
number = 52
print(min(array, key=lambda x: abs(number - x)))

