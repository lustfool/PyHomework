# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = input('Введите число: ')
sum = 0
for i in n:
    if i != '.':
        sum = sum + int(i)
print(sum)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число: '))
some_list = [1]
for i in range(1, n):
    some_list.append((i + 1) * some_list[i - 1])
print(*some_list, sep=', ')

# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Введите число: '))
sum = 0
#some_list = []                     # если хочется задать список и вывести его
for i in range(1, n + 1):
#    some_list.append(((1 + (1 / i)) ** i))
    sum += ((1 + (1 / i)) ** i)
#print(*some_list, sep=', ')
print(round(sum, 2))

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.



# 5. Реализуйте алгоритм перемешивания списка.

import random

n = int(input('Введите число элементов списка: '))
some_list = []
for i in range(n):
    some_list.append(random.randint(0, 10))
print(some_list)
random.shuffle(some_list)
print(some_list)
