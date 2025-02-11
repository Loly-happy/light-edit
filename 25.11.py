numbers_tuple = (1, 2, 3, 4, 5, 6)
numbers_list = [1, 2, 3, 4, 5, 6]

# определим размер с помощью .__sizeof__()
print(f'''Размер кортежа: {numbers_tuple.__sizeof__()}
      Размер списка: {numbers_list.__sizeof__()}''')

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# срез всего кортежа
# start=0 stop=10 step=1
print(numbers[:])

# срез c нулевого по пятый элемент кортежа
# start=0 stop=5 step=1
print(numbers[:5])

# срез c первого по последний элемент кортежа
# start=1 stop=10 step=1
print(numbers[1:])


# срез с третьего по шестой элемент кортежа
# start=3 stop=6 step=1
print(numbers[3:6])

# каждый второй элемент кортежа (четные индексы)
# start=1 stop=10 step=2
print(numbers[1::2])

# user = ('Michael', 'Scott', 40)
#
# # разложим кортеж на отдельные переменные
# name, surname, age = user
# print(name)
# print(surname)
# print(age)
#
#
# numbers = {}
#     # выведем тип полученной переменной с помощью type()
# print(type(numbers))
#
#
# numbers = {1, 1, 2, 2, 3, 4, 5}
#
# num = int(input('Введите число: '))
# if num in numbers:
#     print('Это число есть во множестве.')
# else:
#     print('Этого числа нет во множестве.')
#
#  numbers = {1, 1, 2, 2, 3, 4, 5}
# # перебор элементов множества
# for elem in numbers:
#     print(elem)
#
#
# numbers = {1, 1, 2, 2, 3, 4, 5}
#         # добавим элемент в множество
# numbers.add(6)
# print(numbers)
#
# numbers = {1, 1, 2, 2, 3, 4, 5}
# # удалим элемент из множества
# numbers.remove(1)
# print(numbers)



family = ('Оля', 'Дима', 'Вася', 'Каспер', 'Тайсон', 'Буся')

# вывести первый и последний элемент списка
print(f'''Первый элемент кортежа {family[0]}
            Последний элемент кортежа {family[-1]}''')



# вывести каждый второй элемент списка
print(family[1::2])

# вывести длину списка
print(f'Длина кортежа: {len(family)}')



numbers = {0,5,1,2,4,5,8,3,6,4,1,2,2}

# добавить новый элемент в список
n = int(input('Введите число: '))


if n in numbers:
    numbers.remove(n)
    print('Этот элемент удален из множества')
else:
    numbers.add(n)
    print('Этот элемент добавлен во множество')
print(f'Длина множества: {len(numbers)}')
