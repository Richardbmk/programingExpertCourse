# This suite of tests is written to run against your code
# so that we can check its correctness.

import unittest
import program
# import Question3_decorators

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        result = program.add_values(0, 0)
        self.assertEquals(1, result)

    def test_case_2(self):
        result = program.add_values(9, 32)
        self.assertEquals(42, result)

    def test_case_3(self):
        result = program.add_values(-5, 100)
        self.assertEquals(96, result)

    def test_case_4(self):
        result = program.add_values(-10, 22)
        self.assertEquals(13, result)

    def test_case_5(self):
        result = program.add_values(76, 4)
        self.assertEquals(81, result)

    def test_case_6(self):
        result = program.add_values(-4, -2)
        self.assertEquals(-5, result)