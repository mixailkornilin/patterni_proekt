"""Тема 2. Переменные и область видимости: типы, mutable/immutable, константы, замыкания."""


def task_07(numbers):
    result = [max(numbers), min(numbers)]
    return result

print(task_07([1,2,4,5,3]))


def task_08(total):
    TAX_RATE = 0.2
    result = total * (1 + TAX_RATE)
    result = round(result,2)
    return result
print(task_08(250.5))


def task_09(items, item):
    new_list = items + [item]
    return new_list
print(task_09([], 'a'))


def task_10(values):
    result = [int(x) for x in values]
    return result
print(task_10(['007']))


def task_11(k):
    def inner(x):
        return k * x
    return inner
print(task_11(3)(4))



def task_12(box, key, value):
    box[key] = value
    return box

d = {"a": 1}
print(task_12(d, "b", 2) is d)
print(d)