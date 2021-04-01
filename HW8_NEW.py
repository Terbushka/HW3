from __future__ import annotations
from typing import Dict, Any
from abc import ABC, abstractmethod
import time
import random
import uuid


class Animal(ABC):

    def __init__(self, id, power: int, speed: int):
        self.id = id
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError

    def _strength_restores(self):
        self.current_power *= 1.5
        if self.current_power > self.max_power:
            self.current_power = self.max_power

    def _strength_loses(self):
        self.current_power *= 0.7
        if self.current_power < 1:
            forest.remove_animal(self)


class Predator(Animal):
    def eat(self, forest: Forest):
        food = forest.animals.get(random.choice(list(forest.animals.keys())))
        if self.id == food.id:
            print(f'Predator {self.id} with speed {self.speed} and power {self.current_power} '
                  f'was unlucky and he is still hungry')
        else:
            print('Tries to catch prey')
            if self.speed > food.speed and self.current_power > food.current_power:
                print(f'Predator {self.id} with speed {self.speed} and power {self.current_power}'
                      f' eats food {food.id} with speed {food.speed} and power {food.current_power}. '
                      f'Also restores 50% of his power')
                self._strength_restores()
                forest.remove_animal(food)
            else:
                print(f'Predator {self.id} with speed {self.speed} and power {self.current_power} '
                      f'did not enough strength and loses 30% of his power.'
                      f'{food.id} with speed {food.speed} and power {food.current_power} loses 30% of strength.')
                self._strength_loses()
                food._strength_loses()


class Herbivorous(Animal):
    def eat(self, forest: Forest):
        print(f'Herbivorous {self.id} is eating')
        self._strength_restores()


AnyAnimal = [Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal: Any] = dict()

    def __iter__(self):
        return iter(list(self.animals.values()))

    def add_animal(self, animal: AnyAnimal):
        self.animals[str(animal.id)] = animal

    def remove_animal(self, animal: AnyAnimal):
        self.animals.pop(str(animal.id))

    def any_predator_left(self):
        return all(isinstance(item, Herbivorous) for item in self.animals.values())


def animal_generator(quantity):
    item = 0
    while item < quantity:
        item += 1
        yield random.choice(AnyAnimal)(uuid.uuid4(), random.randint(25, 100), random.randint(25, 100))


if __name__ == "__main__":
    nature = animal_generator(10)
    forest = Forest()
    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)
    print(forest.animals)
    while True:
        if forest.any_predator_left():
            break
        for animal in forest:
            animal.eat(forest=forest)
        time.sleep(1)
        print(f'\n{len(forest.animals)}\n{forest.animals}\n')
        time.sleep(1)