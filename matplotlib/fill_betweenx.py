# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:32:43 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")
y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(4 * np.pi * y)

fig,ax = plt.subplots(1,3,sharex=True,figsize=(6,6))

ax[0].fill_betweenx(y,0,x1)
ax[0].set_title("fill between 0 and x1")


ax[1].fill_betweenx(y,x1,1)
ax[1].set_title("between x1 and 1")

ax[2].fill_betweenx(y,x2,x1)
ax[2].set_title("between x1 and x2")

fig,ax = plt.subplots(1,2,sharex=True,figsize=(6,6))
ax[0].plot(x1,y,x2,y,lw=2,color="black")
ax[0].fill_betweenx(y,x1,x2,where=x1<=x2,color="green",interpolate=True)
ax[0].fill_betweenx(y,x1,x2,where=x1>=x2,color="red",interpolate=True)
ax[0].set_title("fill where")

x2 = np.ma.masked_greater(x2,1.0)
ax[1].plot(x1,y,x2,y,lw=2,color="black")
ax[1].fill_betweenx(y, x1, x2, where=x2 >= x1, facecolor='green',interpolate=True)
ax[1].fill_betweenx(y, x1, x2, where=x2 <= x1, facecolor='red',interpolate=True)
ax[1].set_title('regions with x2 > 1 are masked')

















