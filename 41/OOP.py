# Принцип Наслідування та Універсальність (Abstraction)
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

# Принцип Поліморфізм
class Dog(Animal):
    def make_sound(self):
        return "GAV!"

class Cat(Animal):
    def make_sound(self):
        return "MYAU!"

# Принцип Інкапсуляції (public, protected, private)
class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals(self):
        return self.__animals

# Створення екземплярів класів
zoo = Zoo()
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Додавання тварин до зоопарку
zoo.add_animal(dog)
zoo.add_animal(cat)

# Виведення звуків тварин
for animal in zoo.get_animals():
    print(f"{animal.name} says: {animal.make_sound()}")