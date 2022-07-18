# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:12:03 2022

@author: Ian Ah
"""

import os # not needed for this assignment (-5)

import numpy as np

trials = 1000000
radius = .5
inside = 0

for i in range(trials):
    X_coord = np.random.uniform(0 , 1)
    Y_coord = np.random.uniform(0 , 1)
#Because we are randomizing points from 0 to 1, we must divide them in half 
#since the origin sits at (0.5,0.5) rather than (0,0)  
    dis_from_origin = (X_coord**2 + Y_coord**2)/2
# If the distance from the origin is less than the radius than it must fall 
# inside of the circle 
    if dis_from_origin <= radius:
        inside += 1
        
area = 4 * inside / trials
print("Pi: ", area)


    
  
