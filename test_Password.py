import unittest

from Password import Password


class PasswordTest(unittest.TestCase):

    def test_Pass_if_number_is_in_increasing_order(self):
        number = 123445
        password = Password()
        self.assertTrue(password.validate(number))

    def test_Fail_if_number_Not_in_increasing_order(self):
        number = 123456
        password = Password()
        self.assertFalse(password.validate(number))

    def test_Fail_if_No_element_is_double(self):
        number = 123456
        password = Password()
        self.assertFalse(password.validate(number))

    def test_Pass_If_element_is_double_and_increasing(self):
        number = 156788
        password = Password()
        self.assertTrue(password.validate(number))

    def test_Fail_If_element_is_double_but_Not_increasing(self):
        number = 156722
        password = Password()
        self.assertFalse(password.validate(number))

    def test_to_return_number_of_validate_password(self):
        numbers = [123456, 122345, 1223312, 122334, 111331, 123445]
        password = Password()
        self.assertEqual(3, password.check_validate(numbers))
