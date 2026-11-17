"""Тема 3. Операторы ветвления: if/elif/else, логические операторы, словарь вместо switch."""


def task_13(n):
    if n > 0:
        return 1 
    else:
        return 0
        
print(task_13(0))


def task_14(score):
    if score >= 90:
        return 'отлично'
    if score >= 75 and score <= 89:
        return 'хорошо'
    if score >= 60 and score <= 74:
        return 'удовлетворительно'
    if score < 60:
        return 'неудовлетворительно'
        
print(task_14(90))
print(task_14(89))
print(task_14(60))
print(task_14(59))


def task_15(age, is_citizen):
    if age >= 18 and is_citizen == True:
        return True
    else:
        return False
    
        
print(task_15(19, True))
print(task_15(19, False))
print(task_15(17, True))
print(task_15(18, True))


def task_16(password):
    if (len(password) >= 8 and
        any(i.isupper() for i in password) and
        any(j.isdigit() for j in password)):
        return True
    else:
        return False
        
print(task_16("Str0ngPass"))


def task_17(year):
    if year %4 == 0 and year %100 != 0 or year %400 == 0:
        return True
    else:
        return False
print(task_17(2000))


def task_18(op, a, b):

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 or x != 0 else None,
    }


    if op not in operations:
        return None


    result = operations[op](a, b)
    return result



print(task_18("+", 2, 3))
print(task_18("*", 4, 2.5))
print(task_18("/", 7, 2))
print(task_18("/", 5, 0))
print(task_18("^", 2, 3))