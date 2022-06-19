#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 16:46:54 2022

@author: julianhamre
"""

import unittest
import numpy as np
import poly_tools as pt

class testPoly(unittest.TestCase):
    coef_1 = [3, 2, 4]
    coef_2 = [5, -2, 3.2942, -5, -9.52, -2]
    coef_1_and_2 = [coef_1, coef_2]
    ln = len(coef_1_and_2)
    
    def test_reverse(self):
        reversed_1 = [4, 2, 3]
        reversed_2 = [-2, -9.52, -5, 3.2942, -2, 5]
        rev_1_and_2 = [reversed_1, reversed_2]
        for i in range(0, self.ln):
            func_rev = pt.reverse(self.coef_1_and_2[i])
            self.assertEqual(rev_1_and_2[i], func_rev)

    def array_poly(self, i):
         return pt.polynomial(np.array(self.coef_1_and_2[i]))

    def test_get_coef(self):
        for i in range(0, self.ln):
            poly = self.array_poly(i)
            gc = poly.get_coef()
            self.assertEqual(self.coef_1_and_2[i], gc)

    def test_coef_as_list(self):
        for i in range(0, self.ln):
            poly = self.array_poly(i)
            poly.coef_as_list()
            self.assertEqual(poly.coef, self.coef_1_and_2[i])


if __name__ == "__main__":
    unittest.main()
