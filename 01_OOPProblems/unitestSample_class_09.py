# This suite of tests is written to run against your code
# so that we can check its correctness.

import inspect
import unittest

import program


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(hasattr(program, "ContactInformation"))
        self.assertTrue(inspect.isclass(program.ContactInformation), "ContactInformation should be a class.")

    def test_case_2(self):
        self.assertTrue(hasattr(program, "person1"), "Your program should have a variable named `person1`")
        self.assertTrue(hasattr(program, "person2"), "Your program should have a variable named `person2`")

    def test_case_3(self):
        person1 = program.person1
        self.assertTrue(
            isinstance(person1, program.ContactInformation),
            "`person1` should be an instance of the ContactInformation class.",
        )
        self.assertTrue(hasattr(person1, "first_name"), "`person1` should have a `first_name` attribute.")
        self.assertTrue(hasattr(person1, "last_name"), "`person1` should have a `last_name` attribute.")
        self.assertTrue(hasattr(person1, "email"), "`person1` should have a `email` attribute.")
        self.assertTrue(hasattr(person1, "phone_number"), "`person1` should have a `phone_number` attribute.")
        self.assertTrue(hasattr(person1, "country"), "`person1` should have a `country` attribute.")

    def test_case_4(self):
        person2 = program.person2
        self.assertTrue(
            isinstance(person2, program.ContactInformation),
            "`person2` should be an instance of the ContactInformation class.",
        )
        self.assertTrue(hasattr(person2, "first_name"), "`person2` should have a `first_name` attribute.")
        self.assertTrue(hasattr(person2, "last_name"), "`person2` should have a `last_name` attribute.")
        self.assertTrue(hasattr(person2, "email"), "`person2` should have a `email` attribute.")
        self.assertTrue(hasattr(person2, "phone_number"), "`person2` should have a `phone_number` attribute.")
        self.assertTrue(hasattr(person2, "country"), "`person2` should have a `country` attribute.")
