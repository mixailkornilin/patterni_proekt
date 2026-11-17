"""Тема 4. Коллекции: списки, кортежи, множества, словари, строки, 2D-структуры."""

def task_19(numbers):

    return sorted(numbers, reverse = True)
    
print(task_19([1,2,3]))


def task_20(items):
    result = items[1: -1]
    if len(result) < 3:
        return "()"
    else:
        return result

print(task_20((1,2,3,4)))


def task_21(a, b):

    return {
        "union": sorted(a | b),
        "intersection": sorted(a & b),
        "a_minus_b": sorted(a - b)
    }

print(task_21({1, 2, 3}, {3, 4}))

def task_22(text):
    """Частотный словарь слов.

    Разбейте строку text на слова (разделители — пробельные символы)
    и верните словарь {слово: количество вхождений}.

    Примеры:
        task_22("кот кот пёс") == {"кот": 2, "пёс": 1}
        task_22("раз два три раз два раз") == {"раз": 3, "два": 2, "три": 1}
        task_22("") == {}
    """
    words = text.split()
    frq = {}
    for word in words:
        frq[word] = frq.get(word, 0) + 1
    return frq

print(task_22("раз два три раз два раз"))


def task_23(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())

    return cleaned == cleaned[::-1]


print(task_23("А роза упала на лапу Азора"))


def task_24(matrix):

    total = 0
    n = len(matrix)
    for i in range(n):
        total += matrix[i][i]
    return total

print(task_24([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
