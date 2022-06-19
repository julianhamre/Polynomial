#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 16:46:54 2022

@author: julianhamre
"""

import unittest
import numpy as np
import poly_tools as pt


def round_numbers(numbers, decimals):
    rounded = []
    for n in numbers:
        rounded.append(round(n, decimals))
    return rounded 


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
    
    def test_evaluate(self):
        values = [0, 3, -2.54, 50]
        coef_1_eval = [4, 37, 18.2748, 7604]
        coef_2_eval = [-2, 1066.3834, -675.9197, 1550398797]
        eval_1_and_2 = [coef_1_eval, coef_2_eval]
        for i in range(0, self.ln):
            poly = pt.polynomial(self.coef_1_and_2[i])
            meth_eval = poly.evaluate_values(values)
            meth_eval = round_numbers(meth_eval, 4)
            self.assertEqual(meth_eval, round_numbers(eval_1_and_2[i], 4))
    
    def test_differentiate(self):
        dif_1 = [6, 2]
        dif_2 = [25, -8, 9.8826, -10, -9.52]
        dif_1_and_2 = [dif_1, dif_2]
        for i in range(0, self.ln):
            poly = pt.polynomial(self.coef_1_and_2[i])
            self.assertEqual(poly.differentiate().get_coef(), dif_1_and_2[i])


if __name__ == "__main__":
    unittest.main()
