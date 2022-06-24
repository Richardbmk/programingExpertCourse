# This suite of tests is written to run against your code
# so that we can check its correctness.

import inspect
import unittest

from program import Group


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(inspect.isclass(Group), "Group should be a class.")

    def test_case_2(self):
        group = Group("group1", ["A", "C", "B"])
        self.assertTrue(hasattr(group, "get_members"), "A Group should have a `get_members` method.")
        self.assertTrue(hasattr(group, "add"), "A Group should have an `add` method.")
        self.assertTrue(hasattr(group, "delete"), "A Group should have a `delete` method.")

    def test_case_3(self):
        group = Group("group2", ["A", "C", "B"])
        self.assertEqual(["A", "B", "C"], group.get_members())

    def test_case_4(self):
        group = Group("group3", ["A", "C", "B"])
        group.delete("A")
        self.assertEqual(["B", "C"], group.get_members())

    def test_case_5(self):
        group = Group("group4", ["A", "D"])
        group.add("C")
        self.assertEqual(["A", "C", "D"], group.get_members())

    def test_case_6(self):
        group = Group("group5", ["A", "D"])
        with self.assertRaisesRegexp(Exception, "Member not in group"):
            group.delete("Z")
