# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:07:32 2022

@author: Ian Ah
"""

import os

import numpy as np

#Question 2
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12]])

#Question 3
A[1,2]

A[0]

A[:,1]

A[1:3,2:4]

#Question 4
B = np.array(2*A-8)

np.sum(B, axis=1)

np.sum(B, axis=0)

np.cumsum(B, axis=1)

np.cumsum(B, axis=0)
#Question 5
log_array = np.log(B)

sqrt_array = np.sqrt(B)

sq_array = np.square(B)

abs_array = np.abs(B)

#Question 6
X = np.array([[1, 20],[1, -40]])
Y = np.array ([286, 88])

#To confirm the inverse
X_inv = np.linalg.inv(X)
X.dot(X_inv)

X_sol = X_inv.dot(Y)
print(X_sol)
#To Confirm Solution 
X.dot(X_sol)
