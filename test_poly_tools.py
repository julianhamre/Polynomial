#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 16:46:54 2022

@author: julianhamre
"""

import unittest
import numpy as np
import poly_tools as pt

class testPoly_tools(unittest.TestCase):
    def test_reverse(self):
        forward_list = [5, 4, 3, 2, 1]
        reversed_list = [1, 2, 3, 4, 5]
        func_reversed_list = pt.reverse(forward_list)
        self.assertEqual(reversed_list, func_reversed_list)

    def test_get_coef(self):
        coef = [3, 2, 4]
        array_coef = np.array(coef)
        poly = pt.polynomial(array_coef)
        get_coef = poly.get_coef()
        self.assertEqual(coef, get_coef)


if __name__ == "__main__":
    unittest.main()
