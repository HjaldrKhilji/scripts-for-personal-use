<pre>#!/usr/bin/env python
#example for openrc: python Brightness-nightlight-control.py openrc
from tkinter import *
import tkinter as tk
import os
import sys
import json


base_working_dir=&apos;/.Files used by personal scripts&apos;
base_working_dir_for_helper_scripts=f&quot;{base_working_dir}/helper_scripts&quot;
working_dir_for_this_script=f&quot;{base_working_dir_for_helper_scripts}/brightness_scripts&quot;
service_file=&quot;BRIGHTNESS_service_command&quot;
file_with_all_values=f&quot;{base_working_dir}/all_persistant_values.json&quot;
print(f&quot;working dir for this script: {working_dir_for_this_script}\nservice_file(if supported by your init system): BRIGHTNESS_service_command\n&quot;)
print(f&quot;files with brightness settings saved {file_with_all_values}&quot;)

nightlight_value=4500
brightness_value=20


def log_error(error_message):
        import logging
        import uuid
        error_file_path=f&quot;/tmp/brightness_control_error_{uuid.uuid4()}&quot;
        file_handler= logging.FileHandler(error_file_path, mode=&quot;w+&quot;, encoding=&quot;utf-8&quot;)
        stderr_handler= logging.StreamHandler()
        logger=logging.getLogger(&quot;logger&quot;)
        logger.addHandler(file_handler)
        logger.addHandler(stderr_handler)
        logger.critical(f&quot;{error_message}, reported to file {error_file_path}&quot;)
        file_handler.close()

def update_init_system(nightlight_value, brightness_value):
	if (len(sys.argv)==1):
		print(&quot;no init system provided (SKIPPING)&quot; )
		return
	elif (sys.argv[1]==&quot;openrc&quot;):
        	with open(f&quot;{working_dir_for_this_script}/{service_file}&quot;, &quot;w+&quot;) as f:
                	f.write(f&quot;&quot;&quot;	#!/sbin/openrc-run 
					gammastep -P -O {nightlight_value} -b {brightness_value}	
				&quot;&quot;&quot;)
	#eventually the code for each must be broken into functions or atleast for for some init systems
	else:
		log_error(&quot;init system not supported&quot;)

def save_settings_persistently(nightlight_value, brightness_value):
	with open(file_with_all_values, &quot;w&quot;) as f:
		settings = {
			&quot;nightlight_value&quot;      :  nightlight_value,
			&quot;brightness_value&quot;      :  brightness_value,
		}
		json.dump(settings, f)

def update_settings(nightlight_value, brightness_value):
	os.system(f&quot;gammastep -P -O {nightlight_value} -b {brightness_value} &amp;&gt; /dev/null &quot;)
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
	with open(file_with_all_values, &quot;r&quot;) as f:
		settings = json.load(f)
		return settings
def main():
	settings= load_settings()
	nightlight_value=settings[&quot;nightlight_value&quot;]
	brightness_value=settings[&quot;brightness_value&quot;]
	master = Tk()
	nightlight_label = tk.Label(master, text=&quot;nightlight (lower is more nightlight)&quot;)
	nightlight_label.pack()
	nightlight = Scale(master, command=update_nightlight, from_=1000, to=25000, length=1000,tickinterval=1500,orient=HORIZONTAL)
	nightlight.set(nightlight_value)
	nightlight.pack()
	brightness_label = tk.Label(master, text=&quot;brightness (lower is darker)&quot;)
	brightness_label.pack()
	brightness = Scale(master, command=update_brightness, from_=10, to=100,length=600, tickinterval=10, orient=HORIZONTAL)
	brightness.set(brightness_value)
	brightness.pack()
	mainloop()

if __name__ == &quot;__main__&quot;:
        main()

#to install tkinter, buld python with the &quot;tk&quot; USE flag
</pre>
