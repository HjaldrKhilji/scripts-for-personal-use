#!/usr/bin/env python
#example on how to run for openrc:
#sudo python init_brightness_service.py openrc "/.Files used by personal scripts/helper_scripts/brightness_scripts/BRIGHTNESS_service_command"  "/.Files used by personal scripts/all_persistant_values.json"

import os
import sys
supported_init_systems= {
"openrc"
}
init_system_command_prefix= {
"openrc" : "rc-update add "
}
init_system_command_postfix= { 
"openrc" : " default"
}
script_based_init_systems={
"openrc"
}

def log_error(error_message):
	import logging
	import uuid
	error_file_path=f"/tmp/init_service_error_{uuid.uuid4()}"
	file_handler= logging.FileHandler(error_file_path, mode="w+", encoding="utf-8")
	stderr_handler= logging.StreamHandler()
	logger=logging.getLogger("logger")
	logger.addHandler(file_handler)
	logger.addHandler(stderr_handler)
	logger.critical(f"{error_message}, reported to file {error_file_path}")
	file_handler.close()

def construct_command(init_system_name, service_path):
	return f"{init_system_command_prefix[init_system_name]} '{service_path}' {init_system_command_postfix[init_system_name]}"

def change_perms_to_appropriate(service_path, settings_path):
	os.system(f"chmod 777 '{service_path}' '{settings_path}'")
	print("changed permissions successfully for all respective files")
def main():
	if (len(sys.argv)==1):
		log_error("zero arguments passed (guaranteed human error)")
		return
	init_system_name=sys.argv[1].lower();
	if(len(sys.argv)==4):
		service_path=sys.argv[2];
		settings_path=sys.argv[3];
		if({init_system_name}.issubset(supported_init_systems)):
			change_perms_to_appropriate(service_path, settings_path)
			os.system(construct_command(init_system_name,service_path))
	else:
		if({init_system_name}.issubset(script_based_init_systems)):
			log_error("Missing arguments")
		else:
			log_error("init system not supported")#if init systems other than those which rely on external scripts were supported (like openrc) then this section would have also contained a if(support_init_systems.issubset(init_system_command_prefix)) and then a match statement to run code for that specific init system 
			#eventually this whole thing must be broken into various functions
if __name__ == "__main__":
	main()
