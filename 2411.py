# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # срез всего списка
# # start=0 stop=10 step=1
# print(numbers[:])
#
# # срез c нулевого по пятый элемент списка
# # start=0 stop=5 step=1
# print(numbers[:5])
#
# # срез c первого по последний элемент списка
# # start=1 stop=10 step=1
# print(numbers[1:])
#
# # срез с третьего по шестой элемент списка
# # start=3 stop=6 step=1
# print(numbers[3:6])
#
# # каждый второй элемент списка (нечетные индексы)
# # start=1 stop=10 step=2
# print(numbers[1::2])
#
# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # выведем исходный список
# print(clients)
#
# # добавим новый элемент в список
# clients.append('Oscar Martinez')
#
# # выведем получившийся список
# print(clients)
#
# # считаем имя клиента с консоли
# new_client = input('Введите имя клиента: ')
# # добавим этого клиента в список
# clients.append(new_client)
#
# # выведем итоговый список
# print(clients)
#
# #
# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# print('Клиенты нашей компании:')
# # находим длину списка и вставляем её в метод range()
# for i in range(len(clients)): # i = [0, 1, 2, 3, 4]
#  print(f'{i+1}. {clients[i]}')
#
#  import random
#
#  # генерируем случайное число от 1 до 10
#  number = random.randint(1, 10)
#
#  # пользователь вводит число
#  guess = int(input('Введите число: '))
#
#  # проверка условий
#  if guess == number:  # если числа равны - пользователь угадал
#      print('Поздравляю, вы угадали!')
#  else:  # в противном случае числа не равны - пользователь не угадал
#      print(f'Вы не угадали, загаданные число {number}')
#
#      # список клиентов, участвующих в бонусной программе
# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert','Pam Beesly', 'Kevin Malone']
#
#      # считываем имя клиента
# client_name = input('Введите имя клиента: ')
#
#      # проверяем, есть ли введенный клиент в списке участников
# if client_name in clients:
#     print('Клиент является участником бонусной программы')
# else:
#     print('Клиент еще не участвует в бонусной программе. Добавляем его в список участников.')
#     clients.append(client_name)
#
# print(f'Всего участников бонусной программы: {len(clients)}')
# print(f'Список участников: {clients}')


coworkers = ['Галя', 'Алена', 'Катя','Лиля', 'Алия']
print(coworkers[0],coworkers[-1])
print(coworkers[0::2],coworkers[1::2])
print(f'Всего коллег: {len(coworkers)}')


coworkers_name = input('Введите имя коллеги: ')
coworkers.append(coworkers_name)
print(f'Список коллег: {coworkers}')


coworkers_name = input('Введите имя: ')
if coworkers_name in coworkers:
     print('Это ваш коллега')
else:
     print('Это не ваш коллега')

coworkers = ['Мария', 'Ангелила', 'Антонина', 'Дарья', 'Екатерина']

# вывести первый и последний элемент списка
print(f'''Первый элемент списка {coworkers[0]}
            Последний элемент списка {coworkers[-1]}''')

# вывести каждый первый элемент списка
print(coworkers[::2])

# вывести каждый второй элемент списка
print(coworkers[1::2])

# вывести длину списка
print(f'Длина списка: {len(coworkers)}')

# добавить новый элемент в список
name = input('Введите имя нового коллеги: ')
coworkers.append(name)
# вывести длину списка
print(f'Длина списка: {len(coworkers)}')

# проверить наличие элемента в списке
name = input('Введите имя коллеги: ')
if name in coworkers:
    print('Этот коллега есть в списке')
else:
    print('Такого имени в списке нет')

#      # считываем имя клиента
# client_name = input('Введите имя клиента: ')
#
#      # проверяем, есть ли введенный клиент в списке участников
# if client_name in clients:
#     print('Клиент является участником бонусной программы')
# else:
#     print('Клиент еще не участвует в бонусной программе. Добавляем его в список участников.')
#     clients.append(client_name)
#
# print(f'Всего участников бонусной программы: {len(clients)}')
# print(f'Список участников: {clients}')