"""Тема 4. Генераторы и yield."""


def task_19(n):
    """Ленивые чётные числа.

    Напишите функцию-генератор, которая выдаёт первые n чётных чисел:
    2, 4, ..., 2n. Значения должны выдаваться лениво (по одному, через yield),
    а не возвращаться списком.

    Примеры:
        list(task_19(3)) == [2, 4, 6]
        g = task_19(2)
        next(g) == 2
        next(g) == 4
        # следующий next(g) возбуждает StopIteration
        list(task_19(0)) == []
    """

    for i in range(1, n + 1):
        yield i * 2

print(list(task_19(3)))


def task_20(n):
    """Обратный отсчёт.

    Напишите функцию-генератор обратного отсчёта: выдаёт числа от n до 0
    включительно, затем завершается.

    Примеры:
        list(task_20(3)) == [3, 2, 1, 0]
        list(task_20(0)) == [0]
    """
    for i in range(n, -1, -1):
        yield i
print(list(task_20(3)))

def task_21(n):
    """Квадраты через выражение-генератор.

    Верните выражение-генератор (НЕ список и НЕ функцию-генератор),
    выдающее квадраты чисел от 1 до n.

    Примеры:
        g = task_21(3)
        next(g) == 1
        next(g) == 4
        next(g) == 9
        # следующий next(g) возбуждает StopIteration
    """
    return (x**2 for x in range(1, n+1))
g = task_21(3)
print(next(g))  # 1
print(next(g))  # 4
print(next(g))  # 9

def task_22():
    """Бесконечный генератор Фибоначчи.

    Напишите генератор без параметров, выдающий числа Фибоначчи бесконечно:
    0, 1, 1, 2, 3, 5, ... Брать из него значения можно с помощью itertools.islice
    или next(). Два созданных генератора не должны влиять друг на друга.

    Примеры:
        from itertools import islice
        list(islice(task_22(), 8)) == [0, 1, 1, 2, 3, 5, 8, 13]
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

def task_23(items):
    """Уникальные элементы с сохранением порядка."""
    seen = set()
    for x in items:
        if x not in seen:
            seen.add(x)
            yield x

            
def task_24(nested):
    """Разглаживание вложенных списков."""
    for sublist in nested:
        yield from sublist
