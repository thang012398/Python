# -*- coding: utf-8 -*-
"""
Created on Fri May  1 10:03:43 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["font.size"] = 8.0


np.random.seed(1)

# data

data1 =  np.random.random([6,50])

color1 = ["C{}".format(i) for i in range(6)]

lineoffset1 = np.array([-15,-3,1,1.5,6,10])
linelength1 = [5,2,1,1,3,1.5]

fig,ax = plt.subplots(2,2)

ax[0,0].eventplot(data1,colors=color1,lineoffsets = lineoffset1,
  linelengths=linelength1)
ax[1,0].eventplot(data1,colors=color1,lineoffsets=lineoffset1,
  linelengths=linelength1,orientation="vertical")

data2 = np.random.gamma(4,size=[60,50])

color2 = "black"

lineoffset2 = 1
linelength2 = 1

#create the horizontal plot

ax[0,1].eventplot(data2,colors = color2,lineoffsets=lineoffset2,
  linelengths=linelength2)
# create the vertical plot

ax[1,1].eventplot(data2,colors=color2,lineoffsets=lineoffset2,
  linelengths=linelength2,orientation="vertical")


















































