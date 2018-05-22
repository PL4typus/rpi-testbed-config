#!/usr/bin/env python

#This python script is intended to be ;ore error friendly and easier to use than the bash script

import subprocess
import sys
import os

if (len(sys.argv) != 3):
  print("Usage: python3.5 upload.py </path/to/exec> </path/to/rpi_addr/file>")
  sys.exit(2)
if ( not os.path.isfile(sys.argv[1]) ):
  print("Path to executable is not correct")
  sys.exit(3)
if ( not os.path.isfile(sys.argv[2]) ):
  print("Path to address file is not correct")
  sys.exit(3)



with open(sys.argv[2],'r') as rpi_file:
    try:
      for addr in rpi_file:
        p = subprocess.Popen(["scp", sys.argv[1], "pi@"+addr+":/home/pi"])
        sts = os.waitpid(p.pid, 0)
        p = subprocess.Popen(["ssh", "pi@"+addr,"'/home/pi/"+sys.argv[1]+"'"])
        sts = os.waitpid(p.pid, 0)

    except:
      print("Unexpected error")
      sys.exit(1)





