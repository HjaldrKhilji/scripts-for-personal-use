#!/usr/bin/env bash
if [[ $(ps -e | grep -E '.{26}'$1) != "" ]]; then
	echo 1
else
	echo 0
fi
#personalized alternative to "pgrep $1"
