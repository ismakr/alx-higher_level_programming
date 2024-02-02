#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def max_big(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def max_mid(self):
        self.assertEqual(max_integer([3, 2, 5, 1, 4]), 5)

    def noarg_case(self):
        self.assertEqual(max_integer(), None)

    def neg_num(self):
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def all_neg_num(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def one_el(self):
        self.assertEqual(max_integer([1]), 1)

    def empty_list(self):
        self.assertEqual(max_integer([]), None)

    def float_test(self):
        self.assertEqual(max_integer([1.1, 2.3, 5.4]), 5.4)

    def string_test(self):
        self.assertEqual(max_integer("test"), 't')


if __name__ == '__main__':
    unittest.main()
