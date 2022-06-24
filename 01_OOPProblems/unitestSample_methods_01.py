# This suite of tests is written to run against your code
# so that we can check its correctness.

import inspect
import unittest

from program import Rectangle


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(inspect.isclass(Rectangle), "Rectangle should be a class.")

    def test_case_2(self):
        rect = Rectangle(7, -9, 5, 5)
        self.assertTrue(hasattr(rect, "get_position"), "A Rectangle should have a `get_position` method.")
        self.assertTrue(hasattr(rect, "get_area"), "A Rectangle should have a `get_area` method.")
        self.assertTrue(hasattr(rect, "change_position"), "A Rectangle should have a `change_position` method.")

    def test_case_3(self):
        rect = Rectangle(7, -9, 5, 5)
        self.assertEqual((7, -9), rect.get_position())

    def test_case_4(self):
        rect = Rectangle(7, -9, 5, 5)
        self.assertEqual(25, rect.get_area())

    def test_case_5(self):
        rect = Rectangle(7, -9, 5, 5)
        self.assertEqual((7, -9), rect.get_position())
        rect.change_position(2, 3)
        self.assertEqual((2, 3), rect.get_position())
