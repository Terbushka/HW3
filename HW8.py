from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict
import random
import time
import uuid


@abstractmethod
class Animal(ABC):

    def __init__(self, strength: int, speed: int):
        self.id = None
        self.max_strength = strength
        self.current_strength = strength
        self.speed = speed

    def eat(self, forest: Forest):
        pass


class Predator(Animal):
    def __init__(self, strength: int, speed: int):
        super().__init__(strength, speed)
        self.id = None
        self.max_strength = strength
        self.current_strength = strength
        self.speed = speed

    def eat(self, forest: Forest):
        prey = random.choice(list(forest.animals.values()))
        if prey.id == self.id:
            print('There are no herbivores in the forest')
        else:
            if (self.speed > prey.speed) and (self.current_strength > prey.current_strength):
                print('Predator find prey')
                current_strength = min(self.current_strength + self.max_strength * 0.5, self.max_strength)
                print(f'Predator regained {current_strength} strength')
            else:
                self.current_strength = self.current_strength - self.max_strength * 0.3
                print(f'Predator didn`t catch the prey and lost strength')
                forest.animals[prey.id].current_strength - 0.3 * forest.animals[prey.id].max_strength


class Herbivorous(Animal):
    def __init__(self, strength: int, speed: int):
        super().__init__(strength, speed)
        self.id = None
        self.max_strength = strength
        self.current_strength = strength
        self.speed = speed

    def eat(self, forest: Forest):
        print('Herbivorous eating')
        current_strength = min(self.current_strength + self.max_strength * 0.5, self.max_strength)
        print(f'Herbivorous regained {current_strength} strength')


AnyAnimal: Any[Herbivorous, Predator]


class Forest():
    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print('New animal in forest', animal)
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print(f'{animal, id} animal gone')
        self.animals.pop(animal.id)

    def any_predator_left(self):
        return not all(isinstance(animal, Herbivorous) for animal in self.animals.values())


def animal_generator():
    while True:
        new_animal = random.choice((Predator(random.randint(25, 100), random.randint(25, 100)),
                                    Herbivorous(random.randint(25, 100), random.randint(25, 100))))
        new_animal.id = uuid.uuid4()
        yield new_animal


if __name__ == "__main__":
    forest = Forest()
    nature = animal_generator()

    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        animal_to_remove = []
        for animal in forest.animals.values():
            if animal.current_strength < 1:
                animal_to_remove.append(animal.id)
        for animal_id in animal_to_remove:
            forest.remove_animal(forest.animals[animal_id])
        if not forest.any_predator_left():
            print('All predators is dead!')
            break
        for animal in forest.animals.values():
            animal.eat(forest=forest)
        time.sleep(1)