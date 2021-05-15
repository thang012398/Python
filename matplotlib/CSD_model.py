# -*- coding: utf-8 -*-
"""
Created on Fri May  1 01:49:47 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib.pyplot as plt

dt=0.01
t = np.arange(0,30,dt)
np.random.seed(1)

nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

r = np.exp(-t/0.05)

cnse1 = np.convolve(nse1,r,mode="same")*dt
cnse2 = np.convolve(nse2,r,mode="same")*dt

s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2

fig,ax = plt.subplots(2,1)

ax[0].plot(t, s1, t, s2)
ax[0].set_xlim(0, 5)
ax[0].set_xlabel('time')
ax[0].set_ylabel('s1 and s2')
ax[0].grid(True)

cxy, f = ax[1].csd(s1, s2, 256, 1. / dt)
ax[1].set_ylabel('CSD (db)')
plt.show()






