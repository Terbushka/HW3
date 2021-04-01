from __future__ import annotations
from typing import Dict, Any
from abc import ABC, abstractmethod
import random
import uuid
import time


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError


class Predator(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, forest: Forest):
        target = random.choice(list(forest.animals.values()))
        if target.id == self.id:
            print('There are no herbivores in the forest')
        else:
            if (self.speed > target.speed) and (self.current_power > target.current_power):
                print('Predator find prey')
                tmp = self.current_power
                self.current_power = min(self.current_power + self.max_power * 0.5, self.max_power)
                print(f'Predator regained {self.current_power - tmp} strength')
                forest.animals[target.id].current_power = 0
            else:
                print('Predator didn`t catch the prey and lost strength')
                self.current_power = self.current_power - 0.3 * self.max_power
                forest.animals[target.id].current_power = forest.animals[target.id].current_power - 0.3 * \
                                                          forest.animals[target.id].max_power

    def __str__(self):
        return f'{self.__class__.__name__}'


class Herbivorous(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def __str__(self):
        return f'{self.__class__.__name__}'

    def eat(self, forest: Forest):
        print('Herbivorous eating')
        tmp = self.current_power
        self.current_power = min(self.current_power + self.max_power * 0.5, self.max_power)
        print(f'Herbivorous regained {self.current_power - tmp} strength')


AnyAnimal = [Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print('New animal in forest', animal)
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print(animal, 'animal gone')
        self.animals.pop(animal.id)

    def any_predator_left(self):
        return not all(isinstance(animal, Herbivorous) for animal in self.animals.values())


def animal_generator():
    while True:
        generated_animal = random.choice((Predator(random.randint(25, 100), random.randint(25, 100)),
                                          Herbivorous(random.randint(25, 100), random.randint(25, 100))))
        generated_animal.id = uuid.uuid4()
        yield generated_animal


if __name__ == "__main__":
    nature = animal_generator()

    forest = Forest()
    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        animal_to_remove = []
        for animal in forest.animals.values():
            if animal.current_power < 1:
                animal_to_remove.append(animal.id)
        for animal_id in animal_to_remove:
            forest.remove_animal(forest.animals[animal_id])
        if not forest.any_predator_left():
            print('All predators is dead!')
            break
        for animal in forest.animals.values():
            animal.eat(forest=forest)
        time.sleep(1)
