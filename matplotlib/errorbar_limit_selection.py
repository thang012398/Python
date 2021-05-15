# -*- coding: utf-8 -*-
"""
Created on Fri May  1 01:54:51 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05,0.2,10)

plt.errorbar(x,y+3,yerr=yerr,label="both limit(defaults)")
plt.errorbar(x,y+2,yerr=yerr,uplims = True,label="uplims=True")
plt.errorbar(x,y+1,yerr=yerr,uplims=True,lolims=True,label="Uplims=True,lolims=True")
plt.errorbar(x,y,yerr=yerr,uplims=[True, False] * 5,lolims=[False, True] * 5,label="subsets uplims and lolims")







