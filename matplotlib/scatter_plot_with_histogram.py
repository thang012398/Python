# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:17:19 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

x = np.random.randn(1000)
y = np.random.randn(1000)

# definations for the axes

left,width = 0.1,0.65
bottom,height = 0.1,0.65
spacing = 0.005

rect_scatter = [left,bottom,width,height]
rect_histx = [left,bottom+height+spacing,width,0.2]
rect_histy = [left + width + spacing, bottom, 0.2, height]

plt.figure(figsize=(8,8))

ax_scatter = plt.axes(rect_scatter)
ax_scatter.tick_params(direction="in",top=True,right=True)
ax_histx = plt.axes(rect_histx)
ax_histx.tick_params(direction="in",labelbottom=False)
ax_histy = plt.axes(rect_histy)
ax_histy.tick_params(direction="in",labelleft=False)

# scatter the plot
ax_scatter.scatter(x, y)

binwidth = 0.25

lim = np.ceil(np.abs([x, y]).max() / binwidth) * binwidth
ax_scatter.set_xlim((-lim,lim))
ax_scatter.set_ylim((-lim,lim))

bins = np.arange(-lim,lim+binwidth,binwidth)
ax_histx.hist(x,bins=bins)
ax_histy.hist(y,bins=bins,orientation="horizontal")
ax_histx.set_xlim(ax_scatter.get_xlim())
ax_histy.set_ylim(ax_scatter.get_ylim())































