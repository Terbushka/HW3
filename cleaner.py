from time import sleep


class BatteryDischarging(Exception):
    pass


class BatteryEmpty(Exception):
    pass


class NoWater(Exception):
    pass


class Container(Exception):
    pass


class CleaningStop(Exception):
    pass


class RobotVacuumCleaner:
    battery_discharge = 5
    water_consumption = 10
    filling_the_container = 10
    cleaning_time = 5  # Number of minutes (iterations) to clean

    def __init__(self, battery_charge, garbage_container, amount_of_water):
        self.battery_charge = int(battery_charge)
        self.garbage_container = int(garbage_container)
        self.amount_of_water = int(amount_of_water)

    def move(self):
        print('Loading...')
        while self.cleaning_time != 0:
            sleep(1)
            try:
                self.cleaning_time -= 1
                if self.cleaning_time == 0:
                    raise CleaningStop
            except CleaningStop:
                print('Done with cleaning')
                break
            try:
                print(f'Robot vacuum cleaner moving \n'
                      f'battery charge - {self.battery_charge} % \n')
                self.battery_charge -= self.battery_discharge
                if self.battery_charge <= 20:
                    if self.battery_charge == 0 or self.battery_charge < 0:
                        raise BatteryEmpty
                    raise BatteryDischarging
            except BatteryDischarging:
                print(f'Warning! The battery is discharging - {self.battery_charge} % \n')
            except BatteryEmpty:
                print(f'The battery is discharged!')
                break

            try:
                print('Cleaner working')
                self.vacuum_cleaner()
                if self.garbage_container == 100:
                    raise Container
            except Container:
                print('Container is  full, please clean it up!')
                input('Press "Enter" to clean container... ')
                print()
                self.garbage_container = 0

            try:
                if self.amount_of_water > 0:
                    print('Robot vacuum cleaner washes')
                    self.wash()
                else:
                    raise NoWater
            except NoWater:
                print('There is no water, please fill up tank. \n')

    def wash(self):
        self.amount_of_water -= self.water_consumption
        print(f'water level - {self.amount_of_water} % \n')

    def vacuum_cleaner(self):
        self.garbage_container += self.filling_the_container
        print(f'Trash level in container - {self.garbage_container} % \n')