"""Тема 3. Замыкания и декораторы."""


def task_13(start=0):
    count = start

    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = task_13()
print(c(), c(), c())


def task_14(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@task_14
def double(x):
    return x * 2

print(double.calls)
print(double(2))
print(double.calls)
print(double(3))
print(double.calls)

def task_15(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if type(result) is str else result

@task_15
def greet(name):
    return f"привет, {name}"

print(greet("анна"))  # ПРИВЕТ, АННА


@task_15
def add(a, b):
    return a + b

print(add(1, 2))      # 3


def task_16(func):
    """Декоратор memoize.

    Декоратор кэширует результаты вызовов func по позиционным аргументам.
    Повторный вызов с теми же аргументами не должен вызывать исходную функцию.
    Для простоты считайте, что func вызывается только с позиционными аргументами.

    Примеры:
        calls = []
        def slow_square(x):
            calls.append(x)
            return x * x

        fast = task_16(slow_square)
        fast(2) == 4
        fast(2) == 4
        calls == [2]          # второй раз исходная функция не вызывалась
        fast(3) == 9
        calls == [2, 3]
    """

    def task_16(func):
        """Декоратор memoize."""
        cache = {}

        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]

        return wrapper
#
#
def task_17(func):
    """Декоратор require_positive."""

    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Аргументы должны быть неотрицательными")

        for arg in kwargs.values():
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Аргументы должны быть неотрицательными")

        return func(*args, **kwargs)

    return wrapper


def task_18(times):
    """Фабрика декораторов repeat."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator
