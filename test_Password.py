import unittest

from Password import Password


class PasswordTest(unittest.TestCase):

    def test_Pass_if_number_should_be_in_increasing_order(self):
        number = 12345
        password = Password()
        self.assertTrue(password.validate(number))




