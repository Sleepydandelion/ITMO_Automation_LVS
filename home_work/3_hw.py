# a = int(input())
# b = int(input())
# print (max (a,b))


def task1(a, b):
    if a > b:
        print(a)
    elif b > a:
        print(b)


task1(100, 555)
task1(397, 12)

def task2(c, d):
    if c == d+135 or d == c+135:
        print ('yes')
    else:
        print ('no')

task2(0, 135)
task2(555,0)


def task3(m):
    if m in range (1,3) or m == 12:
        print('Зима')
    elif m in range (3,6):
        print('Весна')
    elif m in range (6, 9):
         print('Лето')
    else:
         print('Осень')


task3(4)


def task4(a,b,c):
    if a>10 and b>10 and c>10:
        print ('yes')
    else:
        print('no')


task4(5,7,3)
task4(13,100,18)


def task5(g=(4, -2, 18, 23, -1000)):
    h = sum(1 for i in g if i >= 0)
    print("Количество положительных чисел:", h)


task5((13,-8,7,45,-100))


def task6(y: int = 1, m: int = 1):
    days = y * 348 + m * 29
    print("Количество дней = ", days)


task6(12,3)





