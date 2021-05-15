# -*- coding: utf-8 -*-
"""
Created on Fri May  1 01:29:25 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib.pyplot as plt

data = {"apple":10,"orange":15,"lemons":5,"limes":20}
names = list(data.keys())
values = list(data.values())

fig,ax = plt.subplots(1,3,figsize=(9,3),sharey=True)
ax[0].bar(names,values)
ax[1].scatter(names,values)
ax[2].plot(names,values)
fig.suptitle("Catergorical plotting")



























