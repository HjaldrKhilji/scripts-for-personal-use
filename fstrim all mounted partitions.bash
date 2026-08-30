#!/usr/bin/bash
base_path="/mnt/heavy_working_files/Files used by personal scripts/files used by crontab's daily fstrim operation"
run_if_date_file_dosent_exist(){
	/sbin/fstrim --all
	umask 0
	touch "${base_path}/$1" #removing 
	rm -f "${base_path}/$2" #removing previous date
}
check_if_date_exists() {
current_date=$(date "+%A")
if [[ ! -e "${base_path}/${current_date}" ]]; then
	run_if_date_file_dosent_exist "${current_date}" "$(date --date "1 day ago" "+%A")"	
fi
}
check_if_date_exists
#file should have execute and read permissions only for all users
