# -*- coding: utf-8 -*-
"""
Created on Fri May  1 10:40:41 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0,2,0.01)
y1 = np.sin(2*np.pi*x)
y2 = 1.2*np.sin(4*np.pi*x)

#fig,ax = plt.subplots(3,1,sharex=True)
#
#ax[0].fill_between(x,0,y1)
#ax[0].set_ylabel("between y1 and 0")
#
#ax[1].fill_between(x,y1,1)
#ax[1].set_ylabel("between y1 and 1")
#
#ax[2].fill_between(x,y1,y2)
#ax[2].set_ylabel("between y1 and y2")
#ax[2].set_xlabel("x")


#fig,ax = plt.subplots(2,1,sharex=True)
#
#ax[0].plot(x,y1,x,y2,color="black")
#ax[0].fill_between(x,y1,y2,where=y2>=y1,facecolor="green",interpolate=True)
#ax[0].fill_between(x,y1,y2,where=y2<=y1,facecolor="red",interpolate=True)
#ax[0].set_label("fill between where")
#
#y2 = np.ma.masked_greater(y2,1.0)
#ax[1].plot(x,y1,x,y2,color="black")
#ax[1].fill_between(x,y1,y2,where=y2>=y1,facecolor="green",interpolate=True)
#ax[1].fill_between(x,y1,y2,where=y2<=y1,facecolor="red",interpolate=True)
#ax[1].set_title("Now regions y2>y1 are masked")


fig,ax = plt.subplots()
y = np.sin(4*np.pi*x)
ax.plot(x,y,color="black")

import matplotlib.transforms as mtransforms

trans = mtransforms.blended_transform_factory(ax.transData,ax.transAxes)
theta = 0.9
ax.axhline(theta,color="green",lw=2,alpha=0.5)
ax.axhline(-theta,color="red",lw=2,alpha=0.5)
ax.fill_between(x,0,1, where=y<-theta,facecolor='red', alpha=0.5, transform=trans)

























