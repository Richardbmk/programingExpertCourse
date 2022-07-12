# This suite of tests is written to run against your code
# so that we can check its correctness.

import unittest

import program


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        result = program.add_values(1, 2, 3)
        self.assertEquals(6, result)

    def test_case_2(self):
        result = program.add_values(2, 4, 3)
        self.assertEquals(9, result)

    def test_case_3(self):
        result = program.add_values(2, 0, 0)
        self.assertEquals(2, result)

    def test_case_4(self):
        result = program.add_values(-2, -4, 2)
        self.assertEquals(-4, result)

    def test_case_5(self):
        result = program.add_values(1.5, 2.3, 8.1)
        self.assertAlmostEqual(11.9, result)

    def test_case_6(self):
        result = program.max_length("", "")
        self.assertEqual(0, result)

    def test_case_7(self):
        result = program.max_length("hello", "tim")
        self.assertEqual(5, result)

    def test_case_8(self):
        result = program.max_length("no", "yes")
        self.assertEqual(3, result)

    def test_case_9(self):
        result = program.max_length("         ", "testing")
        self.assertEqual(9, result)

    def test_case_10(self):
        result = program.create_set([1, 2, 3], [2, 3])
        self.assertEqual(set([1, 2, 3]), result)

    def test_case_11(self):
        result = program.create_set([], [])
        self.assertEqual(set([]), result)

    def test_case_12(self):
        result = program.create_set([], [2, 3])
        self.assertEqual(set([2, 3]), result)

    def test_case_13(self):
        result = program.create_set([1, 2, 3, 4], [4, 5, 6])
        self.assertEqual(set([1, 2, 3, 4, 5, 6]), result)
