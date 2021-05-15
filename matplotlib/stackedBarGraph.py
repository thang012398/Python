# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:26:43 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)

menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
width = 0.35
x = np.arange(N)

p1 = plt.bar(x,menMeans,width,label = "Man",yerr = menStd)
p2 = plt.bar(x,womenMeans,width,menMeans,label="Woman",yerr = menStd)

plt.xticks(x,("G1","G2","G3","G4","G5"))
plt.yticks(np.arange(0,81,10))
plt.legend()







