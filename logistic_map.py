# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

# Logistic map Function
def logistic_map(r,x):
    return r*x*(1-x)

inp = input("Input value of r: ")
r = float(inp)
x0= 0.5
n = 100

#Initialize array to store sequence
x = np.zeros(n)
x[0]=x0

#generate sequence
for i in range (1,n):
      x[i]=logistic_map(r,x[i-1])
      
#plot the sequence
plt.plot(range(n),x,'-o')
plt.title(f'Logistic Map for r ={r}')
plt.xlabel('Iteration')
plt.ylabel('x')
plt.ylim(0,1)
plt.show()
     