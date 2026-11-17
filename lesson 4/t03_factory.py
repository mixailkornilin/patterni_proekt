"""Тема 3. Фабричные функции и Factory Method."""

import math

class Car:
    """Продукт: автомобиль."""

    name = "автомобиль"

class Truck:
    name = "грузовик"

class Bike:
    name = "мотоцикл"

class Ship:
    name = "судно"

class Circle:
    """Продукт: круг радиуса r."""

    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

class Rect:
    """Продукт: прямоугольник."""

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

def task_13(kind):
    """Функция-фабрика.

    Верните объект по строке kind: "car" → Car, "truck" → Truck,
    "bike" → Bike. Для неизвестного kind — ValueError("неизвестный транспорт").

    Примеры:
        task_13("car").name == "автомобиль"
        isinstance(task_13("bike"), Bike)
        task_13("train")  # ValueError: неизвестный транспорт
    """
    registry = {
        "car": Car,
        "truck": Truck,
        "bike": Bike,
    }
    if kind not in registry:
        raise ValueError("неизвестный транспорт")
    return registry[kind]()

print(task_13("car").name == "автомобиль")   
print(isinstance(task_13("bike"), Bike))     

try:
    task_13("train")
except ValueError as e:
    print(f"ValueError: {e}")

class TransportFactory:
    """Задание 14. Фабричный метод класса.

    Классовый метод create(kind) делает то же, что task_13: возвращает
    Car/Truck/Bike по строке, при неизвестном kind — ValueError.

    Примеры:
        TransportFactory.create("truck").name == "грузовик"
        isinstance(TransportFactory.create("car"), Car)
        TransportFactory().create("bike").name == "мотоцикл"   # и через экземпляр
    """

    @classmethod
    def create(cls, kind):
        registry = {
            "car": Car,
            "truck": Truck,
            "bike": Bike,
        }
        if kind not in registry:
            raise ValueError("неизвестный транспорт")
        return registry[kind]()

print("\n")

print(TransportFactory.create("truck").name == "грузовик")          
print(isinstance(TransportFactory.create("car"), Car))              
print(TransportFactory().create("bike").name == "мотоцикл")

class Logistics:
    """Задание 15. Канонический Factory Method.

    Базовый класс доставки: метод deliver() ВОЗВРАЩАЕТ строку
    "{имя транспорта} доставляет груз", беря транспорт у фабричного метода
    create_transport(). Сам create_transport() в базовом классе — «хук»:
    возбуждает NotImplementedError("выберите тип логистики").

    Подклассы RoadLogistics и SeaLogistics переопределяют ТОЛЬКО
    create_transport(): Road → Car, Sea → Ship.

    Примеры:
        RoadLogistics().deliver() == "автомобиль доставляет груз"
        SeaLogistics().deliver() == "судно доставляет груз"
        Logistics().create_transport()  # NotImplementedError: выберите тип логистики
    """

    def create_transport(self):
        raise NotImplementedError("выберите тип логистики")

    def deliver(self):
        transport = self.create_transport()
        return f"{transport.name} доставляет груз"

class RoadLogistics(Logistics):
    def create_transport(self):
        return Car()

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()

print("\n")

print(RoadLogistics().deliver() == "автомобиль доставляет груз")   
print(SeaLogistics().deliver() == "судно доставляет груз")         

try:
    Logistics().create_transport()
except NotImplementedError as e:
    print(f"NotImplementedError: {e}")

class ShapeFactory:
    """Задание 16. Реестр классов-продуктов.

    Фабрика с регистрацией: register(name, cls) запоминает класс продукта;
    create(name, **kwargs) создаёт экземпляр зарегистрированного класса
    с переданными аргументами. Неизвестное имя — ValueError("неизвестный продукт").

    Примеры:
        f = ShapeFactory()
        f.register("circle", Circle)
        c = f.create("circle", r=2)
        isinstance(c, Circle)
        c.area() == 4 * math.pi
        f.create("hexagon")  # ValueError: неизвестный продукт
    """
    def __init__(self):
        self._registry = {}

    def register(self, name, cls):
        self._registry[name] = cls

    def create(self, name, **kwargs):
        if name not in self._registry:
            raise ValueError("неизвестный продукт")
        return self._registry[name](**kwargs)

print("\n")

f = ShapeFactory()
f.register("circle", Circle)

c = f.create("circle", r=2)
print(isinstance(c, Circle))          
print(c.area() == 4 * math.pi)        

try:
    f.create("hexagon")
except ValueError as e:
    print(f"ValueError: {e}")

def task_17(rule):
    """Фабрика функций.

    Верните функцию одного аргумента value:
      "positive" → value > 0
      "even"     → value % 2 == 0
      "nonempty" → bool(value)
    Неизвестное правило — ValueError("неизвестное правило").

    Примеры:
        task_17("positive")(5) == True
        task_17("positive")(-1) == False
        task_17("even")(4) == True
        task_17("nonempty")("") == False
        task_17("odd")  # ValueError: неизвестное правило
    """
    rules = {
        "positive": lambda value: value > 0,
        "even": lambda value: value % 2 == 0,
        "nonempty": lambda value: bool(value),
    }
    if rule not in rules:
        raise ValueError("неизвестное правило")
    return rules[rule]

print("\n")

print(task_17("positive")(5) == True)       
print(task_17("positive")(-1) == False)     
print(task_17("even")(4) == True)           
print(task_17("nonempty")("") == False)     

try:
    task_17("odd")
except ValueError as e:
    print(f"ValueError: {e}")

def task_18(shape, **params):
    """Параметризованная фабрика.

    Создайте фигуру по имени и параметрам:
      "circle" → Circle(r=...)
      "rect"   → Rect(w=..., h=...)
      "square" → Rect(w=s, h=s) по одному параметру side
    Неизвестное имя — ValueError("неизвестная фигура").

    Примеры:
        task_18("circle", r=2).area() == 4 * math.pi
        task_18("rect", w=3, h=4).area() == 12
        task_18("square", side=5).area() == 25
    """
    if shape == "circle":
        return Circle(r=params["r"])
    if shape == "rect":
        return Rect(w=params["w"], h=params["h"])
    if shape == "square":
        s = params["side"]
        return Rect(w=s, h=s)
    raise ValueError("неизвестная фигура")

print("\n")

print(task_18("circle", r=2).area() == 4 * math.pi)   
print(task_18("rect", w=3, h=4).area() == 12)         
print(task_18("square", side=5).area() == 25)         
