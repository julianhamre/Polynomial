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
    def __init__(self, coef):
        self.coef = coef
        self.r_coef = reverse(coef)
        
    def get_coefficients(self):
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
             
    def differenciate(self):
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
        fd = self.differenciate()
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
            raise RuntimeError(f"{self} has no roots")
    
    
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
    fd = f.differenciate()
    x = start_value
    count = 0
    while abs(f.evaluate(x)) > 0.000001:
        if count > 100:
            raise RuntimeError("No root found after 100 iterations")
        x = x - f.evaluate(x) / fd.evaluate(x)
        count += 1
    return x

"""
def solve_next_root(polynomial, start_value):
     f = polynomial
     fd = f.differenciate()
     if
"""
    

"""
a = [1, 2, 3]

g = poly2(a)
gd = g.differenciate()
print(gd.coef)
"""








a = [3, 2, -10, 50]



g = polynomial(a)
print(g.get_coefficients())

pol_plot(g, -5, 5)

print(g.get_extremum(-5))









"""
a = [9.81, 22]
p = polynomial(a)

print(pol_solve(p, 1))

"""

"""
print(f.evaluate(5))
print(type(f))
print(type("hello"))

#print(pol_solve(f, 10000))
"""

"""
f.add_constant(-3)
print(f.get_coefficients())
fd = f.differenciate()
print(fd.get_coefficients())
fd.add_constant(4)
print(fd.get_coefficients())
"""

#pol_plot(f, -2, 2)
#print(f.evaluate(3))
#print(f.get_coefficients())
#print(f.reverse)
#print("f dif", f.differenciate())
#print("g dif", g.differenciate())



"""
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

trend = np.polyfit(x, y, 2)
fn = np.poly1d(trend)

print(trend)
print(fn)
"""