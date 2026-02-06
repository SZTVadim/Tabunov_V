# Домашнее задание: ООП - Инкапсуляция, Полиморфизм, Наследование, Абстракция
# ЗАДАНИЕ: Система управления животными в зоопарке
# Создайте простую систему управления животными, используя все принципы ООП.
# ЧАСТЬ 1: Абстракция - Абстрактный класс Animal
# 1) Создайте абстрактный класс Animal:
#    - Используйте from abc import ABC, abstractmethod
#    - Создайте абстрактный метод make_sound() с декоратором @abstractmethod

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# ЧАСТЬ 2: Наследование - Классы Dog и Cat
# 2) Создайте класс Dog (Собака), который наследуется от Animal:
#    - В __init__ принимайте: name (имя), age (возраст)
#    - Реализуйте метод make_sound() — выводит "{name} говорит: Гав-гав!"

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")

# 3) Создайте класс Cat (Кошка), который наследуется от Animal:
#    - В __init__ принимайте: name (имя), age (возраст)
#    - Реализуйте метод make_sound() — выводит "{name} говорит: Мяу!"

class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")

# ЧАСТЬ 3: Инкапсуляция - Класс Zoo (Зоопарк)
# 4) Создайте класс Zoo:
#    - В __init__ принимайте: name (название зоопарка)
#    - Создайте приватный атрибут __animals (список животных), инициализируйте пустым списком
#    - Создайте метод add_animal(animal) — добавляет животное в __animals
#    - Создайте метод get_animals_count() — возвращает количество животных (геттер для доступа к приватному атрибуту)

class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal):
            self.__animals.append(animal)

    def get_animals_count(self):
            return len(self.__animals)

    def get_animals(self):
        return self.__animals

# ЧАСТЬ 4: Полиморфизм - Работа с разными животными
# 5) Создайте функцию animal_sound(animal):
#    - Принимает объект Animal (может быть Dog или Cat)
#    - Вызывает метод make_sound() у объекта
#    - Объясните в комментарии, почему это пример полиморфизма

def animal_sound(animal):
    animal.make_sound()

# Это полиморфизм потому-что мы вызываем одну и ту же функцию у кошки и собаки

# 6) Создайте объекты:
#    - dog1 = Dog("Бобик", 3)
#    - dog2 = Dog("Шарик", 5)
#    - cat1 = Cat("Мурка", 2)

dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)

# 7) Создайте объект зоопарка: zoo = Zoo("Городской зоопарк")

zoo = Zoo("Городской зоопарк")

# 8) Добавьте всех животных в зоопарк через метод add_animal()

zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)

# 9) Выведите количество животных через метод get_animals_count()

print("Количество животных в зоопарке:", zoo.get_animals_count())

# 10) Используйте цикл for для перебора всех животных зоопарка:
#     - Для каждого животного вызовите функцию animal_sound()
#     - Это должно продемонстрировать полиморфизм

for animal in zoo.get_animals():
    animal_sound(animal)

# 11) Попробуйте создать объект Animal() напрямую — объясните в комментарии, что произошло и почему
# animal = Animal()
# Ошибка TypeError:
# Нельзя создать объект абстрактного класса Animal,
# потому что в нем есть абстрактный метод make_sound(),
# который должен быть реализован в дочерних классах
