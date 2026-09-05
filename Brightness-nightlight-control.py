#!/usr/bin/python
from tkinter import *
import tkinter as tk
import os
def run_command():

    os.system(f"gammastep -P -O {nightlight.get()} -b {brightness.get()/100} ")


master = Tk()
nightlight_label = tk.Label(master, text="nightlight (lower is more nightlight)")
nightlight_label.pack()
nightlight = Scale(master, from_=1000, to=25000, length=1000,tickinterval=1500,orient=HORIZONTAL)
nightlight.set(4500)
nightlight.pack()


brightness_label = tk.Label(master, text="brightness (lower is darker)")
brightness_label.pack()
brightness = Scale(master, from_=10, to=100,length=600, tickinterval=10, orient=HORIZONTAL)
brightness.set(20)
brightness.pack()
Button(master, text='apply', command=run_command).pack()
mainloop()

#to install tkinter, buld python with the "tk" USE flag
#if tkinter shows wierd behaviour, it may be worth adding the "tk" USE flag in /etc/portage/make.conf itself
