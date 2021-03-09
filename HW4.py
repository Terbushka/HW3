# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.__seating_capacity = seating_capacity

    def seating_capacity(self):
        return self.__seating_capacity


# 3. Determine which class a given Bus object belongs to (Check type of an object)

bus = Bus(200, 12500, 60)
print(type(bus))
print(isinstance(bus, Bus))
print(issubclass(Bus, Vehicle))
# 4. Determine if School_bus is also an instance of the Vehicle class

print(isinstance(bus, Vehicle))


# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students

    def get_school_id(self):
        return self.school_id


# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color

class SchoolBus(School, Bus):
    def __init__(self, school_id, max_speed, mileage, seating_capacity, bus_school_color, number_of_students):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.__bus_school_color = bus_school_color

    def bus_school_color(self):
        return self.__bus_school_color


# 4. Determine if School_bus is also an instance of the Vehicle class

print(issubclass(SchoolBus, Vehicle))


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.

class Bear:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('Roar')
class Wolf:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('Growl')

bear = Bear('Ted', 2)
wolf = Wolf('White Fang', 1)

for animal in (bear, wolf):
    animal.make_sound()


# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            return "Your city is too small."


# 9. Override a printable string representation of the City class and return: The population of the city {name} is {population}

    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'


# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.

class Count:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        if self.count > 10 or other.count > 10:
            total_count = self.count * other.count
        else:
            total_count = self.count + other.count
        return Count(total_count)

    def __str__(self):
        return f'Count: {self.count}'

c1 = Count(2)
c2 = Count(9)
c3 = c1 + c2
print(c3)

c4 = Count(12)
c5 = Count(9)
c6 = c4 + c5
print(c6)


# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.

class CallSum:
    def __call__(self, *args):
        return sum(args)
result = CallSum()
print(result(3, 4, 5))


# 12. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 0:
            return True
        else:
            return False
        
order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))
