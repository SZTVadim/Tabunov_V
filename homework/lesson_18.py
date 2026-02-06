from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")


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


def animal_sound(animal):
    animal.make_sound()

# Это полиморфизм потому-что мы вызываем одну и ту же функцию у кошки и собаки


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)
zoo = Zoo("Городской зоопарк")

zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)

print("Количество животных в зоопарке:", zoo.get_animals_count())

for animal in zoo.get_animals():
    animal_sound(animal)

# 11) Попробуйте создать объект Animal() напрямую
# объясните в комментарии, что произошло и почему
# animal = Animal()
# Ошибка TypeError:
# Нельзя создать объект абстрактного класса Animal,
# потому что в нем есть абстрактный метод make_sound(),
# который должен быть реализован в дочерних классах
