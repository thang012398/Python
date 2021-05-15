# -*- coding: utf-8 -*-
"""
Created on Fri May  1 09:45:21 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1,4,0.1)
y = np.exp(-x)

yerr = 0.1 + 0.1*np.sqrt(x)

fig,ax = plt.subplots(nrows=1,ncols=2,sharex=True)

ax[0].errorbar(x,y,yerr)
ax[1].errorbar(x,y,yerr,yerr,errorevery=5)









