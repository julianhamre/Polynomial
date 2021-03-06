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
    
    def fabricate_poly(self):
        return pt.polynomial(self.coef)
        
    def setUp(self):
        self.coef = [5, -2, 3.2942, 0, -9.52, -2]
        self.poly = self.fabricate_poly()

    def test_check_list_type(self):
        with self.assertRaises(TypeError):
            pt.polynomial(np.array(self.coef))
        try:
            self.fabricate_poly()
        except TypeError:
            self.fail("TypeError raised when coefficients were valid type")

    def test_check_coef_types(self):
        list_of_coefs = [[1, 2, "3"], [1, np.int64(2)]]
        for c in list_of_coefs:
            with self.assertRaises(TypeError):
                pt.polynomial(c)

    def test_reverse(self):
        rev = [-2, -9.52, 0, 3.2942, -2, 5]
        func_rev = pt.reverse(self.coef)
        self.assertEqual(rev, func_rev)

    def test_get_coef(self):
        get_c = self.poly.get_coef()
        self.assertEqual(self.coef, get_c)  

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
            refresh_poly = self.fabricate_poly()
            refresh_poly.add_constant(i)
            method_results.append(refresh_poly.coef[-1])
        self.assertEqual(results, method_results) 

    def round_get_ext(self, start_value):
        return round_numbers(self.poly.get_extremum(start_value), 4)

    def test_get_extremum(self):
        ext_A = [-0.6226, 2.3639]
        ext_B = [0.7365, -7.2004]
        all_ext = [ext_A, ext_B]
        start_values = [-0.5, 0.5]
        for i in range(0, len(all_ext)):
            method_ext = self.round_get_ext(start_values[i])
            self.assertEqual(method_ext, all_ext[i])


if __name__ == "__main__":
    unittest.main()
