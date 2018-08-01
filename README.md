# rpi-testbed-config
This repository contains:

* *upload.py*, a python3.5 script to send and run an executable file to a list of raspberry pi
* A sample *Makefile* to simplify cross compilation
* An *example bluetooth code* to demonstrate the use of the Makefile (**WIP**)
* *Ansible playbook* to automate installation and update of dependencies on the RPI.



## Python script usage:
    python3.5 upload.py /path/to/exec/file /path/to/rpi/addr/list

It will transfer the file to the /home/pi/bin directory as a.out, using ssh and scp.
It is better to have ssh keys distributed to the raspberry so that no password input is required.

The killscript.sh script is pretty straightforward, it was the easiest solution to kill the previous program. It should be located on the raspberry pi. In implementation it was in /home/pi/bin/ .


## Makefile usage:
    make
Simple as that. You need to be in the src directory and to set up a few things in the file first.

## Ansible playbook usage:

You have 3 different playbooks there. 

###The ansible role is for generating a ssh config file to be able to use hostnames with ssh (i.e. ssh berry17 instead of ssh pi@IPADDR).

Please refer to the relevant documentation to use it. 

###install.yml configures a number of parameters: ssh, dependencies, etc.

    ansible-playbook install.yml -i hosts 

This will run aptitude update and safe-upgrade on all RPIs in the hosts file, as well as installing dependencies and the cloning/compiling/installing Intel IoT library from source. 

This will also generate and distribute config files for ssh as well as privatekeys

### wifi_setup

    ansible-playbook wifi_setup.yml -i hosts

This will configure the wifi on all raspberries.


Ansible playbooks are supposed to be idempotent, giving the same output regardless of the number of times they are run. They are written in YAML so the syntax is pretty straightforward and the documentation is very complete.

As you can see the playbook is using a hosts file. To use the playbook, the hosts file needs to be filled with the IP addresses of the RPI, and some other options. It is mandatory to share ssh keys between the server and the hosts in order to simplify connections. The hosts can be organized in groups, please refer to the documentation to use them.
