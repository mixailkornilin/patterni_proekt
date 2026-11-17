"""Тема 5. Абстрактные классы и интерфейсы (модуль abc)."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Задание 31. Базовый абстрактный класс.

    Shape — абстрактный класс с абстрактным методом area().
    Реализуйте подклассы Circle(r) и Rectangle(w, h), вычисляющие площадь.
    Экземпляр Shape создать нельзя.

    Примеры:
        Shape()   # TypeError: абстрактный класс
        Circle(2).area() == 4 * math.pi
        Rectangle(3, 4).area() == 12
    """

    @abstractmethod
    def area(self):
        raise NotImplementedError("Реализуйте Shape.area")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Animal(ABC):
    """Задание 32. Конкретный метод на абстрактной базе (шаблонный метод).

    Абстрактный метод speak(); конкретный метод introduce() возвращает
    "Я говорю: {speak()}" — он готов к работе, как только подкласс
    реализует speak(). Подкласс Cat: speak() → "мяу".

    Примеры:
        Cat("Мурка").introduce() == "Я говорю: мяу"
        Animal("X")   # TypeError: speak не реализован
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        raise NotImplementedError("Реализуйте Animal.speak")

    def introduce(self):
        return f"Я говорю: {self.speak()}"


class Cat(Animal):
    def speak(self):
        return "мяу"


class Vehicle(ABC):
    """Задание 33. Абстрактное свойство.

    Vehicle объявляет абстрактное СВОЙСТВО max_speed (через
    @property + @abstractmethod). Подкласс Car реализует его константой 220.

    Примеры:
        Vehicle()   # TypeError
        Car("Лада").max_speed == 220
    """

    @property
    @abstractmethod
    def max_speed(self):
        raise NotImplementedError("Реализуйте Vehicle.max_speed")


class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    @property
    def max_speed(self):
        return 220


class Plugin(ABC):
    """Задание 34. Реестр подклассов.

    Абстрактный run(). Классовый метод subclasses() возвращает отсортированный
    список имён ПРЯМЫХ подклассов того класса, у которого вызван
    (cls.__subclasses__()).

    Примеры:
        class Echo(Plugin):
            def run(self): return "echo"

        "Echo" in Plugin.subclasses()
        Echo().run() == "echo"
    """

    @abstractmethod
    def run(self):
        raise NotImplementedError("Реализуйте Plugin.run")

    @classmethod
    def subclasses(cls):
        return sorted(sub.__name__ for sub in cls.__subclasses__())


class Serializable(ABC):
    """Задание 35, часть 1. Интерфейс сериализации."""

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError("Реализуйте Serializable.to_dict")


def task_35(items):
    """Задание 35, часть 2. Работа через интерфейс, а не через тип.

    Верните список словарей для всех items, вызывая to_dict(). Функция
    принимает любые объекты, реализующие интерфейс Serializable, —
    без isinstance-проверок.

    Примеры:
        class Book(Serializable):
            def __init__(self, title):
                self.title = title
            def to_dict(self):
                return {"title": self.title}

        task_35([Book("а"), Book("б")]) == [{"title": "а"}, {"title": "б"}]
        task_35([]) == []
    """
    return [item.to_dict() for item in items]


class Item:
    """Задание 36, часть 1. Предмет: имя и стоимость (из упражнения 3 книги)."""

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Box(ABC):
    """Задание 36, часть 2. Абстрактная коробка (по упражнению 3 книги).

    Абстрактные методы:
      add(item)  — положить предмет;
      empty()    — забрать ВСЕ предметы и вернуть их списком;
      count()    — сколько предметов сейчас в коробке.

    Реализуйте два подкласса с разным внутренним хранением:
      ListBox  — хранит предметы в списке;
      DictBox  — хранит в словаре.
    """

    @abstractmethod
    def add(self, item):
        raise NotImplementedError("Реализуйте Box.add")

    @abstractmethod
    def empty(self):
        raise NotImplementedError("Реализуйте Box.empty")

    @abstractmethod
    def count(self):
        raise NotImplementedError("Реализуйте Box.count")


class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)


class DictBox(Box):
    def __init__(self):
        self._items = {}
        self._counter = 0

    def add(self, item):
        self._items[self._counter] = item
        self._counter += 1

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)


def task_36(*boxes):
    """Задание 36, часть 3. Переупаковка коробок (по книге).

    Соберите все предметы из всех коробок и распределите их между коробками
    как можно равнее (первые коробки могут получить на один предмет больше).
    Порядок предметов не важен. Функция работает с ЛЮБЫМИ подклассами Box.

    Примеры:
        b1, b2, b3 = ListBox(), ListBox(), DictBox()
        # ... 20, 9 и 5 предметов ...
        task_36(b1, b2, b3)
        sorted(b.count() for b in (b1, b2, b3)) == [11, 11, 12]
    """
    if not boxes:
        return

    # 1. Собираем все предметы из всех коробок
    all_items = []
    for box in boxes:
        all_items.extend(box.empty())

    # 2. Распределяем как можно равнее
    num_boxes = len(boxes)
    total_items = len(all_items)

    # Базовое количество предметов на коробку и остаток
    base_count = total_items // num_boxes
    remainder = total_items % num_boxes

    start = 0
    for i, box in enumerate(boxes):
        # Первые `remainder` коробок получают на 1 предмет больше
        current_count = base_count + (1 if i < remainder else 0)
        for item in all_items[start:start + current_count]:
            box.add(item)
        start += current_count

# 31. Shape
try:
    Shape()
    assert False, "Shape() должна была вызвать TypeError"
except TypeError:
    pass
assert abs(Circle(2).area() - 4 * math.pi) < 1e-9
assert Rectangle(3, 4).area() == 12


# 32. Animal
assert Cat("Мурка").introduce() == "Я говорю: мяу"
try:
    Animal("X")
    assert False
except TypeError:
    pass


# 33. Vehicle
try:
    Vehicle()
    assert False
except TypeError:
    pass
assert Car("Лада").max_speed == 220


# 34. Plugin
class Echo(Plugin):
    def run(self): return "echo"
assert "Echo" in Plugin.subclasses()
assert Echo().run() == "echo"


# 35. Serializable
class Book(Serializable):
    def __init__(self, title):
        self.title = title
    def to_dict(self):
        return {"title": self.title}
assert task_35([Book("а"), Book("б")]) == [{"title": "а"}, {"title": "б"}]
assert task_35([]) == []


# 36. Box и task_36
b1, b2, b3 = ListBox(), ListBox(), DictBox()
for i in range(20): b1.add(Item(f"i{i}", i))
for i in range(9): b2.add(Item(f"j{i}", i))
for i in range(5): b3.add(Item(f"k{i}", i))

task_36(b1, b2, b3)
assert sorted(b.count() for b in (b1, b2, b3)) == [11, 11, 12]
