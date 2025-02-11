# correct_password = '12345'
# password = input('Введите пароль: ')
# # если пароль верный
# if password == correct_password:
#     print('Авторизация прошла успешно')
# # если пароль неверный
# else:
#     print('Введен неверный пароль')

    # считываем число
# number = int(input ('Введите число: '))

# # если число больше нуля
# if number > 0:
#     print('Число положительное')
#     # в противном случае, если число меньше нуля
# elif number < 0:
#     print('Число отрицательное')
#     # в противном случае
# else:
#     print('Число равно 0')

# people = ['Ваня', 'Саша','миша']
# new_person = people.append('Толя')
# print(people)


# people = [['Ваня',17], ['Саша',12],['миша',15]]
# for person in people:
#     for item in person:
#         print(item)
# print(people)

# people = {1:'Ваня', 2:'Саша',3:'миша'}
# for key, value in people.items():
#     print(key, value)
#
# print(people)

# number = 8
# if number%2 == 0:
#     print("число четно")
# else:
#     print('число нечетное')
#
# number = int(input('Введите число'))
# if number % 2 != 0:
#     print("число нечетное")
# else:
#     print('число четное')

correct_password = '12345'
correct_login = 'user777'

# # считываем логи и пароль
# login = input('Введите логин: ')
# password = input('Введите пароль: ')
#
# # если логин и пароль верный
# if login == correct_login and password == correct_password:
#     print('Авторизация прошла успешно')
# # если логин или пароль неверный
# else:
#     print('Введен неверный логин или пароль')

# # считываем число
# number = int(input('Введите число больше или равное нулю: '))
# # если число больше нуля или число равно нулю
# if number > 0 or number == 0:
#     print('Число больше или равно нуля')
# # в противном случае число отрицательное
# else:
#     print('Число отрицательное')



# # считываем число
# number = int(input('Введите число больше или равное нулю: '))
# # если не неотрицательно
# if not number < 0:
#     print('Число больше или равно нуля')
# # в противном случае число отрицательное
# else:
#     print('Число отрицательное')
# number = int(input('Введите число'))
# if number%2 == 0 and not number==0:
#     if number < 0:
#         print('число отрицательно, четное')
#     else:
#         print('число положительное, четное')
# elif number%2 > 0 and not number==0:
#     if number > 0:
#         print('число положительное, нечетное')
#     else:
#         print('число отрицательное, нечетное')
# else:
#     print('число равно нулю')

# number = int(input('Введите число'))
# for i in range(1,11, 1):
#     print(f'{number} * {i} = {number * i}')

# print(list(range(5)))
# print(list(range(1,10,2)))
# print(list(range(10,0,-3)))
# print(list(range(0,10,1)))


# for i in range(1,11, 1):
#     print()
#     for j in range(1,11, 1):
#         print(f'{j} * {i} = {j * i}')

# number = int(input('Введите число'))
# n =1
# sum = 0
# # пока n меньше 6
# while n < number+1:
#     sum = sum+n
#
#     n += 1
# print(sum)
# n = 1
# # бесконечный цикл
# while True:
#     # выводим n
#     print(n)
#     # увеличиваем n на 1
#     n += 1
#     if n >=6 :
#         # прерываем работу программы
#         break

# n = 0
# # пока n меньше 10
# while n < 10:
#     # увеличиваем n на 1
#     n += 1
#     # если число не четное
#     if n % 2 != 0:
#         # пропускаем итерацию
#         continue
#     # а если четное
#     # выводим n
#     print(n)
#
# for i in range(1, 6):
#     if i % 2 == 0:
#         print(f'{i} - четное')
#     else:
#         print(f'{i} - нечетное')

m = 1
for i in range(1, 11):
    if i % 2 == 0:
        continue
    m = i*m
print(m)


# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# if a < b:
#     for i in range(a, b+1):
#         print(i)
# else:
#     for i in range(a, b-1, -1):
#         print(i)



squared = map(lambda x: x**2, [1, 2, 3, 4])
squared1 = filter(lambda x: x**2, [1, 2, 3, 4])
print(list(squared))
# [1, 4, 9, 16]
print(list(squared1))


numbers_int = map(int, ['1', '2', '3', '4'])

print(list(numbers_int))
# [1, 2, 3, 4]

numbers_int = map(int, ['1', '2', '3', '4'])


for n in numbers_int:
   print(n, type(n))
# 1 <class 'int'>
# 2 <class 'int'>
# 3 <class 'int'>
# 4 <class 'int'>

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

even_numbers1 = map(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
# [2, 4, 6]
print(list(even_numbers1))

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]


paired = zip(names, scores)


print(list(paired))
# [('Alice', 85), ('Bob', 90), ('Charlie', 88)]

expected = [200, 404, 500]
actual = [200, 404, 500.05]


for e, a in zip(expected, actual):
   if e != a:
       print(f"Expected {e}, but got {a}")
# Expected 500, but got 500.05

headers = ["name", "age", "gender"]
row = ["Alice", 28, "Female"]


user_data = dict(zip(headers, row))
print(user_data)
# {'name': 'Alice', 'age': 28, 'gender': 'Female'}

keys = ["name", "age"]
values = ["Alice", 30]
data = {key: value for key in keys for value in values}
print(data)

values = [False, False, True, False]
result = any(values)
print(result)
# True

values = [False, False, True, True]
result = all(values)
print(result)
# False

data = [0, 1, -1, 3]
contains_positive = False
for num in data:
   if num > 0:
       contains_positive = True
       break
print(contains_positive)
data = [0, 1, 2, 3]
contains_positive = any(num > 0 for num in data)
print(contains_positive)


prices_in_usd = [10, 20, 30, 40, 50]
exchange_rate = 0.85

prices_in_euro = list(map(lambda x: x*exchange_rate, prices_in_usd))
print(list(prices_in_euro))

phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']

def format_phone_number(number):
    b = []
    for i in phone_numbers:
        even_numbers1 = list(filter(lambda x: x.replace('-', ''), i))
        o = ''.join(even_numbers1)
        b.append(o)
    c = []
    for i in b:
        even_numbers2 = list(filter(lambda x: x.replace('.', ''), i))
        o = ''.join(even_numbers2)
        c.append(o)
    n = []
    for i in c:
        even_numbers3 = list(filter(lambda x: x.replace(')', ''), i))
        o = ''.join(even_numbers2)
        n.append(o)
    s = []
    for i in n:
        even_numbers4 = list(filter(lambda x: x.replace('(', ''), i))
        o = ''.join(even_numbers2)
        s.append(o)
    y = []
    for i in s:
        even_numbers5 = list(filter(lambda x: x.replace(' ', ''), i))
        o = ''.join(even_numbers1)
        y.append(o)
    r = []
    for i in y:
        even_numbers6 = list(filter(lambda x: x.replace('+', ''), i))
        o = ''.join(even_numbers1)
        r.append(o)
    x= r[0]

    return x
print(format_phone_number(phone_numbers))

formatted_numbers =  list(map(format_phone_number,phone_numbers))
print(formatted_numbers)
b=[]
for i in phone_numbers:
    even_numbers1 = list(filter(lambda x: x.replace('-', ''), i))
    o = ''.join(even_numbers1)
    b.append(o)
c=[]
for i in b:
    even_numbers2 = list(filter(lambda x: x.replace('.', ''), i))
    o = ''.join(even_numbers2)
    c.append(o)
n=[]
for i in c:
    even_numbers3 = list(filter(lambda x: x.replace(')', ''), i))
    o = ''.join(even_numbers2)
    n.append(o)
s=[]
for i in n:
    even_numbers4 = list(filter(lambda x: x.replace('(', ''), i))
    o = ''.join(even_numbers2)
    s.append(o)
y =[]
for i in s:
    even_numbers5 = list(filter(lambda x: x.replace(' ', ''), i))
    o = ''.join(even_numbers1)
    y.append(o)
r=[]
for i in y:
    even_numbers6 = list(filter(lambda x: x.replace('+', ''), i))
    o = ''.join(even_numbers1)
    r.append(o)
print(r)



h = list(map(lambda x:''.join(x), even_numbers ))
x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print(''.join(x))
print(h)