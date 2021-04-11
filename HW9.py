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
    file = open('hw9_task1.log', 'r')
except:
    file = open('hw9_task1.log', 'w')
finally:
    file.close()

template_log = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='hw9_task1.log', filemode='a', format=template_log)


def starting():
    logging.info("Start calculator'")


def calculator():

    global number_1, number_2
    logging.info("called calculator function")
    try:
        number_1 = float(input('Enter first number: '))
    except ValueError:
        print('wrong format')
        logging.error("incorrect variable format")
    try:
        number_2 = float(input('Enter second number: '))
    except ValueError:
        print('Wrong format')
        logging.error("incorrect variable format")

    operation = input('''
    Please choose  math operation:
    + for Addition
    - for Subtraction
    * for Multiplication
    / for Division
    ** for Exponentiation
    nrt for n-th root
    per for Percentage of number
    ''')
    logging.info("selected operation")

    if operation == '+':
        logging.info("Addition")
        try:
            print('{} + {} = '.format(number_1, number_2))
            logging.info("Addition completed successfully")
            return print(number_1 + number_2)
        except UnboundLocalError:
            print('One of the numbers is not decimal')
            logging.error("indefinite variable")
    elif operation == '-':
        logging.info("Subtraction")
        try:
            print('{} - {} = '.format(number_1, number_2))
            logging.info("subtraction completed successfully")
            return print(number_1 - number_2)
        except UnboundLocalError:
            print('One of the numbers is not decimal')
            logging.error("indefinite variable")
    elif '*' == operation:
        logging.info("Multiply function is selected")
        try:
            print('{} * {} = '.format(number_1, number_2))
            logging.info("multiplication completed successfully")
            return print(number_1 * number_2)
        except UnboundLocalError:
            print('One of the numbers is not decimal')
            logging.error("indefinite variable")
    elif operation == '/':
        logging.info("Division")
        try:
            print('{} / {} = '.format(number_1, number_2))
            logging.info("Division completed successfully")
            return print(number_1 / number_2)
        except UnboundLocalError:
            print('One of the numbers is not decimal')
            logging.error("indefinite variable")
        except ZeroDivisionError:
            print('division by zero')
            logging.error("attempt to divide by zero")
    elif operation == '**':
        logging.info("Exponentiation is selected")
        try:
            print('{} ** {} = '.format(number_1, number_2))
            logging.info("Exponentiation completed successfully")
            return print(number_1 ** number_2)
        except UnboundLocalError:
            print('One of the numbers is not decimal')
            logging.error("indefinite variable")
        except ZeroDivisionError:
            logging.error("ZeroDivisionError")
            print("Zero can`t be raised to a negative power")
    elif operation == 'nrt':
        logging.info("the n-th root function is selected")
        try:
            print('{} ** (1/{})'.format(number_1, number_2))
            logging.info("n-th root  completed successfully")
            return print(number_1 ** (1 / number_2))
        except UnboundLocalError:
            print('One of the numbers is not decimal')
            logging.error("indefinite variable")
        except ZeroDivisionError:
            print('can not get root, number_2 is zero')
            logging.error("attempt to divide by zero")
    elif operation == 'per':
        logging.info("Percentage cent of number is selected")
        try:
            print('{} * {} / 100'.format(number_1, number_2))
            logging.info("Percentage of number completed successfully")
            return print(number_1 * number_2 / 100)
        except UnboundLocalError:
            print('One of the numbers is not decimal')
            logging.error("indefinite variable")
    else:
        logging.error("non-existent operation selected")
        print('You have not typed a valid operator, please run the program again.')


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
    logging.info("called again function")
    if calc_again.upper() == 'Y':
        calculator()
    elif calc_again.upper() == 'N':
        print('exit')
    else:
        again()


starting()
calculator()
again()

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


class LowWater(Exception):
    pass


class LowBattery(Exception):
    pass


class FullTank(Exception):
    pass


class WithoutWater(Exception):
    pass


class WithoutCharge(Exception):
    pass


class CleanTank(Exception):
    pass


class VacCleaner:
    def __init__(self, water, battery, tank):
        self.water = water
        self.battery = battery
        self.tank = tank

    def wash(self):
        if self.water == 0:
            raise WithoutWater
        else:
            self.water -= 1
            print(f'Washing...\n Water tank is {self.water}%')
            if 2 <= self.water <= 15:
                raise LowWater

    def perc_batt(self):
        if self.battery <= 0:
            raise WithoutCharge
        else:
            self.battery -= 1
            print(f'Moving...\n Battery is {self.battery}%.')
            if 1 <= self.battery <= 20:
                raise LowBattery

    def full_tank(self):
        if self.tank >= 100:
            raise FullTank
        else:
            self.tank += 1
            print(f'Cleaning...\n Tank is {self.tank}%.')
            if 99 >= self.tank >= 90:
                raise CleanTank


def move():
    vac_cleaner = VacCleaner(5, 50, 50)

    print(f'Level of water tank is {vac_cleaner.water}%.')
    print(f'Level of charge {vac_cleaner.battery}%.')
    print(f'Fullness of dust tank is {vac_cleaner.tank}%.')
    print('Start cleaning:')
    while True:
        try:
            vac_cleaner.perc_batt()
        except LowBattery:
            print(f'WARNING: level of battery {vac_cleaner.battery}%. \n Need to be charged.')
        except WithoutCharge:
            print(f'level of battery {vac_cleaner.battery}%. \n Stop working.')
            break

        try:
            vac_cleaner.wash()
        except LowWater:
            print(f'Water is {vac_cleaner.water}%. Please fill up tank.')
        except WithoutWater:
            print(f'Level of water {vac_cleaner.water}%, only dry cleaning...')

        try:
            vac_cleaner.full_tank()
        except CleanTank:
            print(f'WARNING: level of fullness tank is {vac_cleaner.tank}%. \n  Clean tank!!!.')
        except FullTank:
            print(f'Tank is {vac_cleaner.tank}%, only washing!')
        time.sleep(1)


move()
