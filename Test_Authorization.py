import unittest
from Authorization import *


class TestDB(unittest.TestCase):
    def test_reg(self):
        with self.assertRaises(ShortEmailError):
            DB().reg('short@meta.ua', "qwerty123")
        with self.assertRaises(IncorrectEmailError):
            DB().reg('@wrongemail..', "qwerty123")
        with self.assertRaises(WrongSymbEmailError):
            DB().reg('wrongsymb?@yahoo.com', "qwerty123")
        with self.assertRaises(ShortPassError):
            DB().reg('normal_email@gmail.com', "qwerty123")
        with self.assertRaises(WrongSymbPassError):
            DB().reg('normal_email@gmail.com', "qwerty1234567###")
        with self.assertRaises(AlreadyRegistered):
            DB().reg('truemail@gmail.com', "qwerty1234567890")
        self.assertEqual(DB().reg('truemail2@gmail.com', "qwerty1234567890"), "200")

    def test_auth(self):
        with self.assertRaises(WrongEmailError):
            DB().auth('falsemail@gmail.com', "qwerty1234567890")
        with self.assertRaises(WrongPassError):
            DB().auth('truemail@gmail.com', "qwerty123")
        self.assertIsInstance(DB().auth('truemail@gmail.com', "qwerty1234567890") ,UserToken)