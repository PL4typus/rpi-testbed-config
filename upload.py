#!/usr/bin/env python

import subprocess
import sys
import os
import threading
from threading import Thread
class Uploader(Thread):

  def __init__(self, addr):
    Thread.__init__(self)
    self.addr = addr

  def run(self):
    print("Terminating previous program... "+self.addr)
    # Kill the previous program using awk magic (script should be on raspberry)
    p = subprocess.Popen(["ssh", "pi@"+self.addr.rstrip(),"'/home/pi/bin/killscript.sh'"])
    sts = os.waitpid(p.pid, 0)
    # Transfer the binary and rename as a.out
    print("Transfering the new executable as a.out..."+self.addr)
    p = subprocess.Popen(["scp", sys.argv[1], "pi@"+self.addr.rstrip()+":/home/pi/bin/a.out"])
    sts = os.waitpid(p.pid, 0)
    # Execute the binary in the bqckground
    print("Running the new executable as a.out..."+self.addr)
    p = subprocess.Popen(["ssh", "pi@"+self.addr.rstrip(),"'/home/pi/bin/a.out'"])
    #sts = os.waitpid(p.pid, 0)
    #Removed becaues otherwise script waits for termination of a.out


if (len(sys.argv) != 3):
  print("Usage: python3.5 upload.py </path/to/exec> </path/to/rpi_addr/file>")
  sys.exit(2)
if ( not os.path.isfile(sys.argv[1]) ):
  print("Path to executable is not correct")
  sys.exit(3)
if ( not os.path.isfile(sys.argv[2]) ):
  print("Path to address file is not correct")
  sys.exit(3)

uploaders = dict()

# Reading the list of addresses and running the threads.
with open(sys.argv[2],'r') as rpi_file:
  try:
    for addr in rpi_file:
      uploaders[addr] = Uploader(addr)
      uploaders[addr].start()
    t=threading.main_thread()
    t.join()
  except Exception as e:
    print("Unexpected error: "+str(e))
sys.exit(1)





