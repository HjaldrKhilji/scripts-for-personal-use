#!/usr/bin/env python
from tkinter import *
import tkinter as tk
import os


base_working_dir='/.Files used by personal scripts'
base_working_dir_for_helper_scripts=f"{base_working_dir}/helper_scripts"
working_dir_for_this_script=f"{base_working_dir_for_helper_scripts}/brightness_scripts"
print(f"working dir for this script: {working_dir_for_this_script}")




def update_session_independently(nightlight_value, brightness_value):
        with open(f"{working_dir_for_this_script}/BRIGHTNESS_service_command", "w+") as f:
                f.write(f"#!/sbin/openrc-run \ngammastep -P -O {nightlight_value} -b {brightness_value} \n")
def update_settings(nightlight_value, brightness_value):
        os.system(f"gammastep -P -O {nightlight_value} -b {brightness_value} ")
        update_session_independently(nightlight_value, brightness_value)

def format_brightness(brightness_value):
        return int(brightness_value)/100

def update_nightlight(nightlight_value):
        update_settings(nightlight_value, format_brightness(brightness.get()))
def update_brightness(brightness_value):
        update_settings(nightlight.get(), format_brightness(brightness_value))




master = Tk()
nightlight_label = tk.Label(master, text="nightlight (lower is more nightlight)")
nightlight_label.pack()
nightlight = Scale(master, command=update_nightlight, from_=1000, to=25000, length=1000,tickinterval=1500,orient=HORIZONTAL)
nightlight.set(4500)
nightlight.pack()


brightness_label = tk.Label(master, text="brightness (lower is darker)")
brightness_label.pack()
brightness = Scale(master, command=update_brightness, from_=10, to=100,length=600, tickinterval=10, orient=HORIZONTAL)
brightness.set(20)
brightness.pack()
mainloop()

#to install tkinter, buld python with the "tk" USE flag
