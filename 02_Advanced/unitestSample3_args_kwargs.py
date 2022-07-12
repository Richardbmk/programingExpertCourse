# This suite of tests is written to run against your code
# so that we can check its correctness.

import unittest

import program


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        args = ["a", [2], 3]
        kwargs = {"num": 4}
        result = program.get_args_and_kwargs(*args, **kwargs)
        self.assertFalse(result)

    def test_case_2(self):
        args = ["a", [2], 3]
        kwargs = {"num": 6}
        result = program.get_args_and_kwargs(*args, **kwargs)
        self.assertTrue(result)

    def test_case_3(self):
        args = ["a", [2]]
        kwargs = {"num": 6, "x": True}
        result = program.get_args_and_kwargs(*args, **kwargs)
        self.assertTrue(result)

    def test_case_4(self):
        args = [2, 3]
        kwargs = {"num": 6, "a": 1, "b": 2}
        result = program.get_args_and_kwargs(*args, **kwargs)
        self.assertTrue(result)

    def test_case_5(self):
        args = [2, 3]
        kwargs = {"number": 7, "a": 1, "b": 2}
        result = program.get_args_and_kwargs(*args, **kwargs)
        self.assertFalse(result)

    def test_case_6(self):
        args = [2, 3, 4, 5, 6, 7]
        kwargs = {}
        result = program.get_args_and_kwargs(*args, **kwargs)
        self.assertFalse(result)

    def test_case_7(self):
        args = []
        kwargs = {}
        result = program.get_args_and_kwargs(*args, **kwargs)
        self.assertFalse(result)

    def test_case_8(self):
        args = []
        kwargs = {"num": 245}
        result = program.get_args_and_kwargs(*args, **kwargs)
        self.assertFalse(result)

    def test_case_9(self):
        args = [2, 3, 4, 5, 6, 7]
        kwargs = {"num": 56.7}
        result = program.get_args_and_kwargs(*args, **kwargs)
        self.assertTrue(result)
