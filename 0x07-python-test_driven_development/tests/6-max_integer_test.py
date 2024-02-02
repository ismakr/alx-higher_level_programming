#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def max_end(self):
        """max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def max_big(self):
        """max at the bigi"""
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def max_mid(self):
        """max in the mid"""
        self.assertEqual(max_integer([3, 2, 5, 1, 4]), 5)

    def noarg_case(self):
        """no arg case"""
        self.assertEqual(max_integer(), None)

    def neg_num(self):
        """one neg num"""
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def all_neg_num(self):
        """all neg num"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def one_el(self):
        """one ele in the list"""
        self.assertEqual(max_integer([1]), 1)

    def empty_list(self):
        """empty list"""
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
