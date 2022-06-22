#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 20:21:15 2022

@author: julianhamre
"""

from matplotlib import pyplot as plt
import numpy as np


def reverse(a):
     r = []
     count = -1
     for i in a:
         r.append(a[count])
         count -= 1
     return r


class polynomial:

    def check_list_type(self):
        if not isinstance(self.coef, list):
            raise TypeError(f"In {self.get_coef()}, the coefficients must be type list, got {type(self.coef)}")

    def check_coef_types(self):
        counter = 0
        for c in self.coef:
            t = type(c)
            if t not in [int, float]:
                raise TypeError(f"In {self.get_coef()}, all coefficients must be type int or float, got {t} in element {counter}")
            counter += 1

    def __init__(self, coef):
        self.coef = coef
        self.r_coef = reverse(coef)
        
        self.check_list_type()
        self.check_coef_types()
    
    def get_coef(self):
        a = []
        for i in self.coef:
            a.append(i)
        return a
    
    def evaluate(self, x):
        y = self.r_coef[0]
        for i in range(1, len(self.r_coef)):
            term = self.r_coef[i]*x**i
            y += term
        return y
    
    def evaluate_values(self, values):
        evaluated = []
        for v in values:
            evaluated.append(self.evaluate(v))
        return evaluated
         
    def differentiate(self):
       f = self.r_coef
       d = []
       for i in range(1, len(f)):
           d.append(i*f[i])
       return polynomial(reverse(d))
   
    def add_constant(self, value):
        constant = self.coef[-1]
        self.coef.remove(constant)
        constant += value
        self.coef.append(constant)
        self.r_coef = reverse(self.coef)
        
    def get_extremum(self, start_value):
        fd = self.differentiate()
        solve = pol_solve(fd, start_value)
        return [solve, self.evaluate(solve)]
     
        
class poly2(polynomial):
    def __init__(self, coef):
        length = len(coef)
        if length != 3:
            raise IndexError(f"Second degree polynomials must have 3 coefficients, got {length} coefficients")
        super().__init__(coef)

    def abc_solve(self):
        a = self.coef[0]
        b = self.coef[1]
        c = self.coef[2]
        sq_statement = b**2 - 4*a*c
        
        if sq_statement > 0:
            x1 = (-b + np.sqrt(sq_statement)) / (2*a)
            x2 = (-b - np.sqrt(sq_statement)) / (2*a)
            return [x1, x2]
        elif sq_statement == 0:
            x = -b / (2*a)
            return x
        else:
            raise RuntimeError(f"polynomial {self.get_coef()} has no roots")
    
    
class grav_poly2(poly2):
    def __init__(self, velocity):
        grav = 9.81
        a = - 1./2*grav
        b = velocity
        coef = [a, b, 0]
        super().__init__(coef)
                 

def pol_plot(polynomial, start, end):
    x = np.linspace(start, end, 1001)
    y = polynomial.evaluate(x)
    plt.ylim(-10, 120)
    plt.axvline(color="k")
    plt.axhline(color="k")
    plt.plot(x, y)
    plt.show()

def pol_solve(polynomial, start_value):
    f = polynomial
    fd = f.differentiate()
    x = start_value
    count = 0
    while abs(f.evaluate(x)) > 0.000001:
        if count > 100:
            raise RuntimeError(f"No root found found in {polynomial.get_coef()} after 100 iterations")
        x = x - f.evaluate(x) / fd.evaluate(x)
        count += 1
    return x
