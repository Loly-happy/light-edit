# a=0.33
# s=18.42
# print(f'{a * s:.4f}')
# print(f"{5.724609312:.3f}")
# a=4
# c='Саутуарк'
# print(f"Сегодня утром {a} автомобиля и {a} омнибуса проехали по мосту {c}.")

# count = 4
# name = "Саутуарк"
# a = "Сегодня утром %d автомобиля и %d омнибуса проехали по мосту %s." % (count, count, name)
# b = "Сегодня утром {count} автомобиля и {count} омнибуса проехали по мосту {name}.".format(count=count, name=name)
# c = f"Сегодня утром {count} автомобиля и {count} омнибуса проехали по мосту {name}."
# print(a)
# print(b)
# print(c)
# import sys
# print("количество тракторов: ")
# num1 = sys.stdin.readline()
# print("количество мешков: ")
# num2 = sys.stdin.readline()
# r= "За прошедший месяц было проданj {h} мешков картошки и {f} тракторов".format(h=num1,f=num2)
# print("множитель: ")
# num3 = sys.stdin.readline()
#
# print(r*int(num3))
#
#
# g=[1,2,3,4,5, 'ytklkj']
# print(g[5]*6, end=" # ")
#
a=['3','2','5','1','4',]
print(sorted(a))
def el_cl(num):
    min = num%60
    h = (num//60)%24
    print(h,min)
el_cl(1441)



