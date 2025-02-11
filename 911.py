#
#
# a = 15**42
# print(a)
# print(120 // 12 == 120 / 12)
# print(True == 1)
#
# a = 10
# if a >= 10:
#         b = 1
# else:
#         b = 0
# print(b)
#
# a = 36
# b = a % 2
# if b == 0:
#    print('четное')
# else:
#    print('нечетное')
#
# my_variable = 11
# print(my_variable % 2 == 0)

#
# print(bin(-30 ** 1))
# print(oct(-30 ** 1))
import math
#
# seconds_since_birthdate = 757679845
# # if seconds_since_birthdate/365*24*60*60 < 200:
# if seconds_since_birthdate/(365*24*60*60) < 200:
#     print(math.floor(seconds_since_birthdate/(365*24*60*60)))
#
#
# a = "string"
# b = 'string'
# c = """string"""
# d = '''string'''
# print(a == b == c == d)
# print(a is b is c is d)
# text = "Привет Оля"
#
# print(text[7:])
# t = "abcdefghijk 1456 ahalai-mahalai! Восстань, сын трёхголового дракона!"
# if len(t) >= 42:
#     print(t[1:-1:2])
# else:
#     print(len(t))
#
# text = "mistake message: Ай, случилася беда!"
#
# template = 'message: '
# i = text.index(template)
# print(text[i + len(template):])  #начальный индекс элемена + дина элемента, чтобы вычислить с какго места будет срез
# print(i + len(template))
# print(i)
# text = "12435514234 ERROR index: big_terrible_mistake message: Ай, случилася беда!"
#
# template = 'e: '
# index = text.index(template)
# print(text[index + len(template):])

# text = "5423534 lajksdfij;jhh message: абракадабра dfasdfs9d6f7686"
#
# template = 'message: '
# index = text.find(template)
# if index != -1:
#     print(text[index + len(template):])

# string = 'geeks for geeks'
#
# # returns index value
# result = string.find('for')
# print("Substring for:", result)
#
# result3 = string.find("best")
# print("substring best:", result3)
#
# text = "12435514234 ERROR index: big_terrible_mistake message: Ай, случилася беда!"
#
# template = 'message: '
# if template in text:
#     index = text.index(template)
#     print(text[index + len(template):])
#
# word = "стоять"
#
# if word.endswith("ь"):
#     print("Это существительное женского рода:", word)
#
# s = "Python is a great programming language"
# print(len(s))
# print(s.endswith("language"))  # True
# print(s.endswith("Python"))  # False
# print(s.endswith(("Python", "language")))  # True (checking multiple suffixes)
#
#
t= 'b645m7km76tn3w4(*&(%^%*T(🂦 🂧 🂨 🂩 🂪 🂫*uiovjty_8_'
# t= ""
# print(t.isascii())
# rt = t.isascii()
# print(len(t))
# if len(t) == 0:
#     print("false")
#     # print(rt)
#
# else:
#     print(t.endswith('8_'))
#
# a = ["ddfgh", "типа", "паывтипакафцум", "типа", "выуатек", "нек", "типа"]
# print(a.count("типа"))

#
# text = "В мире нет ни чего приятнее чем поспать до ОБЕДА"
# prepared_text = text.casefold().replace(' ', '')
# print(prepared_text)
# print(prepared_text[::-1])
# print(prepared_text == prepared_text[::-1])
#
# a = 'Три утёнка по три раза тёрли лапки потрёпанными мочалками и крякали друг другу: „смотри, мои лапки чище твоих!“ Смотри, утёнок, насквозь не протри!'
# print(a.casefold().count("тр"))
#
# string = "Три утёнка по три раза тёрли лапки потрёпанными мочалками и крякали друг другу: „смотри, мои лапки чище твоих!“ Смотри, утёнок, насквозь не протри!"
# substring = "Тр"
# print(string.count(substring))
#
# print('--+-- Запись номер 1 --+--'.removesuffix("--+--"))
#
#
# text = "Привет World"
# result = text.removesuffix(".jpg")
# print(result)  # Полученный результат: «Привет, Мир» [4](https://tr-page.yandex.ru/translate?lang=en-ru&url=https%3A%2F%2Fwww.tutorialspoint.com%2Fpython%2Fremovesuffix_method.htm)
#
# text = "Hello World"
# result = text.removesuffix(".jpg")
# print(result)  # Вывод: «Привет, Мир» [4](https://tr-page.yandex.ru/translate?lang=en-ru&url=https%3A%2F%2Fwww.tutorialspoint.com%2Fpython%2Fremovesuffix_method.htm)

#
# string = "Да чтоб тебя таращило!, Где мои деньги???, Тестовый текст 3(!)"
# x = string.split(',')
# print(x)
# # t = x.rstrip('!().?')
# # print(t)
# print(string.strip('!().?'))
# h = '(Что бы это ни значило :)'
# print(", блин, ".join(h))
# splitted = "Вася нехороший человек занял три рубля и отказывается отдавать!".split()
# print(", блин, ".join(splitted))
#     # 'Вася, блин, нехороший, блин, человек, блин, занял, блин, три, блин, рубля, блин, и, блин, отказывается, блин, отдавать!'
# name, author = "Незнайка", "Николай Носов"
# print("{:%<30} х {:%>30}".format(name, author))

# name = "Алиса"
# author = "Иванов"
# sentence = "Меня зовут {} и я живу в {}.".format(name, author)
# print(sentence)  # Вывод: Меня зовут Алиса и я живу в Иванов [1](https://pyhub.ru/python/lecture-5-12-26/)
#
#
# text = "один два три четыре пять шесть"
# print(text.split(' ',2))  # ['один', 'два', 'три четыре']
# #
# car_cost = 120000
# manager, count = "Петров", 12
# #
# print("Продажи автомобилей в прошлом месяце:")
# print(f"Менеджер {manager} продал {count} автомобилей, что принесло {car_cost * count} единиц валюты.")
#
# r = 15
# r2 = r*r/10000
# h = 10
# p = 3.14
# print("объем цилиндра равен:")
# print(f"радиус в квадрате {r/100*r/100}  * высота {h}  * пи {p} ответ {r2*h*p:.2f}" )
          # {sqr(r/100)*h*p:.3f}.")
# import math
#
#
# radius = 15
# height = 10
# print("{:.2}".format(math.pi * height * (radius/100) ** 2))
# spade_cards = "🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂬 🂭 🂮"
#
# print(spade_cards)
# a = "star"
# b = a
# c = 'star'
# print(a == b == c)
#
# a = 20**50
# b = str(a)
# print(len(b))
#
# print("1"<"2")
#
# string = "Три утёнка по три раза тёрли лапки потрёпанными мочалками и  крякали друг другу: „смотри, мои лапки чище твоих!“ Смотри, утёнок, насквозь не протри!".split()
# substring = " "
# print(string.count(substring))
# print(len(string))
# print(string)
#
# s = "Это наш пример строки"
# words = s.split()
# num_words = len(words)
# print(num_words)
#
# data = input()
# print(data * 5)
#
# import sys
#
# data = sys.stdin.readline()
# print(data * 5)

# import sys
#
# line = sys.stdin.readline()
# # Удаление завершающего символа новой строки
# line = line.strip(',.')
# print(f"Received: {line}")

# txt = ',.banana,.'
#
# x = txt.strip(',.')
#
# print('of all fruits', x, 'is my favorite') # => of all fruits, banana, is my favorite


# name = input("Введите IP-адрес: ")
# d = name.split('.')
# print("_".join(d))
#
# import sys
#
# sys.stdout.write("Привет, кожаный мешок!\n")
#
# print("Эта строка плавно переходит", end="")
#
# print(" в следующую строку.")
#
# # name1 = oct(input())
# name2 = input("Введите первое число:")
# name3 = input("Введите первое число: ")
# name4 = input("Введите первое число: ")
# a = input("Введите восьмеричное число>")
# print(int(name2, 0), int(name3, 0), int(name4, 0), int(a, 0), sep = ".")
# # print(int("name1"))
# binary_number = "1010"
# decimal_number = int(binary_number, 2)
# print(decimal_number)
#
# num1 = input("Введите первое восьмеричное число: ")
# num2 = input("Введите второе восьмеричное число: ")
# num3 = input("Введите третье восьмеричное число: ")
# num4 = input("Введите четвёртое восьмеричное число: ")
# print(f"{int(num1, 8)}.{int(num2, 8)}.{int(num3, 8)}.{int(num4, 8)}")
#
#
# def recursive_func(n=0):
#    print('Вывод до запуска рекурсии: ', n)
#    if n < 3:
#        recursive_func(n + 1)
#    print('Вывод после запуска рекурсии: ', n)
#
#
# recursive_func()
#
#
#
#
#
# def factorial(n):
#    # Базовый случай
#    if n == 0:
#        return 1
#
#    # Рекурсивный случай
#    else:
#        return n * factorial(n-1)
#
# print(factorial(3))
# class Node:
#    def __init__(self, value, children=None):
#        self.value = value
#        self.children = children if children else []
# root = Node(5, [
#    Node(3, [
#        Node(1),
#        Node(4)
#    ]),
#    Node(2, [
#        Node(6),
#        Node(1)
#    ])
# ])
#
#
# # Получение значения в узле-корне
# print(root.value)
# # 5
#
# # Получение значений дочерних узлов
# print(root.children[0].value, root.children[1].value)
# # 3 2
#
# # Получение значений листьев
# print(root.children[0].children[0].value, root.children[0].children[1].value)
# print(root.children[1].children[0].value, root.children[1].children[1].value)
# # 1 4
# # 6 -1
#
#
# def test_tree_structure(node):
#     # у node есть  value — значение
#     # и children — список других node
#
#     # Базовый случай
#     if node.value < 0:
#         return False
#
#     # Рекурсия
#     for child in node.children:
#         if not test_tree_structure(child):
#             return False
#
#     return True
#
#
#
# # Тестируем наше дерево
# print(test_tree_structure(root))
# # False
#
#
# def fibonacci(n):
#    # Базовый случай
#    if n <= 0:
#        return 0
#
#    if n == 1:
#        return 1
#
#    # Рекурсивный случай
#    else:
#        return fibonacci(n-1)+fibonacci(n-2)
#
# print(fibonacci(5))
# #5
# print(fibonacci(7))
# #13
# print(fibonacci(8))
# #21
#
# def is_palindrome(n):
#    # Базовый случай
#    if n <= 0:
#        return 0
#
#    if n == 1:
#        return 1
#
#    # Рекурсивный случай
#    else:
#        return fibonacci(n-1)+fibonacci(n-2)
#
#
# def is_palindrome(s):
#     s_lower = s.lower()
#     if len(s_lower) < 2: return True
#     if s_lower[0] != s_lower[-1]: return False
#     return is_palindrome(s_lower[1:-1])







# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s == s[-1]:
#         return False
#     return is_palindrome(s[::-1])

# print(is_palindrome('racecar'))
# # True
# print(is_palindrome('gong'))
# # False

#
#
#
# def binary_search(arr, x, low = 0, high = 4):
#
#
#     # Check base case
#     if high >= low:
#
#         mid = low + (high - low) // 2
#
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return True
#
#         # If element is smaller than mid, then it
#         # can only be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, x,low, mid-1)
#             if arr[mid-1] ==x:
#                 return True
#
#         # Else the element can only be present
#         # in right subarray
#         else:
#             return binary_search(arr, x, mid+1, high)
#             if arr[mid+1] ==x:
#                 return True
#
#
#
#
#
#     # Element is not present in the array
#     else:
#         return False
#
#
# print(binary_search([1, 2, 3, 4, 5], 4))
# True
# print(binary_search([1, 2, 3, 4, 5], 6))
# # False
#
#
# s=[1, 2, 3, 4, 5]
# print(len(s))
# d = len(s)-1
# print(d)



x = (n**2 for n in range(1, 6))
print(sum(x))


# print(next(x))
# # 1
# print(next(x))
# # 4
# print(next(x))
# # 9
# print(next(x))
# # 16
# print(next(x, None))
# print(next(x, None))
# # None
# x = (n**2 for n in range(1, 6))
# for n in x:
#    print(n)
# # 1
# # 4
# # 9
# # 16
#
# # very_big_data = (n for n in range(1000000000000))
# # for n in very_big_data:
# #    print(n, end=' ')
# #    if n == 100:
# #        break
#
#
# very_big_data = (n for n in range(10000))
# very_big_data = list(very_big_data)
# print(type(very_big_data), len(very_big_data))
#
#
# def generate_test_data(n):
#    for i in range(n):
#        yield f"test_data_{i}"
#
#
# test_data = generate_test_data(10)
# print(test_data)
#
# print(next(test_data))
# # test_data_0
# print(next(test_data))
# # test_data_1
# # И так далее, пока не закончатся элементы...
#
#
# test_data = generate_test_data(10)
#
# for test in generate_test_data(10):
#    print(test)
#
#
#
#
# def generate_combinations(colors, sizes):
#    for color in colors:
#        for size in sizes:
#            yield color, size
#
#
# combination_generator = generate_combinations(["red", "blue"], ["small", "large"])
# for combination in combination_generator:
#    print(combination)
# # ('red', 'small')
# # ('red', 'large')
# # ('blue', 'small')
# # ('blue', 'large')
#
# combination_generator = ((color, size) for size in ["small", "large"] for color in ["red", "blue"])
# for n in combination_generator:
#    print(n)
# def generate_urls(g, x,y):
#     j= (f'{g}{n}' for n in range(x,y+1))
#     return j
#
#
#
#
# url_generator = generate_urls("/product/", 1, 3)
# for url in url_generator:
#    print(url)
# # /product/1
# # /product/2
# # /product/3
#
# print(list(generate_urls("https://example.com/page_", 1, 5)))




#
# import random
# #
# def generate_user_data(g, first_names,last_names, m):
#     q= int(m[0])
#     a =int(m[1])
#     very_big_data = (n for n in range(q,a))
#     very_big_data = list(very_big_data)
#
#     jj = [random.choice(first_names) for n in range(g)]
#     hh = [random.choice(last_names) for n in range(g)]
#     kk = [random.choice(very_big_data) for s in  range(g)]
#     for (j, h, k) in zip(jj, hh, kk):
#         yield j, h, k
#
#
#
# first_names = ["Alice", "Bob", "Charlie"]
# last_names = ["Smith", "Johnson", "Williams"]
# user_data_generator = generate_user_data(5, first_names, last_names, [18, 60])
# for user in user_data_generator:
#    print(user)
# ('Charlie', 'Williams', 19)
# ('Charlie', 'Johnson', 48)
# ('Bob', 'Johnson', 26)
# ('Charlie', 'Smith', 36)
# ('Charlie', 'Johnson', 35)
# very_big_data = ['hgfh', 'gdf', 'dfsdf', 'sf']
# for i in range(g):
# j = list(( n for n in random.choice(first_names)))
# for first_name in first_names:
#     l = random.choice(first_names)
# h = (l for l in random.choice(last_names))
# for random.choice(last_names) in last_names:
# k =list ((s for s in random.choice(very_big_data)))
# for random.choice(m) in m:

# print(l)
# print(random.choice(last_names))
#
#
#
# def func(...):
#    # Какой-то набор операций здесь
#    for _ in range(...):
#        # Генерируем значение последовательности и останавливаем функцию
#        yield ...
#        # Код здесь выполнится при последующем вызове функции (генерации нового элемента)
#    # И код здесь выполнится при последующем вызове функции (генерации нового элемента)

# def fibonacci(n):
#    # Базовый случай
#    if n <= 0:
#        k =[]
#        return k
#
#    if n == 1:
#        k = [0]
#        return k
#
#    # Рекурсивный случай
#    else:
#        k=[0,1]
#        for i in range(n):
#            k.append(n-1+n-2)
#
#
#
#
#
# test1 = list(fibonacci(15))
#
#
#
# print(test1)
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(1)))

import math

def primes(x):
    prs = {}
    p = 2
    while p-1 < x:
        if p not in prs:
            yield p
            prs[p * p] = [p]
        else:
            for s in prs[p]:
                prs.setdefault(s + p, []).append(s)
            del prs[p]

        p += 1
print(list(primes(0)))


# # создаем словарь
# translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
#
# # выводим словарь в консоль
# # ключи словаря - метод keys()
# print(f'Ключи словаря: {translator.keys()}')
# # значения словаря - метод values()
# print(f'Значения словаря: {translator.values()}')
# # пары ключ:значение - метод items()
# print(f'Пары ключ:значение словаря: {translator.items()}')




# # создаем словарь
# translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
# print(f'Исходный словарь: {translator}')
#
# # добавляем новую запись в словарь
# translator['tester'] = 'тестировщик'
# print(f'Словарь с новой записью: {translator}')
#
# # редактируем запись в словаре
# translator['tester'] = 'тестер'
# print(f'Словарь с отредактированной записью: {translator}')




# # создаем словарь
# translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
# # выводим английские слова, которые сохранены в словаре
# print(f'Слова в словаре: {translator.keys()}')
#
# # считываем слово, которое нужно перевести
# eng_word = input('Введите слово, которое нужно перевести: ')
# # выводим элемент словаря, полученный по ключу
# print(f'{eng_word} - {translator[eng_word]}')


#
#
#  # создаем словарь
# translator = {'bug':'ошибка', 'function':'функция', 'approve':'согласовать'}
# # удаляем элемент словаря с ключом bug
# del translator['bug']
# # выводим полученный словарь
# print(f'Полученный словарь: {translator}')
#
#
#
#
# # создаем словарь
# translator = {'bug':'ошибка', 'function':'функция', 'approve':'согласовать'}
# # удаляем элемент словаря с ключом function и выводим его
# print(translator.pop('function'))
# # выводим полученный словарь
# print(f'Полученный словарь: {translator}')



#
# # создаем словарь
# translator = {'bug':'ошибка', 'function':'функция', 'approve':'согласовать'}
# print(f'Исходный словарь: {translator}')
# # считываем слово, которое нужно удалить
# eng_word = input('Введите слово, которое хотите удалить: ')
# # если введенное слово есть в списке ключей словаря
# if eng_word in translator.keys():
#     print(f'Удаляем из словаря: {eng_word} - {translator[eng_word]}')
#     # удаляем элемент словаря с ключом eng_word
#     del translator[eng_word]
# else:
#     print('Этого слова в словаре нет')
# # выводим полученный словарь
# print(f'Полученный словарь: {translator}')
#
#
#
#
#
# # создаем словарь
# translator = {'bug':'ошибка', 'function':'функция', 'approve':'согласовать'}
# print('Исходный словарь:')
# # цикл по элементам словаря
# for key, value in translator.items():
#     # выводим пары ключ - значение
#     print(f'{key} - {value}')

#
#
# num1 = [1, 2, 3, 4, 5, 6, 7]
# num2 = [1, 2.0, 3.1, 4, 5, 6, 7.9]
# print(all([type(x) is int for x in num1]))
# # True
# print(all([type(x) is int for x in num2]))
# # False
# lis_1=[['0','0','0'],['4','5','6'],['7','7','7']]
