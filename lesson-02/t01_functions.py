"""Тема 1. Функции: параметры, возврат значений, рекурсия, значения по умолчанию."""


def task_01(base, exponent=2):
    """Степень с показателем по умолчанию.

    Верните base, возведённое в степень exponent. Если exponent не передан,
    считайте его равным 2.

    Примеры:
        task_01(3) == 9
        task_01(2, 10) == 1024
        task_01(5, exponent=0) == 1
        task_01(-2, 3) == -8
    """
    try:
        return base ** exponent
    except ValueError:
        return base ** 2

print(task_01(3))

def task_02(numbers):
    """Минимум, максимум и среднее.

    Для непустого списка numbers верните кортеж (минимум, максимум, среднее).
    Среднее — float.

    Примеры:
        task_02([1, 2, 3, 4]) == (1, 4, 2.5)
        task_02([5]) == (5, 5, 5.0)
    """
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers)/len(numbers)
    return minimum, maximum, average
print(task_02([1,2,3,4]))


def task_03(n):
    """Сумма от 1 до n (рекурсия).

    Верните сумму целых чисел от 1 до n включительно (n >= 0).
    Обязательно используйте рекурсию — без циклов и формулы Гаусса.

    Примеры:
        task_03(5) == 15
        task_03(0) == 0
        task_03(10) == 55
    """
    if n == 1:
        return 1
    if n == 0:
        return 0
    return n + task_03(n - 1)

print(task_03(10))


def task_04(item, items=None):
    if items is None:
        result = []
    else:
        result = items.copy()

    result.append(item)
    return result
    """task_04("b") == ["b"]
        task_04("a") == ["a"]              # списки независимы, кэша нет
        task_04("b", ["a"]) == ["a", "b"]
        src = ["a"]; task_04("b", src); src == ["a"]  # вход не изменился
    """
print(task_04("b"))


def task_05(name, *, greeting="Привет", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"
try:
    task_05("А", "Б")
except TypeError:
    print("TypeError: позиционно передавать нельзя")


def task_06(func, value):
    """Применить функцию дважды.

    Функции — такие же объекты, как числа и строки: их можно передавать
    параметром. Верните результат применения func к value два раза подряд.

    Примеры:
        task_06(lambda x: x + 3, 10) == 16
        task_06(lambda s: s + "!", "привет") == "привет!!"
        task_06(str.strip, "  x  ") == "x"
    """
    return func(func(value))

print(task_06(lambda x: x + 3, 10))

