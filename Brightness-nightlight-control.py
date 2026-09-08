#!/usr/bin/env python
from tkinter import *
import tkinter as tk
import os
import sys
import json


base_working_dir='/.Files used by personal scripts'
base_working_dir_for_helper_scripts=f"{base_working_dir}/helper_scripts"
working_dir_for_this_script=f"{base_working_dir_for_helper_scripts}/brightness_scripts"
service_file="BRIGHTNESS_service_command"
file_with_all_values=f"{base_working_dir}/all_persistant_values.json"
print(f"working dir for this script: {working_dir_for_this_script}\nservice_file(if supported by your init system): BRIGHTNESS_service_command\n")


nightlight_value=4500
brightness_value=20


def log_error(error_message):
        import logging
        import uuid
        error_file_path=f"/tmp/brightness_control_error_{uuid.uuid4()}"
        file_handler= logging.FileHandler(error_file_path, mode="w+", encoding="utf-8")
        stderr_handler= logging.StreamHandler()
        logger=logging.getLogger("logger")
        logger.addHandler(file_handler)
        logger.addHandler(stderr_handler)
        logger.critical(f"{error_message}, reported to file {error_file_path}")
        file_handler.close()

def update_init_system(nightlight_value, brightness_value):
	if (len(sys.argv)==1):
		return "no init system provided (SKIPPING)" 
	elif (sys.argv[1]=="openrc"):
        	with open(f"{working_dir_for_this_script}/{service_file}", "w+") as f:
                	f.write(f"""	#!/sbin/openrc-run 
					gammastep -P -O {nightlight_value} -b {brightness_value}	
				""")
	#eventually the code for each must be broken into functions or atleast for for some init systems
	else:
		log_error("init system not supported")

def save_settings_persistently(nightlight_value, brightness_value):
	with open(file_with_all_values, "w") as f:
		settings = {
			"nightlight_value"      :  nightlight_value,
			"brightness_value"      :  brightness_value,
		}
		json.dump(settings, f)

def update_settings(nightlight_value, brightness_value):
	os.system(f"gammastep -P -O {nightlight_value} -b {brightness_value} &> /dev/null ")
	update_init_system(nightlight_value, brightness_value)
	save_settings_persistently(nightlight_value, brightness_value*100)

def format_brightness(brightness_value):
	return int(brightness_value)/100


def update_nightlight(nightlight_param):
	global brightness_value
	global nightlight_value
	nightlight_value=nightlight_param
	update_settings(nightlight_value, format_brightness(brightness_value))

def update_brightness(brightness_param):
	global brightness_value
	global nightlight_value
	brightness_value=brightness_param
	update_settings(nightlight_value, format_brightness(brightness_value))
	
def load_settings():
	with open(file_with_all_values, "r") as f:
		settings = json.load(f)
		return settings
def main():
	settings= load_settings()
	nightlight_value=settings["nightlight_value"]
	brightness_value=settings["brightness_value"]
	master = Tk()
	nightlight_label = tk.Label(master, text="nightlight (lower is more nightlight)")
	nightlight_label.pack()
	nightlight = Scale(master, command=update_nightlight, from_=1000, to=25000, length=1000,tickinterval=1500,orient=HORIZONTAL)
	nightlight.set(nightlight_value)
	nightlight.pack()
	brightness_label = tk.Label(master, text="brightness (lower is darker)")
	brightness_label.pack()
	brightness = Scale(master, command=update_brightness, from_=10, to=100,length=600, tickinterval=10, orient=HORIZONTAL)
	brightness.set(brightness_value)
	brightness.pack()
	mainloop()

if __name__ == "__main__":
        main()

#to install tkinter, buld python with the "tk" USE flag
