# -*- coding: utf-8 -*-
"""
Created on Fri May 29 07:30:43 2020

@author: ThangNguyenHuu

Department of Mechanical Engineering
"""
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import time
from datetime import datetime

root = Tk()
root.title("Clock")

w = Canvas(root,width=500,height=500,bg="white")
#w.create_image(10,10,image=image,anchor=NW)
w.pack()

nx = 300
ny = 300
r1 = 140
r2 = 155
r3 = 175
r_text = 175



# initialize
def display():   
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour =  float(current_time[0:2])
    minute = float(current_time[3:5])
    second = float(current_time[6:8])
        
    phi3 = (second-15)*360/60*np.pi/180
    phi2 = (minute-15+second/60)*360/60*np.pi/180
    phi1 = (hour-3+minute/60)*360/12*np.pi/180
    
    
    theta = -3*360/12*np.pi/180
    
    for i in range(1,13):
        theta += 360/12*np.pi/180
        w.create_text(250+r_text*np.cos(theta),
                      250+r_text*np.sin(theta),
                      text=i,
                      font=("Helvetica", 32))
    
    w.create_line(250,250,
                  250+r1*np.cos(phi1),
                  250+r1*np.sin(phi1),
                  fill="red",
                  arrow=LAST,
                  width=10)
    
    w.create_line(250,250,
                  250+r2*np.cos(phi2),
                  250+r2*np.sin(phi2),
                  fill="blue",
                  arrow=LAST,
                  width=5)
    
    w.create_line(250,250,
                  250+r3*np.cos(phi3),
                  250+r3*np.sin(phi3),
                  fill="green",
                  arrow=LAST,
                  width=3)
    
    
    w.create_rectangle(50, 50,450,450,width=2)
    
    w.create_oval(50, 50,450,450,
                  outline="black")
    
    w.create_oval(240,260,260,240,
                  fill="black",
                  outline="cyan")
    
    root.update()

def del_canvas():
    w.delete("all")
    
while True:
    display()
    del_canvas()

root.mainloop()

































