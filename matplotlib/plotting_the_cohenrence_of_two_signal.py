# -*- coding: utf-8 -*-
"""
Created on Fri May  1 01:41:47 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

dt = 0.01

t = np.arange(0,30,dt)
nse1 = np.random.randn(len(t))
nse2 = np.random.randn(len(t))

s1 = np.sin(2*np.pi*10*t)+nse1
s2 = np.sin(2*np.pi*10*t)+nse2

fig,ax = plt.subplots(2,1)
ax[0].plot(t,s1,t,s2)
ax[0].set_xlim(0,2)
ax[0].set_xlabel("time")
ax[0].set_ylabel("s1 and s2")

ax[0].grid(True)

cxy,f = ax[1].cohere(s1,s2,256,1./dt)
ax[1].set_ylabel("coherence")
fig.tight_layout()

