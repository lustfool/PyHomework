# 1. Вычислить число c заданной точностью d
#
#     Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

a = float(input('Введите число: '))
d = input('Введите точность: ')
new_str = '{:.' + str(len(d) - 2) + 'f}'
print(new_str.format(a))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число: '))
some_list = []
for i in range(2, n + 1):
    if n % i == 0:
        count = 1
        for j in range(2, (i // 2 + 1)):
            if i % j == 0:
                count = 0
                break
        if count == 1:
            some_list.append(i)
print(some_list)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

new_list = [int(i) for i in input().split()]  # ввод последовательности чисел через пробел в строку
print(set(new_list))

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
#     Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень: '))
some_list = [random.randint(0, 101) for i in range(k + 1)]
new_str = ''
if len(some_list) < 1:
    new_str = 'x = 0'
else:
    for i in range(len(some_list)):
        if i != len(some_list) - 1 and some_list[i] != 0 and i != len(some_list) - 2:
            new_str += f'{some_list[i]}x^{len(some_list) - i - 1}'
            if some_list[i + 1] != 0:
                new_str += ' + '
        elif i == len(some_list) - 2 and some_list[i] != 0:
            new_str += f'{some_list[i]}x'
            if some_list[i + 1] != 0:
                new_str += ' + '
        elif i == len(some_list) - 1 and some_list[i] != 0:
            new_str += f'{some_list[i]} = 0'
        elif i == len(some_list) - 1 and some_list[i] == 0:
            new_str += ' = 0'
        elif some_list[i] == 0:
            new_str += ' + '
with open('file.txt', 'w') as data:
    data.write(new_str)

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Выбрал 4ю, мысли по 5й есть, но работоспособный код пока не удаётся.