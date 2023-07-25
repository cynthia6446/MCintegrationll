# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:37:06 2023

@author: be
"""
import numpy  as np
import MC_Double as mc

def f(x):
    return (x**2)
print(f(.5))

n = 10
x0 = 0
x1 = 1
y0 = 0
y1 = 1
ans = mc.MonteCarlo_double