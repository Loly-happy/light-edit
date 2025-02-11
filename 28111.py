# rows = int(input('Введите количество строк массива: '))
# # считываем количество столбцов массива
# columns = int(input('Введите количество столбцов массива: '))
# # создаем пустой массив
# todo_list = []
# # цикл по строкам массива
# for i in range(rows):
#     # каждая строка массива состоит из columns элементов
#     todo_list.append([0]*columns)
# # выводим сгенерированный массив
#
# # for x in todo_list:
# #      print(x)
#
# day = ['понедельник', 'вторник' , 'среда' , 'четверг' , 'пятница' , 'суббота' , 'воскресенье' ]
# hourse = ['утро', 'день' , 'вечер']
# for i in range(rows):
#     print(f'Введите список дел на {day[i]}')
#     for j in range(columns):
#         print(f'Введите список дел на {hourse[j]}')
#
#         todo_list[i][j] = input()
#
# for x in todo_list:
#      print(x)
#
# n = input('Какой день нужно отредактировать, выберите с пн-вс: ')
# m = input('На ккакое время внести изменения утро, день вечре: ')
#
# del_d = day.index(n)
# del_h = hourse.index(m)
#
# task = input('Введите новое описание для дела: ')
# todo_list[del_d][del_h]= task
#
#
# for i in todo_list:
#      print(i)
#


todo_list = [# утро  день  вечер
        ['',    '',    ''], # понедельник
        ['',    '',    ''], # вторник
        ['',    '',    ''], # среда
        ['',    '',    ''], # четверг
        ['',    '',    ''], # пятница
        ['',    '',    ''], # суббота
        ['',    '',    ''], # воскресенье
       ]

days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
time = ['утро', 'день', 'вечер']

print('Заполняем ежедневник')
for i in range(7):
   for j in range(3):
      print(days[i], time[j])
      task = input('Введите дело: ')
      todo_list[i][j] = task

print()
print('Удаляем запись: ')
i = int(input('Введите индекс дня недели: '))
j = int(input('Введите индекс времени дня: '))
# удаляем запись
todo_list[i].pop(j)

print()
print('Добавляем запись: ')
i = int(input('Введите индекс дня недели: '))
task = input('Введите дело: ')
todo_list[i].append(task)

print()
print('Итоговый список дел: ')
for i in range(7):
   print(days[i])
   print(todo_list[i])
   print()


