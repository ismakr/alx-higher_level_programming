#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def simple_case(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def noarg_case(self):
        self.assertEqual(max_integer(), None)

    def empty_list(self):
        self.assertEqual(max_integer([]), None)

    def float_test(self):
        self.assertEqual(max_integer([1.1, 2.3, 5.4]), 5.4)

    def string_test(self):
        self.assertEqual(max_integer("test"), 't')


if __name__ == '__main__':
    unittest.main()
