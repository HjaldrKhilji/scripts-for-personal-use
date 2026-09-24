#!/usr/bin/env bash
path=/tmp/$(uuidgen)/XDG_RUNTIME_DIR
i=0
while [[ -e "$path\_$i" ]] do
	i=$((i+1))
	path="$path\_$i"
done
path=$path\_$i
mkdir -p $path
chmod 700 $path
export XDG_RUNTIME_DIR=$path
#to use this, add this to your /etc/profile file:
# source /.scripts_for_personal_use/init_scripts/make_and_export_XDG_RUNTIME_DIR.bash
