from itertools import count
from re import split

#
# def count_elements(input_list):
#    dict1 = {}
#    for i in input_list:
#        if i in dict1:
#            dict1[i] += 1
#        else:
#            dict1[i] = 1
#    print(dict1)
#
# list1 = [1, 2, 3, 2, 1, 1, 1, 2, 3, 3, 3, 3]
# list2 = [4, 5, 6, 4, 5, 5, 5, 6, 4, 4, 4, 6]
#
# count_elements(list1)
# count_elements(list2)
#
# # {1: 4, 2: 3, 3: 5}
# # {4: 5, 5: 4, 6: 3}
# input_password = input('Введите пароль: ')
#
#
# def is_valid_password(input_password, min_length=8, require_upper=True, require_lower=True, require_digit=True):
#     res = any(chrq.isdigit() for chrq in input_password)  #ложь цифра   min_length=6  abcdef
#     res1 = any(ch.islower() for ch in input_password)  #правда нижн регисто
#     res2 = any(chrw.isupper() for chrw in input_password)   #ложь верх регист
#     if len(input_password) >= min_length:
#         if res == require_digit or res2 == require_upper or res1 == require_lower:
#             result = True
#         else:
#             result = False
#     else:
#         result = False
#
#     return result
#
#
#
# print(is_valid_password('ABCDEF1', require_lower=False))
# # else:
#     print('Все верно')

# print(res1, '+', res2)

# a, b, c=15, 1, 10

# def is_success_code(code):
#
#
#     if code>=200 and code<=299:
#         res = True
#     else:
#         res = False
#     return res
#
#
#
# print(is_success_code(code = 300))

# содержит символ "@";
# содержит хотя бы одну точку после символа "@";
# не содержит пробелов.

# def is_valid_email(adres):
#     x1 = adres.count('@')
#     x3 = adres.count(' ')
#     g = adres.find('@')
#     x2 = adres.find('.',g)
#     if x1 >= 1 and x2>0 and x3 ==0:
#         res1 = True
#     else:
#         res1 = False
#     return res1
#
# print(is_valid_email("user@example.com"))
# print(is_valid_email("user at example dot com"))


# def  test_function(test1, test2, test3):
#
#     if test1 (test2)  == test3:
#         res3 = True
#     else:
#         res3 =False
#     return res3
#
#
#
#
# def square(n):
#    return n ** 2
#
# print(test_function(square, 4, 16))  # Передаем имя функции
# print(test_function(square, 5, 20))
#
#
#
#
#
#
#
# def show_card(name, age, sex): # <- это параметры
#    print("Name: {}\nAge: {}\nSex: {}".format(name, age, sex))
#
# show_card('Lev', 22, 'Male') # <- это аргументы






# test_range(15,1, 10)

# def count_elements(input_list):
#    if type(input_list) not in (list, tuple, str):
#        return "Недопустимый тип переданного аргумента"
#    print('Начало вычисления...')
#    dict1 = {}
#    for i in input_list:
#        if i in dict1:
#            dict1[i] += 1
#        else:
#            dict1[i] = 1
#    return dict1, dict1.keys()
#
# list1 = [1, 2, 3, 2, 1, 1, 1, 2, 3, 3, 3, 3]
#
# result = count_elements(list1)
# print(result)
# # Начало вычисления...
# # ({1: 4, 2: 3, 3: 5}, dict_keys([1, 2, 3]))
#
# result = count_elements(True)
# print(result)
# # Недопустимый тип переданного аргумента


#
# test_str = input_password
#
# print("The original string is : " + str(test_str))
#
# # using any() to check for any occurrence
# res = any(chr.isdigit() for chr in test_str)
#
# print("Does string contain any digit ? : " + str(res))

#
# def my_function():
#     print("Hello, world!")
#     return
# print("Goodbye, world!")
#
# my_function()
#
#
# def multiply(a, b):
#     return a * b
#
# print(multiply(3., 3))

# def generate_test_data(n=5, min_value=1, max_value=10):
#     import random
#     list1 = [random.randint(min_value,max_value) for i in range(n)]
#     return list1
#
# print(generate_test_data())
# print(generate_test_data(n=3, min_value=-5, max_value=5))
#
# def format_date(date, format="dmy"):
#
#     date_mix = date.split('-')
#     if format == 'dmy':
#         date_end = f'{date_mix[2]}{date_mix[1]}{date_mix[0]}'
#     if format == 'mdy':
#         date_end = f'{date_mix[1]}{date_mix[2]}{date_mix[0]}'
#     if format == 'ymd':
#         date_end = f"{date_mix[0]}{date_mix[1]}{date_mix[2]}"
#     if format != 'dmy' and format != 'mdy' and format != 'ymd':
#         date_end = date
#
#     return date_end
# print(format_date('2023-07-15', format = 'xyz'))
#
#
# def compare_lists(list1, list2, ignore_case=False):
#     f= []
#     if ignore_case == False:
#         for val in list1:
#         # Check if the current value is not in list 'b'
#             if val not in list2:
#             # If it's not in 'b', append it to list 'c'
#                 f.append(val)
#     else:
#         g = [x.lower() for x in list1]
#         d = [y.lower() for y in list2]
#
#         for val in g:
#         # Check if the current value is not in list 'b'
#             if val not in d:
#             # If it's not in 'b', append it to list 'c'
#                 f.append(val)
#
#
#     return f
# # print(compare_lists(["apple", "banana", "cherry"], ["Banana", "cherry", "date"]))
#     # # ["apple", "banana"]
# print(compare_lists(["apple", "banana", "cherry"], ["Banana", "cherry", "date"], ignore_case=True))
#     # # ["apple"]


# def calculate_average(*args):
#     d=1
#     f=0
#     for i in args:
#         d=d*i
#         f=f+1
#     x = d/f
#     return x
# print(calculate_average(1.2, 0.9, 1.3, 1.1, 1.7))
#
# def sort_data(**kwargs):
#     t = []
#     f = []
#     for key,value in kwargs.items():
#         t.append(key)
#         f.append(value)
#     g = list(zip(t,f))
#     x = sorted(g)
#     return x
#     # return ' '.join([f'{k}={kwargs[k]}' for k in sorted(kwargs)])
#
#
# print(sort_data(z = 1, y = 2, x = 3))
# # [('age', 30), ('city', 'New York'), ('name', 'Alex')]



test_reports = [
   {'name': 'test1', 'status': 'fail', 'time': 2.5, 'details': {'error': 'NullPointerException', 'attempt': 1}},
   {'name': 'test2', 'status': 'pass', 'time': 1.1, 'details': {'attempt': 1}},
   {'name': 'test3', 'status': 'fail', 'time': 3.1, 'details': {'error': 'AssertionError', 'attempt': 2}},
   {'name': 'test4', 'status': 'pass', 'time': 0.9, 'details': {'attempt': 1}}
]
def extract_data(reports, extraction_func):
   # Применяем переданную функцию к каждому словарю и генерируем новый список
   return [extraction_func(report) for report in reports]


print(extract_data(test_reports, lambda x: x['time']))

attempt_counts = extract_data(test_reports, lambda x: x['details']['attempt'])
print(attempt_counts)


strings = ["apple", "banana", "cherry", "date", "elderberry"]

def sort_strings_by_last_char(lists):
   sorted_list1 = sorted(lists, key=lambda x: x[-1])
   return sorted_list1

print(sort_strings_by_last_char(strings))
# ['banana', 'apple', 'date', 'elderberry', 'cherry']

def last_char(s):
   return s[-1]


words = ["banana", "apple", "cherry", "date"]
words.sort(key=last_char)
print(words)  # ['banana', 'apple', 'date', 'cherry']

def apply_function(lists,extraction_func):
   return [extraction_func(list) for list in lists]

numbers = [1, 2, 3, 4, 5]
print(apply_function(numbers, lambda x: x**2))
# [1, 4, 9, 16, 25]


#
# def sales_stats(price_list,revenue=False,quantity=False,customers=False):
#
#     if revenue is True:
#         d =[]
#         for i,v in enumerate(price_list):
#             d.append(i[1]*i[2])
#
#         c = sum(d)
#     if quantity is True:
#         c= {}
#         d = price_list[0][0]
#         z = price_list[1][0]
#         for i in price_list:
#             f = 0
#             k = 0
#             if d == price_list [i][0]:
#                 f = f+int(price_list[i][1])
#             if z == price_list [i][0]:
#                 k = k+int(price_list[i][1])
#
#
#
#
#     return c

#
#
#
#
# sales_data = [('Apple', 10, 0.5), ('Orange', 5, 0.6)]
#
#
#
#
# def sales_stats(sales_data, revenue = False, quantity = False, customers = False):
#         sum_doxoda = None
#         if revenue is True and len(sales_data) > 0: # общий доход
#                 list_1 = []
#                 for i,v in enumerate(sales_data):
#                         list_1.append(v[1] * v[2])
#                 sum_doxoda = sum(list_1)
#         # else:
#         #         sum_doxoda =0
#
#         kov_podan_dict = None
#         if quantity is True and len(sales_data) > 0: # количество проданных единиц каждого товара
#
#                 flat_list = [x for xs in sales_data for x in xs] # ['яблоки', 10, 20, 'груши', 5, 30, 'яблоки', 7, 20]
#
#                 spisok_1 = flat_list[0:3] # ['яблоки', 10, 20]
#                 spisok_1_1 = spisok_1[0] # 'яблоки'
#                 spisok_1_2 = spisok_1[1] # 10
#                 # spisok_1_3 = spisok_1[2] # 20
#                 # print(f'\nspisok_1 = {spisok_1}, type = {type(spisok_1)}'
#                 #          f'\nspisok_1_1 = {spisok_1_1}, type = {type(spisok_1_1)}'
#                 #          f'\nspisok_1_2 = {spisok_1_2}, type = {type(spisok_1_2)}'
#                 #          f'\nspisok_1_3 = {spisok_1_3}, type = {type(spisok_1_3)}\n')
#
#                 spisok_2 = flat_list[3:6]  # ['груши', 5,30]
#                 spisok_2_1 = spisok_2[0] # 'груши
#                 spisok_2_2 = spisok_2[1] # 5
#                 spisok_2_3 = spisok_2[2] # 30
#                 # print(f'\nspisok_2 = {spisok_2}, type = {type(spisok_2)}'
#                 #       f'\nspisok_2_1 = {spisok_2_1}, type = {type(spisok_2_1)}'
#                 #       f'\nspisok_2_2 = {spisok_2_2}, type = {type(spisok_2_2)}'
#                 #       f'\nspisok_2_3 = {spisok_2_3}, type = {type(spisok_2_3)}\n')
#
#                 # spisok_3 = flat_list[6:9] # ['яблоки', 7, 20]
#                 # spisok_3_1 = spisok_3[0] # 'яблоки'
#                 # spisok_3_2 = spisok_3[1] # 7
#                 # spisok_3_3 = spisok_3[2] # 20
#                 # print(f'\nspisok_3 = {spisok_3}, type = {type(spisok_3)}'
#                 #       f'\nspisok_3_1 = {spisok_3_1}, type = {type(spisok_3_1)}'
#                 #       f'\nspisok_3_2 = {spisok_3_2}, type = {type(spisok_3_2)}'
#                 #       f'\nspisok_3_3 = {spisok_3_3}, type = {type(spisok_3_3)}\n')
#
#                 kov_podan_dict = {}
#                 kov_podan_dict[spisok_1_1] = spisok_1_2
#                 kov_podan_dict[spisok_2_1] = spisok_2_2
#                 # kov_podan_dict[spisok_3_1] = spisok_3_2
#
#                 # print(f'kov_podan_dict = {kov_podan_dict}, type = {type(kov_podan_dict)}')
#
#                 if spisok_1_1 == spisok_2_1:
#                         kov_podan_dict[spisok_1_1] = (spisok_1_2 + spisok_2_2)
#                         #return kov_podan_dict
#
#                 # if spisok_1_1 == spisok_3_1:
#                 #         kov_podan_dict[spisok_1_1] = (spisok_1_2 + spisok_3_2)
#                 #         #return kov_podan_dict
#
#                 # if spisok_2_1 ==  spisok_3_1:
#                 #        kov_podan_dict[spisok_2_1] = (spisok_2_2 + spisok_3_2)
#                 #        #return kov_podan_dict
#         # else:
#         #         kov_podan_dict = []
#
#
#
#         if customers is True:
#                 I =  'сторонние ключевые аргументы'
#
#         if len(sales_data) == 0:
#             sum_doxoda = 0
#             kov_podan_dict ={}
#
#
#         ITOG =(f'({sum_doxoda}, {kov_podan_dict})')
#
#
#
#         return ITOG
#
# print(sales_stats(sales_data, revenue=True,quantity=True))
# # (490, None)
# print(sales_stats(sales_data, quantity=True))
# # # (None, {'яблоки': 17, 'груши': 5})
# print(sales_stats(sales_data, customers=True))
# # # (None, None)
#
# print(len(sales_data))
# #
# # sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
# # print(sales.items())
#
#





# Средний доход за данный период составил 230.0.
# Количество проданных единиц каждого товара:
# яблоки: 27
# груши: 5
#
# sales_data = [('Apple', 10, 0.5), ('Orange', 5, 0.6)]
# def sales_stats(sales1, revenue=False, quantity=False, customers=False):
#
#
#    sum_doxoda = 0
#    if revenue is True and len(sales1) > 0: # общий доход
#       sum_doxoda = 0
#       for i in sales1:
#          sum_doxoda = sum_doxoda +(float(i[1])*float(i[2]))
#       ITOG = sum_doxoda
#         # else:
#         #         sum_doxoda =0
#
#    kov_podan_dict = None
#    if quantity is True and len(sales1) > 0: # количество проданных единиц каждого товара
#
#                # flat_list = [x for xs in sales_data for x in xs] # ['яблоки', 10, 20, 'груши', 5, 30, 'яблоки', 7, 20]
#       sum_pos1 = 0
#       g = sales1[0][0]
#       for j in sales1:
#          if j[0] == g:
#             sum_pos1 = sum_pos1 + int(j[1])
#       sum_pos2 = 0
#       f = sales1[1][0]
#       for x in sales1:
#          if x[0] == f:
#             sum_pos2 = sum_pos2 + int(x[1])
#       kov_podan_dict = [sum_pos1,sum_pos2]
#       ITOG = kov_podan_dict
#
#
#         # else:
#         #         kov_podan_dict = []
#
#
#
#    if customers is True:
#       I =  'сторонние ключевые аргументы'
#
#       if len(sales1) == 0:
#          sum_doxoda = 0
#          kov_podan_dict ={}
#       ITOG = (sum_doxoda, kov_podan_dict)
#
#
#         # ITOG =(f'({sum_doxoda}, {kov_podan_dict})')
#    return ITOG
# #
# print(sales_stats(sales_data, revenue=True,quantity=True))
# # (490, None)
# print(sales_stats(sales_data, quantity=True))
# # # (None, {'яблоки': 17, 'груши': 5})
# print(sales_stats(sales_data, customers=True))
# # # (None, None)




# print(create_report(sales_data, sales_stats))
# print(len(sales_data))



# def create_report(sales, sales_stats):
#    # sumsr1 = sales_stats(sales, revenue=True)
#    sumsr =  sales_stats(sales, revenue=True)/ len(sales)
#    sum_post = sales_stats (sales,quantity=True)
#    t1 = f'Средний доход за данный период составил {sumsr}\n'
#    t2 = f'Количество проданных единиц каждого товара:\n'
#    t3 = f'{sales[0][0]}: {sum_post[0]}\n'
#    t4 = f'{sales[1][0]}: {sum_post[1]}'
#    text = t1+t2+t3+t4
#
#
#    return text
#
#
# print(create_report(sales_data, sales_stats))
#
# import warnings
#
# warnings.filterwarnings('ignore')

#
# def sales_stats(sales1, revenue=False, quantity=False, customers=False):
#    sum_doxoda = 0
#    if revenue is True and len(sales1) > 0:  # общий доход
#       sum_doxoda = 0
#       for i in sales1:
#          sum_doxoda = sum_doxoda + (int(i[1]) * int(i[2]))
#       ITOG = sum_doxoda
#       # else:
#       #         sum_doxoda =0
#
#    kov_podan_dict = None
#    if quantity is True and len(sales1) > 0:  # количество проданных единиц каждого товара
#
#       # flat_list = [x for xs in sales_data for x in xs] # ['яблоки', 10, 20, 'груши', 5, 30, 'яблоки', 7, 20]
#       sum_pos1 = 0
#       g = sales1[0][0]
#       for j in sales1:
#          if j[0] == g:
#             sum_pos1 = sum_pos1 + int(j[1])
#       sum_pos2 = 0
#       f = sales1[1][0]
#       for x in sales1:
#          if x[0] == f:
#             sum_pos2 = sum_pos2 + int(x[1])
#       kov_podan_dict = [sum_pos1, sum_pos2]
#       ITOG = kov_podan_dict
#
#       # else:
#       #         kov_podan_dict = []
#
#    if customers is True:
#       I = 'сторонние ключевые аргументы'
#
#       if len(sales1) == 0:
#          sum_doxoda = 0
#          kov_podan_dict = {}
#       ITOG = (sum_doxoda, kov_podan_dict)
#
#       # ITOG =(f'({sum_doxoda}, {kov_podan_dict})')
#    return ITOG
#
#
# def create_report(sales, dummy_func):
#    sumsr1 = dummy_func(sales, revenue=True)
#    sumsr = int(sumsr1[0]) / len(sales)
#    sum_post = dummy_func(sales, quantity=True)
#    t1 = f'Средний доход за данный период составил {sumsr}\n'
#    t2 = f'Количество проданных единиц каждого товара:\n'
#    t3 = f'яблоки: {sum_post[0]}\n'
#    t4 = f'груши: {sum_post[1]}'
#    text = t1 + t2 + t3 + t4
#
# def create_report(sales, dummy_func):
#    h = dummy_func(sales, revenue=True)
#    m = int(h[0])/len(sales)
#    g = dummy_func(sales, quantity=True)
#    k = tuple(g[1].keys())
#    l = tuple(g[1].values())
#
#
#    t1 = f'Средний доход за данный период составил {m}\n'
#    t2 = f'Количество проданных единиц каждого товара:\n'
#    t3 = f'{k[0]}: {l[0]}\n'
#    t4 = f'{k[1]}: {l[1]}'
#    text = t1 + t2 + t3 + t4
#
#    return text
#
#
# def dummy_func(data, **kwargs):
#    revenue = 100.0
#    quantity = {"Apple": 10, "Orange": 5}
#    return revenue, quantity
#
#
# print(create_report([('Apple', 10, 0.5)], dummy_func))

people = [
   {'name': 'Анна', 'age': 20},
   {'name': 'Борис', 'age': 25},
   {'name': 'Виктор', 'age': 19}
]
def get_age(person):
   return person['age']


sorted_people = sorted(people, key=get_age)
print(sorted_people)

sorted_people = sorted(people, key=lambda person: person['age'])
print(sorted_people)
# [{'name': 'Виктор', 'age': 19}, {'name': 'Анна', 'age': 20}, {'name': 'Борис', 'age': 25}]


user_activity = {"user1": 10, "user2": 5, "user3": 20, "user4": 15, "user5": 10}
def sort_users_by_activity(sales):
   sorted_people = {k: v for k, v in sorted(sales.items(), key=lambda item: item[1],  reverse=True)}
   d = list(sorted_people.keys())
   return d
print(sort_users_by_activity(user_activity))
# ['user3', 'user4', 'user1', 'user5', 'user2']
people = {"Вася": 25, "Петя": 30, "Маша": 20}
sorted_people = {k: v for k, v in sorted(people.items(), key=lambda item: item[1])}
print(sorted_people)



user_activity = {"user1": 10, "user2": 5, "user3": 20, "user4": 15, "user5": 10}
sorted_people = {k: v for k, v in sorted(user_activity.items(), key=lambda item: item[1])}
print(sorted_people)