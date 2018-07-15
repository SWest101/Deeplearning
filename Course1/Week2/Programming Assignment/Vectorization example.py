#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 16:47:56 2018
@Description: Demonstration of the time difference between for loops vs 
              vectorization.
@author: shaun
"""

import numpy as np 
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc  = time.time()

print("Vectorized version:" + str(toc-tic) + "ms")

c = 0
tic = time.time()
for i in range (1000000):
    c += a[i]+b[i]

toc = time.time()
print("Non-Vectorized version:" + str(toc-tic) + "ms")

