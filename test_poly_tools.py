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
    
    def create_poly(self):
        return pt.polynomial(self.coef)
 
    def create_array_poly(self):
        return pt.polynomial(np.array(self.coef))
        
    def setUp(self):
        self.coef = [5, -2, 3.2942, 0, -9.52, -2]
        self.poly = self.create_poly()
        self.array_poly = self.create_array_poly()

    def test_reverse(self):
        rev = [-2, -9.52, 0, 3.2942, -2, 5]
        func_rev = pt.reverse(self.coef)
        self.assertEqual(rev, func_rev)

    def test_get_coef(self):
        get_c = self.array_poly.get_coef()
        self.assertEqual(self.coef, get_c)

    def test_coef_as_list(self):
        self.array_poly.coef_as_list()
        self.assertEqual(self.poly.coef, self.coef)        

    def test_evaluate(self):
        values = [0, -3, -7.54, 56]
        evaluated = [-2, -1439.3834, -129656.8601, 2734567867.1072]
        method_evaluated = self.poly.evaluate_values(values)
        round_method_evaluated = round_numbers(method_evaluated, 4)
        self.assertEqual(round_method_evaluated, evaluated)
    
    def test_differentiate(self):
        dif = [25, -8, 9.8826, 0, -9.52]
        poly_dif = self.poly.differentiate()
        self.assertEqual(poly_dif.get_coef(), dif)

    def test_add_constant(self):
        constants = [0, 1, 104, -4, -3.6]
        results = [-2, -1, 102, -6, -5.6] 
        method_results = []
        for i in constants:
            self.coef = [5, -2, 3.2942, 0, -9.52, -2]
            refresh_poly = self.create_poly()
            refresh_poly.add_constant(i)
            method_results.append(refresh_poly.coef[-1])
        self.assertEqual(results, method_results) 


if __name__ == "__main__":
    unittest.main()
