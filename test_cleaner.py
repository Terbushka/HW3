import unittest

from cleaner import RobotVacuumCleaner


class TestRobotVacuumCleaner(unittest.TestCase):

    def setUp(self) -> None:
        self.robot = RobotVacuumCleaner(100, 0, 100)
        self.robot_1 = RobotVacuumCleaner('2', 0, 30)
        self.robot_2 = RobotVacuumCleaner(20.0, 50, 100)
        self.vacuum_cleaners = [self.robot, self.robot_1, self.robot_2]

    def test_init(self):
        with self.assertRaises(ValueError):
            RobotVacuumCleaner('as', 0, 30)

        for item in self.vacuum_cleaners:
            self.assertIsInstance(item.battery_charge, int)
            self.assertIsInstance(item.garbage_container, int)
            self.assertIsInstance(item.amount_of_water, int)

    def test_move(self):
        self.assertNotEqual(RobotVacuumCleaner.battery_discharge, 0)
        self.values_1 = RobotVacuumCleaner(0, 100, 0)
        self.values_1.move()
        self.values_2 = RobotVacuumCleaner(100, 0, 100)
        self.values_2.cleaning_time = 5
        self.values_2.move()

    def test_wash(self):
        self.assertNotEqual(RobotVacuumCleaner.water_consumption, 0)

    def test_vacuum_cleaner(self):
        self.assertNotEqual(RobotVacuumCleaner.filling_the_container, 0)

    def tearDown(self) -> None:
        print('Stop')