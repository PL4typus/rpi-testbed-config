# rpi-testbed-config
This repository contains upload.py, a python3.5 script to send and run an executable file to a list of raspberry pi

## Usage:
    python3.5 upload.py /path/to/exec/file /path/to/rpi/addr/list

It will transfer the file to the /home/pi/bin directory as a.out, using ssh and scp.
It is better to have ssh keys distributed to the raspberry so that no password input is required.

The killscript.sh script is pretty straightforward, it was the easiest solution to kill the previous program. It should be located on the raspberry pi. In implementation it was in /home/pi/bin/ .


