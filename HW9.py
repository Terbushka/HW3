# Task 1
# Напишіть калькулятор в якого будуть реалізовані операції додавання, віднімання, множення, ділення, піднесення в степінь,
# взяття з під кореня, пошук відсотку від числа
#
# Огорніть в конструкцію try... except... потенційно "небезпечні" місця, наприклад отримання числа і приведення до типу даних
# або інструкції математичних операцій
#
# заповніть ваш скрипт логами
# Логи здебільшого інформаційні (викликали таку функцію з такими аргументами)
# + логи з помилками
# причому логи повинні записуватись у файл, тому що в консолі ви будете взаємодіяти з калькулятором,
# лог файл завжди відкриваєтсья в режимі дозапису.
# так як ви працюєте з файлом не забудьте про те що це потенційне місце поломки
import logging

try:
    file = open("hw9_task1.log", 'r')
except:
    file = open("hw9_task1.log", 'w')
finally:
    file.close()

log_template = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, filename="hw9_task1.log", filemode="a", format=log_template)


def Addition():
    print('Addition')
    logging.info("Addition")
    str_a = input('First number: ')
    try:
        a = int(str_a)
    except ValueError:
        print('a is not decimal')
        logging.error('not decimal first number to do addition')
        return
    str_b = input('Second number: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to do addition')
        return
    c = a + b
    print(f"{a} + {b} = {c}")
    logging.info(f"Addition is finished, {a}, {b}")
    return c


def Subtraction():
    print('Subtraction')
    logging.info("calling Subtraction")
    str_a = input('First number: ')
    try:
        a = int(str_a)
    except ValueError:
        print('a is not decimal')
        logging.error('not decimal first number to do Subtraction')
        return
    str_b = input('Second number: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to do Subtraction')
        return
    c = a - b
    print(f"{a} - {b} = {c}")
    logging.info(f"Subtraction is finished, {a}, {b}")
    return c


def Multiply():
    print('Multiply')
    logging.info("calling Multiply")
    str_a = input('First num: ')
    try:
        a = int(str_a)
    except ValueError:
        print('a is not decimal')
        logging.error('not decimal first number to do multiplication')
        return
    str_b = input('Second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to do multiplication')
        return
    c = a * b
    print(f"{a} * {b} = {c}")
    logging.info(f"Multiply is  finished, {a}, {b}")
    return c


def Division():
    print('Division')
    logging.info("calling Division")
    str_a = input('First num: ')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to do Division')
        return
    str_b = input('Second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to do Division')
        return
    try:
        c = a / b
        print(f"{a} / {b} = {c}")
        logging.info(f"Division is  finished, {a}, {b}")
        return c
    except ZeroDivisionError:
        print("b is 0, ZeroDivisionError")
        logging.error('trying to divide by zero')
        return


def Expo():
    print('Expo')
    logging.info("calling Expo")
    str_a = input('First num: ')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to do Exponentiation')
        return
    str_b = input('Second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to do Exponentiation')
        return
    try:
        c = a ** b
    except ZeroDivisionError:
        print("0 ^ -1 can't be compute")
        logging.error('Trying 0 ^ -1')
        return
    print(f"{a} ^ {b} = {c}")
    logging.info(f"Exponentiation is  finished, {a}, {b}")
    return c


def Square_root():
    print('Square root')
    logging.info("calling Square_root")
    str_a = input('First num: ')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to do Square root')
        return
    str_b = input('second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to do Square root')
        return
    try:
        c = a ** (1 / b)
        print(f"{a} ^ {b} = {c}")
        logging.info(f"Square root is  finished, {a}, {b}")
        return c
    except ZeroDivisionError:
        print("b is 0, can't get root, ZeroDivisionError")
        logging.error('trying to divide by zero (in degree)')
        return


def Percentage():
    print('-Percentage-')
    logging.info("calling Percentage")
    str_a = input('First num: ')
    try:
        a = int(str_a)
    except ValueError:
        print("a is not decimal")
        logging.error('not decimal first number to do Percentage')
        return
    str_b = input('Second num: ')
    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        logging.error('not decimal second number to do Percentage')
        return
    c = a * b / 100
    print(f"{b}% from {a} = {c}")
    logging.info(f"Percentage is finished, {a}, {b}")
    return c


Addition()
Subtraction()
Multiply()
Division()
Expo()
Square_root()
Percentage()

# ---------------------------------------------------------
# Task 2
# Напишіть клас робота пилососа
# в ініт приймається заряд батареї, заповненість сміттєбака і кількість води
#
# реалізуйте функцію move() - нескінченний цикл який на кожній ітерації "замерзає" на 1 сек
# окрім цього на кожній ітерації викликаються функції "wash" і "vacuum cleaner"
# (в цих функціях повинні стояти прніти "wash" і "vacuum cleaner" відповідно),
# також на кожній ітерації прінтиться "move"
# + на кожній ітерації цикла заряд батареї і кількість води зменшується на певну кількість
# (задайте в статік аргументах класу як конфіг пилососа, або в окремому конфіг файлі),
# а кількість сміття збільшується
#
# Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%, кількість води - 0, кількість сміття більша ніж певне число
# опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20% то цикл робить ще певну кількість ітерацій і зупиняється,
# якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
# 0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)

import time
import random


class LowPower(Exception):
    pass


class NoPower(Exception):
    pass


class NoWater(Exception):
    pass


class AlmostFilledGarbage(Exception):
    pass


class VacuumRobot:
    energy_loss = 2
    water_loss = 2

    def __init__(self, charge_level, garbage_fullness, water_left):
        self.charge_level = charge_level
        self.garbage_fullness = garbage_fullness
        self.water_left = water_left

    def wash(self):
        if self.water_left == 0:
            raise NoWater
            # return
        self.water_left = max(self.water_left - self.water_loss, 0)

    def vacuum_cleaner(self):
        self.garbage_fullness = min(self.garbage_fullness + random.randint(1, 3), 100)
        if self.garbage_fullness > 90:
            raise AlmostFilledGarbage
        if self.garbage_fullness == 100:
            print("Container is full")
            self.garbage_fullness = 0

    def step_end(self):
        self.charge_level = max(self.charge_level - self.energy_loss, 0)
        if self.charge_level == 0:
            raise NoPower
        elif self.charge_level < 20:
            raise LowPower


def wash(robot):
    print('wash')
    robot.wash()


def vacuum_cleaner(robot):
    print('vacuum_cleaner')
    robot.vacuum_cleaner()


test_robot = VacuumRobot(40, 20, 10)


def move(robot):
    i = 4
    k = 0
    while True:
        print("move")
        try:
            wash(robot)
        except NoWater:
            if k == 0:
                print("There is no water, please fill up tank.")
                k += 1
        try:
            vacuum_cleaner(robot)
        except AlmostFilledGarbage:
            print('Container is  full, please clean it up!')
        try:
            robot.step_end()
        except NoPower:
            print("Battery is discharged")
            break
        except LowPower:
            if i == 0:
                print("I need to be charged!!!")
                break
            else:
                print(f"Battery low, {i} steps remaining")
                i = i - 1
        time.sleep(1)


move(test_robot)