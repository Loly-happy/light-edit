# import random
# from os import remove
#
# students = ['Андрей','Ольга','Светлана','Дмитрий','Елена']
# students.sort()
# classes = ['Геометрия','Физики','Химия','Биология']
# students_marks = {}
# for student in students:
#     students_marks[student]={}
#     for clas in classes:
#         marks = [random.randint(2,5) for i in range(3)]
#         students_marks[student][clas] = marks
# for student in students:
#     print(f'''{student}
#             {students_marks[student]}''')
#
#
# print('''Список команд:
#         1. Добавить оценку ученика по предмету
#         2. Вывести средний балл по всем предметам по каждому ученику
#         3. Вывести все оценки по всем ученикам
#         4. Удаление и редактирование по всем данным
#         5. Выход из программы''')
#
# while True:
#
#     command = int(input('Введите команду: '))
#     if command == 1:
#
#
#         print('Добавте оценку ученику по предмету')
#         student = input('Введите имя ученика: ')
#         clas = input('Введите название предмета: ')
#         mark = int(input('Введите оценку: '))
#         if student in students_marks.keys() and clas in students_marks[student].keys():
#             students_marks[student][clas].append(mark)
#             print(f'Для {student} по предмету {clas} добавлена оценка {mark}')
#         else:
#             print('ОШИБКА: неверное имя ученика или название предмета')
#
#     elif command == 2:
#         for student in students:
#             print(student)
#             for clas in classes:
#                 # находим сумму оценок по предмету
#                 marks_sum = sum(students_marks[student][clas])
#                 # находим количество оценок по предмету
#                 marks_count = len(students_marks[student][clas])
#                 # выводим средний балл по предмету
#                 print(f'{clas} - {marks_sum//marks_count}')
#             print()
#
#
#     elif command == 3:
#         for student in students:
#             print(student)
#             # цикл по предметам
#             for clas in classes:
#                 print(f'\t{clas} - {students_marks[student][clas]}')
#             print()
#
#     elif command == 4:
#         print('''Список команд:
#                 6 Удалить, редактировать ученика
#                 7 Удалить, редактировать предмет
#                 8 Удалить, редактировать оценки
#                 9 Выход из подпрограммы''')
#         command = int(input('Введите команду: '))
#         while True:
#             if command == 6:
#                 student = input('Введите имя ученика, которого нужно удалить или отредкатировать: ')
#                 if student in students_marks.keys():
#                     x = input('Если ученик нужна удалить, введите да, если отредактировать, введите нет: ')
#                     if x == "да":
#                         students.remove(student)
#                         del students_marks[student]
#                         print(f'запись ученика {student} удалена')
#                         break
#                     else:
#                         name = input('Введите новое имя ученика: ')
#                         i = students.index(student)
#                         students.remove(student)
#                         students.insert(i, name)
#                         print(students)
#
#                         # dictionary[new_key] = dictionary.pop(old_key)
#
#                         students_marks[name] = students_marks.pop(student)
#                         print(f'запись ученика {student} отредактирована')
#                         print(students_marks)
#                         break
#
#
#                 else:
#                     print('Этого ученика в списке нет')
#
#             elif command == 7:
#                 clas = input('Введите название предмета, которое нужно удалить или отредкатировать: ')
#                 if clas in students_marks[student].keys():
#                     x = input('Если предмет нужно удалить, введите да, если отредактировать, введите нет: ')
#                     if x == "да":
#                         classes.remove(clas)
#                         print(classes)
#                         for student in students:
#                             del students_marks[student][clas]
#                         print(f'предмет {clas} удален')
#                         print(students_marks)
#                         break
#                     else:
#                         name = input('Введите новый предмет: ')
#                         i = classes.index(clas)
#                         classes.remove(clas)
#                         classes.insert(i, name)
#                         print(classes)
#
#                         # dictionary[new_key] = dictionary.pop(old_key)
#                         for student in students:
#                             students_marks[student][name] = students_marks[student].pop(clas)
#                         print(f'предмет {clas} отредактирован')
#                         print(students_marks)
#                         break
#
#             elif command == 8:
#                 student = input('Введите имя ученика, которому нужно изменить оценки')
#                 clas = input('Введите предмет по которому нужно изменить оценки ')
#                 if student in students_marks.keys() and clas in students_marks[student].keys():
#                     x = input('Если оценки нужно удалить, введите да, если изменить, введите нет: ')
#                     if x == "да":
#                         i = int(input('Введите индекс оценки: '))
#                         students_marks[student][clas].pop(i)
#                         print('оценка удалена')
#
#                         print(students_marks)
#                         break
#                     else:
#                         i = int(input('Введите индекс оценки: '))
#                         m = int(input('Введите оценку'))
#                         students_marks[student][clas].pop(i)
#                         students_marks[student][clas].insert(i, m)
#
#                         print('оценка изменена')
#                         print(students_marks)
#                         break
#
#
#                 else:
#                     print('Этого ученика в списке нет')
#             elif  command == 9:
#                 print('9. Выход из подпрограммы')
#                 break
#
#
#
#
#
#
#
#     elif command == 5:
#         print('4. Выход из программы')
#         break
from os.path import split
#
#
#
#
# def make_account(balance):
#     def deposit(amount):
#         nonlocal balance
#         balance += amount
#         return balance
#
#     def withdraw(amount):
#         nonlocal balance
#         if amount > balance:
#             return "Insufficient funds"
#         balance -= amount
#         return balance
#
#     return deposit, withdraw
#
# deposit, withdraw = make_account(100)
# print(deposit(15))
# # 115
# print(withdraw(30))
# # 85
#
#
# def create_counter():
#     i = 0
#
#     def func():
#         nonlocal i
#         i += 1
#         return i
#
#     return func
#
#
# counter = create_counter()
# print(counter())  # 1
# print(counter())  # 2
# print(counter())  # 3
#
#
# def create_unique_checker():
#     i = list()
#
#     def func(x):
#         nonlocal i
#         i.append(x)
#         if len(set(i)) < len(i) :
#             i.pop()
#             return False
#         else:
#             return True
#
#
#     return func
#
#
#
# unique_checker = create_unique_checker()
# print(unique_checker(0))
# print(unique_checker(0))
# print(unique_checker(10))
#
# # True
# # False
# # True
#
#
#
#
#
#
# # Вывод:
# # 0
# # 2
# import time
# def timer():
#
#     # seconds = time.time()
#     # result = time.localtime(seconds)
#
#     local_time = time.time()
#
#     def func()  :
#         nonlocal local_time
#         # local_time = result.tm_sec
#         # s = time.mktime(result)
#         local_time1 = time.time()
#         f = local_time1 - local_time
#
#         return f
#     return func
#
# my_timer = timer()
# print(int(my_timer())) # int — для приближенного значения секунд
# # Ждем немного...
# time.sleep(10)
# print(int(my_timer()))
# import random
# def create_password_generator(f, h):
# #
#
#     ssss = list(h)
#
#
#     def func()  :
#         nonlocal f, ssss
# #         y = random.shuffle(ssss)
#         password=[]
#         for i in range(f):
#             k = random.choice(ssss)
#             password.append(k)
#             random.shuffle(password)
#         password_and = ''.join(password)
#         return password_and
# #
# #
#     return func
#
#
#
#
#
#
# symbols_for_password = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#
#
#
# password_generator = create_password_generator(10, symbols_for_password)
# print(password_generator())
# print(password_generator())

# Stl0tgwWSL
# oboYrgROdF
# def decorator(func):
# 	print("Делаем что-то перед вызовом функции — изменяем её поведение")
# 	func()
# 	print("Делаем что-то после вызова функции — изменяем её поведение")
#
# # Делаем "основную" функцию, поведение которой будем менять
# def demo_func():
# 	print('Работает целевая функция')
#
# changed_function = decorator(demo_func)
# # После этой строчки выведется следующее:
# # Делаем что-то перед вызовом функции — изменяем её поведение
# # Работает целевая функция
# # Делаем что-то после вызова функции — изменяем её поведение
#
#
# def decorator(func):
#     # Реализуем принцип Замыкания
#     def wrapper():
#         print("Делаем что-то перед вызовом функции -- изменяем её поведение")
#         func()
#         print("Делаем что-то после вызова функции -- изменяем её поведение")
#     return wrapper
#
# # Делаем "основную" функцию, поведение которой будем менять
# def demo_func():
#     print('Работает целевая функция')
#
# changed_function = decorator(demo_func)
#
# changed_function()
# # Делаем что-то перед вызовом функции -- изменяем её поведение
# # Работает целевая функция
# # Делаем что-то после вызова функции -- изменяем её поведение
#
#
# def decorator(func):
#     def wrapper(parameter):
#         print("Делаем что-то перед вызовом функции -- изменяем её поведение")
#         func(parameter)
#         print("Делаем что-то после вызова функции -- изменяем её поведение")
#     return wrapper
#
# def demo_func(parameter):
#     print('Работает целевая функция c параметром(-ами):')
#     print(parameter)
#
# changed_function = decorator(demo_func)
#
# changed_function('Параметр декорированной функции')
# # Делаем что-то перед вызовом функции -- изменяем её поведение
# # Работает целевая функция c параметром(-ами):
# # Параметр декорированной функции
# # Делаем что-то после вызова функции -- изменяем её поведение
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Делаем что-то перед вызовом функции -- изменяем её поведение")
#         func(*args, **kwargs)
#         print("Делаем что-то после вызова функции -- изменяем её поведение")
#     return wrapper
#
# def demo_func(parameter1, parameter2):
#     print('Работает целевая функция c параметром(-ами):')
#     print(parameter1)
#     print(parameter2)
#
# changed_function = decorator(demo_func)
#
# changed_function('Параметр декорированной функции_1',
#                 'Параметр декорированной функции_2')
#
# # Делаем что-то перед вызовом функции -- изменяем её поведение
# # Работает целевая функция c параметром(-ами):
# # Параметр декорированной функции_1
# # Параметр декорированной функции_2
# # Делаем что-то после вызова функции -- изменяем её поведение
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Делаем что-то перед вызовом функции -- изменяем её поведение")
#         res = func(*args, **kwargs)
#         print("Делаем что-то после вызова функции -- изменяем её поведение")
#         return res + ' + Изменяем возвращаемое значение в wrapper'
#     return wrapper
#
# def demo_func(parameter1, parameter2):
#     print('Работает целевая функция c параметром(-ами):')
#     print(parameter1)
#     print(parameter2)
#     return 'Возвращаемое значение оригинальной функции'
#
#
# changed_function = decorator(demo_func)
#
# result = changed_function('Параметр декорированной функции_1',
#                 'Параметр декорированной функции_2')
# print(result)
#
# # Делаем что-то перед вызовом функции -- изменяем её поведение
# # Работает целевая функция c параметром(-ами):
# # Параметр декорированной функции_1
# # Параметр декорированной функции_2
# # Делаем что-то после вызова функции -- изменяем её поведение
# # Возвращаемое значение оригинальной функции + Изменяем возвращаемое значение в wrapper
#
#
# import time
# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         work_time = time.time() -- start_time
#         print(f'Функция {func.__name__} отработала за {work_time} секунд')
#         return res
#     return wrapper
#
# @timeit
# def large_sum(n):
#     return sum(range(n))
# @timeit
# def prime_numbers(n):
#     primes = []
#     for possiblePrime in range(2, n):
#         isPrime = True
#         for num in range(2, int(possiblePrime ** 0.5) + 1):
#             if possiblePrime % num == 0:
#                 isPrime = False
#         if isPrime:
#             primes.append(possiblePrime)
#     return primes
#
# test_data = 193700
#
# prime_numbers = prime_numbers(test_data)
# # Функция prime_numbers отработала за 2.0152699947357178 секунд
#
# result = large_sum(test_data)
# # Функция large_sum отработала за 0.004996538162231445 секунд
#
# @timeit
# def power_sum(n, p):
#     """Функция возвращает сумму первых n чисел, возведенных в степень p."""
#     return sum(i**p for i in range(n))
#
# result = power_sum(10000, 2)
# # Функция power_sum отработала за 0.002002239227294922 секунд
# print(result)
# # 333283335000
#
#
# import time
# def timeit(func):
#     call_stack = []
#     def wrapper(*args, **kwargs):
#         call_stack.append(None)
#         if len(call_stack) == 1:  # Если это изначальный вызов
#             start_time = time.time()
#             result = func(*args, **kwargs)
#             work_time = time.time() -- start_time
#             print(f'Функция {func.__name__} отработала за {work_time} секунд')
#         else:  # Если это рекурсивный вызов
#             result = func(*args, **kwargs)
#         call_stack.pop()
#         return result
#
#     return wrapper
#
# @timeit
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# factorial(155)
# # Функция factorial отработала за 0.00095367431640625 секунд
#
#
# import time
# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         work_time = time.time() -- start_time
#         print(f'Функция {func.__name__} отработала за {work_time} секунд')
#         print(f'args: {args}')
#         print(f'kwargs: {kwargs}')
#         return res
#     return wrapper
#
# @timeit
# def prime_numbers(n):
#     ...
#
# for i in range(1, 10000, 2000):
#     prime_numbers(i)
#
#
#
# # Функция prime_numbers отработала за 0.0 секунд
# # args: (1,)
# # kwargs: {}
# # Функция prime_numbers отработала за 0.001998424530029297 секунд
# # args: (2001,)
# # kwargs: {}
# # Функция prime_numbers отработала за 0.00800180435180664 секунд
# # args: (4001,)
# # kwargs: {}
# # Функция prime_numbers отработала за 0.015002727508544922 секунд
# # args: (6001,)
# # kwargs: {}
# # Функция prime_numbers отработала за 0.029001951217651367 секунд
# # args: (8001,)
# # kwargs: {}
#
# import random
# import time
#
# def retry_on_failure(max_retries=3):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(max_retries):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f"Function {func.__name__} failed with error: {e}. Retrying...")
#                     time.sleep(1)
#             print(f"Function {func.__name__} failed after {max_retries} retries.")
#         return wrapper
#     return decorator
#
# @retry_on_failure(max_retries=5)
# def fragile_function(*args, **kwargs):
#     ...
#     if random.random() < 1:  # Специально делаем так, чтобы функция всегда поднимала ошибку
#         raise Exception("An error occurred")
#     else:
#         return "Success"
#
# # Запускаем функцию
# print(fragile_function())
#
# # Function fragile_function failed with error: An error occurred. Retrying...
# # Function fragile_function failed with error: An error occurred. Retrying...
# # Function fragile_function failed with error: An error occurred. Retrying...
# # Function fragile_function failed with error: An error occurred. Retrying...
# # Function fragile_function failed with error: An error occurred. Retrying...
# # Function fragile_function failed after 5 retries.
# # None



# import random
# import time
#
# def retry_if_result_is_none(m):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#
#
#             for _ in range(m):  # Операция повторяется до трёх раз [5]
#                 try:
#                     return func(*args, **kwargs)  # Выполняем критический код [5](https://sky.pro/wiki/python/povtornaya-popytka-iteratsii-pri-oshibke-v-python-tsikly-isklyucheniya/)
#                     break  # Успех! Прекращаем цикл [5](https://sky.pro/wiki/python/povtornaya-popytka-iteratsii-pri-oshibke-v-python-tsikly-isklyucheniya/)
#                 except YourException:  # Здесь указывается конкретное исключение [5](https://sky.pro/wiki/python/povtornaya-popytka-iteratsii-pri-oshibke-v-python-tsikly-isklyucheniya/)
#                     pass  # При обнаружении исключения делаем повторную попытку [5](https://sky.pro/wiki/python/povtornaya-popytka-iteratsii-pri-oshibke-v-python-tsikly-isklyucheniya/)
#                 else:
#                     raise  # Если после трёх попыток успех не достигнут, поднимаем исключение [5](https://sky.pro/wiki/python/povtornaya-popytka-iteratsii-pri-oshibke-v-python-tsikly-isklyucheniya/)
#
#
#
#             return wrapper
#         return decorator
#
#
# @retry_if_result_is_none(m)
# def test_function():
#     return random.choice([None, "Passed"])
#
# # Получилось получить значение за 2 вызова
# print(test_function())
# # Passed
#
# # Не получилось получить значение за 2 вызова
# print(test_function())
# # None
#
#
# def logger(function):
#     def wrapper(*args, **kwargs):
#         print(f"----- {function.__name__}: start -----")
#         function(*args, **kwargs)
#         print(f"----- {function.__name__}: end -----")
#         return function
#     return wrapper
#
# @logger
# def some_function(text):
#     print(text)
#
# some_function("first test")
# some_function("second test")
#
# import random
# def retry_if_result_is_none(times):
#     def decorate(func):
#
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorate
#
#
# @retry_if_result_is_none(times=2)
# def test_function():
#     return random.choice([None, "Passed"])
#
# # Получилось получить значение за 2 вызова
# print(test_function())
# # Passed
#
# # Не получилось получить значение за 2 вызова
# print(test_function())
# # None
#
# import random
#
# def ensure_result_is_number(func):
#
#     def wrapper(*args, **kwargs):
#         i=type(func(*args, **kwargs))
#         if  type(i) is int or float:
#             g = func(*args, **kwargs)
#
#             return g
#         else:
#             return None
#         return wrapper
#     return ensure_result_is_number
#
# @ensure_result_is_number
# def test_function():
#     return random.choice(["Passed", 10, "Failed", 5.5])
#
# # Функция вернула не int и не float
# print(test_function())
# # None
#
# # Функция вернула float
# print(test_function())
# print(test_function())
#
# # 5.5
#
# # Функция вернула int
# print(test_function())
#
# # 10


# from typing import List, Dict, Any
# from datetime import date
#
# def calculate_age(birth_date: str) -> int:
#     a = date.today()
#     c = str(a)
#     f = c.split('-')
#     x = birth_date.split('-')
#     if int(f[1]) < int(x[1]):
#         w = int(f[0]) - int(x[0]) - 1
#     else:
#         if int(f[2]) < int(x[2]):
#             w = int(f[0]) - int(x[0]) - 1
#         else:
#             w = int(f[0]) - int(x[0])
#     return w
#
#
# def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
#     a = date.today()
#     c = str(a)
#     f = c.split('-')
#     j=[]
#     for i in range(len(users)):
#         x = users[i-1]['birth_date'].split('-')
#         if int(f[1]) < int(x[1]):
#             w = int(f[0]) - int(x[0]) - 1
#         else:
#             if int(f[2]) < int(x[2]):
#                 w = int(f[0]) - int(x[0]) - 1
#             else:
#                 w = int(f[0]) - int(x[0])
#         if w >= 18:
#             j.append(users[i-1])
#     return j
#
#
#
# def generate_username(first_name: str, last_name: str) -> str:
#     s = first_name.casefold()
#     d = (f'{s[0:1]}.{last_name.casefold()}')
#     return d
# #     ...
# #
# print(calculate_age("1990-05-15"))
# # 33
# users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'},
#               {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'},
#               {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01'}]

# print(filter_adults(users_data))
# # # [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'}, {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'}]
# print(generate_username("John", "Doe"))
# # # "j.doe"
# first_name = "John"
# last_name = "Doe"
# d = (f'{first_name}.{last_name}')

#
# from typing import List, Dict, Any
# # А также вам наверняка может понадобиться модуль functools...
#
# def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
#     j = []
#     for i in range(len(users)):
#         x = users[i]['first_name']+' '+users[i]['last_name']
#         j.append(x)
#     return j
#
#
# def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
#     a = set()
#     for i in range(len(users1)):
#         x = list(users1[i - 1].values())
#         a.update(x)
#     b = list(users2[0].values())
#     h = list(a.intersection(b))
#     h = h[2]
#     d=set()
#     d.add(h)
#
#
#     return d
#
# #     ...
# def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
#     d=dict()
#     f = list()
#     g = list()
#     h = list()
#     j = list()
#     for i in range(len(users)):
#         f.append(users[i]['first_name'])
#         g.append(users[i]['last_name'])
#         h.append(users[i]['birth_date'])
#         j.append(users[i]['email'])
#     d['first_name'] = tuple (f)
#     d['last_name']=tuple(g)
#     d['birth_date']=tuple(h)
#     d['email']=tuple(j)
#     return d
#
#
#
#     ...
# users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
#               {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22', 'email': 'bobJ@gmail.com'},
#               {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01', 'email': 'lev46@gmail.com'},
#               {'first_name': 'Anna', 'last_name': 'Smith', 'birth_date': '1988-03-08',
#                'email': 'anna.smith@example.com'},
#                {'first_name': 'Emily', 'last_name': 'Brown', 'birth_date': '1993-11-28',
#                 'email': 'emily_brown@hotmail.com'}]
#
# users_data_ext = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
#                   {'first_name': 'Alex', 'last_name': 'Davis', 'birth_date': '2000-09-17',
#                    'email': 'alex.davis@gmail.com'},
#                   {'first_name': 'Maria', 'last_name': 'Martinez', 'birth_date': '1977-07-12',
#                    'email': 'maria.m@example.com'},
#                   {'first_name': 'Michael', 'last_name': 'Johnson', 'birth_date': '1972-04-05',
#                    'email': 'michaelj@example.net'}]
#
# to_test = [convert_to_full_name(users_data), find_matching_emails(users_data, users_data_ext), combine_user_data(users_data)]
#
# print(convert_to_full_name(users_data))
# # ['John Doe', 'Bob Johnson', 'Lev Sergeev']
# print(find_matching_emails(users_data, users_data_ext))
# # # {'johndoe@gmail.com'}
# print(combine_user_data(users_data))
# # # {'first_name': ('John', 'Bob', 'Lev'), 'last_name': ('Doe', 'Johnson', 'Sergeev'), 'birth_date': ('1990-05-15', '1985-10-22', '2015-01-01'), 'email': ('johndoe@gmail.com', 'bobJ@gmail.com', 'lev46@gmail.com')
# a=set()
#
# x = list(users_data[0].values())
# a.update(x)
# print(a)

#
#
# import time
# def time_it(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         work_time = time.time() -- start_time
#         m='test_func'
#         print('Execution time of \'{}\' : 1 seconds'.format(m))
#         'We are the {} who say "{}!"'.format('knights', 'Ni')
#         return res
#     return wrapper
# #
# # @timeit
# # Функция — пример
# # Она просто делает копию списка, добавляет value в конец списка и возвращает этот список
# def add_point(original_list: list, value):
#     # Специально делаем sleep, потому как без него время выполнения будет около нуля
#     time.sleep(2)
#     return original_list[:].append(value)
#
# # Делаем новую функцию уже с декоратором
# @time_it
# def add_point_with_timer(original_list: list, value):
#     add_point(original_list, value)
#
# # Выполняем функцию с декоратором
# add_point_with_timer([1, 2, 3, 4, 5], 6)

# Execution time of 'add_point_with_timer': 2.003331 seconds
# def log_filter (g,log_level="ERROR"):
#     g = g.split(('\n'))
#     x=[]
#
#     for i in range(len(g)):
#         c = g[i]
#         # print(c)
#         c = c.find(log_level)
#         # print(c)
#         if int(c) > -1:
#
#             x.append(g[i])
#     return x
#
#
#
# logs = """\
# 2023-08-15 14:15:24 INFO Starting the system.
# 2023-08-15 14:15:26 WARN System load is above 80%.
# 2023-08-15 14:15:27 ERROR Failed to connect to database.
# 2023-08-15 14:15:28 INFO Connection retry in 5 seconds.
# """
#
#
#
# logs = "2023-08-15 14:15:24 INFO Starting the system.\n2023-08-15 14:15:26 WARN System load is above 80%.\n2023-08-15 14:15:27 ERROR Failed to connect to database.\n2023-08-15 14:15:28 INFO Connection retry in 5 seconds.\n"
#
# to_test = list(log_filter(logs, log_level="ERROR"))
#
# print(to_test)

# 2023-08-15 14:15:27 ERROR Failed to connect to database.

#
# h='ERROR'
# g = logs.split(('.'))
# # c=g[2]
# # c = c.find('ERROR')
# # print(g[0].substring('ERROR'))
# # print(c)
# for i in range(len(g)):
#     c = g[i]
#     # print(c)
#     c = c.find(h)
#     # print(c)
#     if int(c) > -1:
#         x = g[i]
#         # print(x)
#
# print(x)
# for log in log_filter(logs, 'ERROR'):
   # print(log)

# 2023-08-15 14:15:27 ERROR Failed to connect to database.
#
# class Node:
#    def extract_categories(self, value, children=None):
#        self.value = value
#        self.children = children if children else []
#
# root = Node(5, [
#    Node(3, [
#        Node(1),
#        Node(4)
#    ]),
#    Node(2, [
#        Node(6),
#        Node(-1)
#    ])
# ])
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

# class Node:
#    def extract_categories(self, value, children=None):
#        self.value = value
#        self.children = children if children else []




#


# # root > Электроника
# # root > Электроника > Телефоны
# # root > Электроника > Телефоны > Смартфоны
# # root > Электроника > Телефоны > Проводные
# # root > Электроника > Компьютеры
# # root > Электроника > Компьютеры > Ноутбуки
# # root > Электроника > Компьютеры > Стационарные
# # root > Электроника > Компьютеры > Стационарные > Игровые
# # root > Электроника > Компьютеры > Стационарные > Для работы
# # root > Одежда
# # root > Одежда > Мужская
# # root > Одежда > Мужская > Джинсы
# # root > Одежда > Мужская > Куртки
#

def extract_categories(ggg):

    h=[]
    s=[]
    j=[]
    r=[]
    g=dict()
    f=dict()
    p=dict()
    v=dict()
    for key, value in ggg.items():
        h.append(key)
        g.update(value)

    for key, value in g.items():
        s.append(key)
        f.update(value)

    for key, value in f.items():
        j.append(key)
        p.update(value)

    for key, value in p.items():
        r.append(key)



    m=[h[0],h[0]+'>'+s[0], h[0]+'>'+s[0]+'>'+j[0] , h[0]+'>'+s[0]+'>'+j[1] , h[0]+'>'+s[1] , h[0]+'>'+s[1] +'>'+j[2] ,  h[0]+'>'+s[1]+'>'+j[3]  ,     h[0]+'>'+s[1]+'>'+j[3]+'>'+r[0]   ,   h[0]+'>'+s[1]+'>'+j[3]+'>'+r[1]         , h[1] , h[1]+'>'+s[2] , h[1]+'>'+s[2]+'>'+j[4] , h[1]+'>'+s[2]+'>'+j[5]]

    return m


categories = {"Электроника": {"Телефоны": {"Смартфоны": {},"Проводные": {} },
       "Компьютеры": { "Ноутбуки": {}, "Стационарные": {"Игровые": {}, "Для работы": {} } }  },
   "Одежда": { "Мужская": { "Джинсы": {}, "Куртки": {} } }}


paths = extract_categories(categories)
#
print(paths)

L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))
a=0
b=0
f=0
while f == 0:
    a = a-1
    b = b-1
    f = (id(a)-id(b))
else:
    print(f)
    print(a,b)


shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])
print(list_id_before)
print(list_id_after)

print(list_id_before == list_id_after)
h='ucjyhvikbi8jhfgdfgeyuhloi0-986ty6lk0n6ujcyhyrv'
print(list(set(list(h))))

# text = input("Введите текст:")
#
# unique = set(text)
#
# print("Количество уникальных символов: ", len(unique))

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = [2, 4, 6, 8, 10, 12]
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#
# a_and_b = a_set.symmetric_difference(b_set)
#
# print(a_and_b)
a = None # пустая строка
b = a or 1
some_var = b
if some_var is None:
    print("NoneType")
else:
    print(type(some_var))
print(b)


a = ''
b = ''

# print(1 and a or b)
#
#
# if  a and b: # проверка истинности обеих переменных
#     print("Обе переменные истинные")
# print(a,b)
#
# if a and b:
#     print("Обе переменные истинные")
#     print(a,b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print( b)
#
#
#
# if a and b:
#     print("Обе переменные истинные")
#     print(a,b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print( a or b ) # печать одной переменной, которая является истинной
# else:
#     print("Обе переменные ложные")
#
#
# a=66
#
# if type( a) == int and 100 < a<999 and a%2==0 and a%3==0:
#     print(True)
# else:
#     print(False)
#
#
# data = [0, 1, 2, 3]
# contains_positive = all(num > 0 for num in data)
# print(contains_positive)
#
#
# L = list(map(int, input().split()))
# print(not any(L))
# print(all([L]))
# print(L)
# print(all([4,8,890,6,7]))
#
# M = [[f'{i}*{j}={i*j}' for j in range(10)] for i in range(10)]
# print(M)
# #[[0, 1, 2, 3, 4],
# # [1, 2, 3, 4, 5],
# # [2, 3, 4, 5, 6],
# # [3, 4, 5, 6, 7],
# # [4, 5, 6, 7, 8]]
#
#
#
# L = [int(input())%2 == 0 for i in range(5)]
# print(L)
#
# L = [i for i in range(10)]
# # 0 1 2 3 4 5 6 7 8 9
# M = [i for i in range(10,0,-1)]
# # 10 9 8 7 6 5 4 3 2 1
# C = [a*b for a,b in zip(L,M)]
# print(C)
# b=1
# s=[]
# f ='aaabbccccdaa'
# L = list(f)
# print(L)
# for i in range(len(L)-1):
#     if L[i] == L[i+1]:
#         b = b+1
#         print(L[i],'1')
#     else:
#
#         print(L[i],'2')
#         s.append(L[i])
#         s.append(b)
#         b=1
# s.append(L[len(L)-1])
# s.append(b)
# print(s)
# text = input()  # получаем строку
#
# last = text[0]  # сохраняем первый символ
# count = 0  # заводим счетчик
# result = ''  # и результирующую строку
#
# for c in text:
#     if c == last:  # если символ совпадает с сохраненным,
#         count += 1  # то увеличиваем счетчик
#     else:
#         result += last + str(count)  # иначе - записываем в результат
#         last = c  # и обновляем сохраненный символ с его счетчиком
#         count = 1
#
# result += last + str(count)  # и добавляем в результат последний символ
# print(result)

# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
#
# print(fruits[0], fruits[1], fruits[2], fruits[3])
# # lemon pear watermelon tomato
# print(*fruits)
# # lemon pear watermelon tomato
# print(fruits)
#
# def linear_solve(a, b):
#     return b / a
# x =(linear_solve(2, 9))
# # 2*x = 9
# print(linear_solve(2, 9))
# print(linear_solve(0,1))


# def D(a, b, c):
#     return b**2 - 4*a*c  # дискриминант
#
# def quadratic_solve(a, b, c):
#     if D(a, b, c) < 0:
#         return print('нет вещественных доказательств')
#     elif D(a, b, c) ==0:
#         return -b/(2*a)
#     else:
#         return (-b - D(a, b, c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)
#
#
# def minimum(e):
#     if len(e)>1:
#
#         if int(e[0]) > int(e[1]):
#             e.pop(0)
#
#             return minimum(e)
#         else:
#             e.pop(1)
#             return minimum(e)
#     return e
#
# s =[6, 7, 9,2]
# print(minimum(s))
# # print(s[1])
#
# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
# s =[6, 7, 9,2]
# print(min_list(s))
#
#
# def reverse_number_recursion(num, reversed_num=0):
#     if num == 0:
#         return reversed_num
#     remainder = num % 10
#     reversed_num = (reversed_num * 10) + remainder
#     return reverse_number_recursion(num // 10, reversed_num)
# h = 4326556
# print(reverse_number_recursion(h))
#
#
# # def mirror(a, res=0):
# #     return mirror(a // 10, res*10 + a % 10) if a else res
#
# def mirror(a, res = 0 ):
#
#     return mirror(a // 10, res + a % 10) if a else res
# print( mirror(56765876))
#
# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N // 10, S - N % 10)
#
# print( equal(56765876, 60))
# def e():
#     n = 1
#
#     while True:
#         yield (1 + 1 / n) ** n
#         n += 1
#
# last = 0
# for a in e(): # e() - генератор
#     if (a - last) < 0.00000001: # ограничение на точность
#         print(a)
#         break # после достижения которого - завершаем цикл
#     else:
#         last = a # иначе - присваиваем новое значение
#
# iter_obj = iter("Hello!")
#
# print(next(iter_obj))
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#     return wrapper
#
# def has_access(func):
#     def wrapper():
#         if USERS.count(username):
#             print(f'Вы пршло авторизацию как: {username}')
#             func()
#         else:
#             print('не прошли идентификацию')
#     return wrapper
#
#
#
# @is_auth
# def from_db():
#     print("some data from database")
#
#
# from_db()
# @is_auth
# def change_profile():
#     print("Profile has been changed")
# change_profile()
#
#
# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# if auth:
#     username = input("Введите ваш username:")
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
# from_db()
L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(str.lower, L)))  # [1, 4, 9]

# for i in map(pow(2, 3), a_list):
#    pass

# Из заданного списка вывести только положительные элементы
def positive(x):
    return x > 0  # функция возвращает только True или False


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [1, 2]

def chet(h):
    return h%2 ==0 and h !=0

resul = filter(chet, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(resul))   # [1, 2]

result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [1, 2]

d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}

# Чтобы отсортировать его по ключам нужно сделать так
print(dict(sorted(d.items())))
# {1: 'd', 2: 'c', 3: 'b', 4: 'a'}

print(sorted(d.items(), key=lambda x: x[1]))  # сортировка по значению словаря

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]

print(sorted(data, key = lambda x: x[0] / x[1]**2))
print(min(data, key = lambda x: x[0] / x[1]**2))


a = ["asd", "bbd", "ddfa", "mcsa"]

print(list(map(len, a)))


