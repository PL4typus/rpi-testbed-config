#!/bin/bash

# Script that will send your program to all raspberry pies and execute it.
# Need to specify exec name as argument
# 
# Author: Pierre-Louis Palant for CRoCS

if [[ $# -ne 2 ]]; then
  echo "Usage: upload.sh /path/to/exec/file /path/to/rpi/addr/file"
  exit 1
fi


exec_file=$1

rpi_config_file=$2

for rpi in $(cat "$rpi_config_file")
do
    scp "$exec_file" pi@"$rpi":/home/pi/
    ssh pi@"$rpi" "./$exec_file"
done

exit 0
