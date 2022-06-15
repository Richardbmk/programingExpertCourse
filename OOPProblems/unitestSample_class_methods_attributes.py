# This suite of tests is written to run against your code
# so that we can check its correctness.

import inspect
import unittest

from program import Employee


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(inspect.isclass(Employee), "Employee should be a class.")

    def test_case_2(self):
        self.assertTrue(hasattr(Employee, "average_age"), "Employee should have a `average_age` attribute.")
        self.assertTrue(hasattr(Employee, "average_salary"), "Employee should have a `set_balance` attribute.")

    def test_case_3(self):
        employee = Employee("Tim", 10, 65000)
        self.assertEqual(10, Employee.average_age)
        self.assertEqual(65000, Employee.average_salary)

    def test_case_4(self):
        employee = Employee("Clement", 23, 10000)
        self.assertEqual(16.5, Employee.average_age)
        self.assertEqual(37500, Employee.average_salary)

    def test_case_5(self):
        employee = Employee("Conner", 45, 15000)
        self.assertEqual(26, Employee.average_age)
        self.assertEqual(30000, Employee.average_salary)

    def test_case_6(self):
        employee = Employee("Alex", 60, 95000)
        self.assertEqual(34.5, Employee.average_age)
        self.assertEqual(46250, Employee.average_salary)
