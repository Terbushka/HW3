import unittest
from Cleaner import VacuumRobot, simple_move, wash, vacuum_cleaner, NoPower


class TestVacuumRobot(unittest.TestCase):

    def setUp(self) -> None:
        self.test_robot1 = VacuumRobot(100, 0, 100)
        self.test_robot2 = VacuumRobot(0, 0, 100)
        self.test_robot3 = VacuumRobot(200, 200, 200)
        self.test_robot4 = VacuumRobot("100", 0, -100)
        with self.assertRaises(ValueError):
            self.test_robot5 = VacuumRobot("text for ValueError", 0, 100)
        with self.assertRaises(NameError):
            self.test_robot6 = VacuumRobot(non_existed_variable, 0, 100)
        self.test_robots = [self.test_robot1, self.test_robot2, self.test_robot3, self.test_robot4]

    def test_init(self):
        for vac_robot in self.test_robots:
            self.assertIsInstance(vac_robot.battery_charge_level, (float, int))
            self.assertIsInstance(vac_robot.garbage_fullness, (float, int))
            self.assertIsInstance(vac_robot.water_left, (float, int))

    def test_move(self):
        i = 1
        for vac_robot in self.test_robots:
            print(f'Test 5 steps for robot {i}')
            k = 5
            while k > 0:
                try:
                    simple_move(vac_robot)
                    k -= 1
                except NoPower:
                    break
            k -= 1
            i += 1