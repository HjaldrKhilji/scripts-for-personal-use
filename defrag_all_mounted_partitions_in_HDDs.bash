#!/usr/bin/bash
base_path="/.Files used by personal scripts/files used by crontab's daily HDD defrag operation"
run_if_date_file_dosent_exist(){
        for dir in /media/HDD_partitions/*; do
                if [[ -d "$dir" ]]; then
                         xfs-fsr $dir;
                fi
        done
	umask 0
        touch "${base_path}/$1" #adding 
        rm -f "${base_path}/$2" #removing previous date
}

check_if_date_exists() {
current_date=$(date "+%A")
if [[ ! -e "${base_path}/${current_date}" ]]; then
        if [[ ! $("/.scripts_for_personal_use/shared_scripts/check_if_process_exist.bash xfs-fsr") ]]; then
                run_if_date_file_dosent_exist "${current_date}" "$(date --date "1 day ago" "+%A")"      
        fi
fi

}
check_if_date_exists
