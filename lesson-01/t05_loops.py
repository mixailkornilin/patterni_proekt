"""Тема 5. Операторы управления циклом: while, for, break/continue, генераторы списков."""


def task_25(n):
    if n == 0:
        return 0
    if n <0:
        n = -n


    result = []
    while n > 0:
        dight = n %10
        n //= 10
        result.append(dight)
    result = result[::-1]

    sum = 0
    for i in result:
        sum += i

    return sum

print(task_25(12345))

def task_26(n):
    """Факториал.

    Верните n! для целого n >= 0. Реализуйте через цикл for.

    Примеры:
        task_26(0) == 1
        task_26(1) == 1
        task_26(5) == 120
        task_26(10) == 3628800
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(task_26(5))

def task_27(n):
    """Таблица умножения.

    Верните таблицу умножения размером n×n в виде списка списков:
    элемент на позиции (i, j) равен (i+1)*(j+1). Используйте вложенные циклы.

    Примеры:
        task_27(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
        task_27(1) == [[1]]
    """
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

print(task_27(3))



def task_28(names, days):
    def task_28(names, days):
        result = {}
    for name, day in zip(names, days):
        result[name] = day
    return result

print(task_28(["январь", "февраль"], [31, 28]))



def task_29(numbers):
    """Квадраты чётных чисел.

    Верните список квадратов только чётных чисел из numbers.
    Используйте генератор списка (list comprehension).

    Примеры:
        task_29([1, 2, 3, 4]) == [4, 16]
        task_29([1, 3]) == []
        task_29([]) == []
    """
    result = [x**2 for x in numbers if x % 2 == 0 ]
    return result
print(task_29([1, 2, 3, 4]))



def task_30(numbers, stop_value):
    """Сумма до sentinel-значения.

    Пройдите по numbers и просуммируйте элементы, пока не встретится элемент,
    равный stop_value (само это значение не суммируется — прервите цикл break).
    Если stop_value не встретился, верните сумму всех элементов.

    Примеры:
        task_30([5, 7, -1, 9], -1) == 12
        task_30([1, 2], 99) == 3
        task_30([0, 1, 2], 0) == 0
    """
    result = 0
    for i in numbers:
        if i == stop_value:
            break
        else:
            result += i
    return result
print(task_30([5, 7, -1, 9], -1))