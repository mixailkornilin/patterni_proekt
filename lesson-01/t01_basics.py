"""Тема 1. Основы Python: числа, строки, выражения, форматирование."""


def task_01(a, b, c):
    result = (a + b + c)/3
    return result

print(task_01(1, 2, 3))

def task_02(total_seconds):
    chas = int(total_seconds / 3600)
    minute = int((total_seconds - chas*3600)/ 60)
    second = int((total_seconds - chas*3600-minute*60)/1)
    result = (chas, minute, second)
    return result

print(task_02(59))



def task_03(fahrenheit):
    C = (fahrenheit - 32) * 5 / 9
    return C

print(task_03(212))


def task_04(price, discount_percent):
    result = price - (discount_percent * 0.01 * price)
    formatt_num = round(result,2)
    return (formatt_num)


print(task_04(199.99, 10))


def task_05(x, y):
    z = x + y
    result = (f"{x} + {y} = {z}")
    return result


print(task_05(2, 3))


def task_06(name):
    new_name = name.replace("  ",'')
    new_name = new_name.title()
    return new_name

print(task_06("  аННА   пЕТРОВА  "))

