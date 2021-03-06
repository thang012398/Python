# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:55:00 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig,ax = plt.subplots()

rect1 = ax.bar(x-width/2,men_means,width,label="Men")
rect2 = ax.bar(x+width/2,women_means,width,label="Women")
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate("{}".format(height),
                   xy=(rect.get_x()+rect.get_width()/2,height),
                   xytext=(0,3),textcoords="offset points",
                   ha="center",va="bottom")

autolabel(rect1)
autolabel(rect2)
fig.tight_layout()




























