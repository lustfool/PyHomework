# 41. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;


some_string = input('Введите арифметическое выражение: ')
list_of_operators = ['-', '+', '*', '/']


def split_into_arifm(some_string, list_of_operators):
    operator = []
    numbers = []
    temp = ''
    for char in some_string:
        if not char in list_of_operators:
            temp += char
        else:
            operator.append(char)
            numbers.append(int(temp))
            temp = ''
    numbers.append(int(temp))

    while len(numbers) > 1:

        if '*' in operator:
            index = operator.index('*')
            temp = parser(numbers[index], numbers[index + 1], '*')
            numbers[index] = temp
        elif '/' in operator:
            index = operator.index('/')
            temp = parser(numbers[index], numbers[index + 1], '/')
            numbers[index] = temp
        elif '+' in operator:
            index = operator.index('+')
            temp = parser(numbers[index], numbers[index + 1], '+')
            numbers[index] = temp
        elif '-' in operator:
            index = operator.index('-')
            temp = parser(numbers[index], numbers[index + 1], '-')
            numbers[index] = temp

        del (numbers[index + 1])
        del (operator[index])
    return numbers[0]


def parser(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return num1 / num2


print(some_string)
print(split_into_arifm(some_string, list_of_operators))

# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:*

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]



unic = []
for i in range(len(my_list)):
    if my_list[i] not in my_list[i + 1::] and my_list[i] not in my_list[:i - 1:]:
        unic.append(my_list[i])

print(unic)
