import unittest
from unittest.mock import patch
from  employee import Employee

class TestEmployee(unittest.TestCase):

    # If we want to run once one method before we run our functions and after we have to use
    # we can do it with 2 class methods - setup and teardown

    @classmethod # we work with class rather than the instance of the class
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")


    # if we don`t want to create every time a new emp_ sample we can use setUp and tearDown methods
    # because if we change data in one employee we have to apply it rest of them
    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Bob", "Mclaus", 40000)
        self.emp_2 = Employee("Tom", "Marcus", 23000)

    def tearDown(self):
        print("tearDown")

    def test_email(self):
        print("test_email")
        # emp_1 = Employee("Bob", "Mclaus", 40000)
        # emp_2 = Employee("Tom", "Marcus", 23000)

        self.assertEqual(self.emp_1.email, "Bob.Mclaus@email.com")
        self.assertEqual(self.emp_2.email, "Tom.Marcus@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Stephanie"

        self.assertEqual(self.emp_1.email, "John.Mclaus@email.com")
        self.assertEqual(self.emp_2.email, "Stephanie.Marcus@email.com")

    def test_fullname(self):
        print("full_name")
        # emp_1 = Employee("Bob", "Mclaus", 40000)self.
        # emp_2 = Employee("Tom", "Marcus", 23000)

        self.assertEqual(self.emp_1.full_name, "Bob Mclaus")
        self.assertEqual(self.emp_2.full_name, "Tom Marcus")

        self.emp_1.first = "John"
        self.emp_2.first = "Stephanie"

        self.assertEqual(self.emp_1.full_name, "John Mclaus")
        self.assertEqual(self.emp_2.full_name, "Stephanie Marcus")

    def test_apply_raise(self):
        print("test_apply_raise")
        # emp_1 = Employee("Bob", "Mclaus", 40000)
        # emp_2 = Employee("Tom", "Marcus", 23000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 42000)
        self.assertEqual(self.emp_2.pay, 24150)

    # Mocked function
    # They are record when they are called
    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Mclaus/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Marcus/June")
            self.assertEqual(schedule, "Bad Response!")

if __name__ == "__main__":
    unittest.main()


"""
Test should be isolated. It means your test should relay on other tests or affect other tests
You should be able to run any test by its self, independent of the other test
Test driven development - you write a test before your write a code. Worth to mention, kind of practice
"""