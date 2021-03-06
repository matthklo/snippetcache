#!/usr/bin/env python

import subprocess
import os

"""
   Usage: subprocess.call([ argv0, argv1, argv2 ,... ], stdin=None, stdout=None, stderr=None, shell=False)
   Run the specified command. Wait for command to complete, then return the returncode attribute.

   Valid values for stdin,stdout,stderr:
      subprocess.PIPE
      file descriptor (integer)
      file object
      None (no redirection)

   Extra valid value for stderr:
      subprocess.STDOUT (merged to stdout)
"""

rc = subprocess.call(['ls', '-l'])
print ("Return Code: " + str(rc))


"""
   When shell==True, the 1st argument should be a string.
   On Unix, when shell==True, Python use /bin/sh as default shell executable.
   If other shell executable is desired, it can be specified by 'executable' argument.
"""

rc = subprocess.call("echo ${SHELL}", executable="/bin/bash", shell=True)
print ("Return Code: " + str(rc))


"""
   Usage: subprocess.check_call([ argv0, argv1, argv2 ,... ], stdin=None, stdout=None, stderr=None, shell=False)
   Run the specified command. Wait for command to complte. Throws subprocess.CalledProcessError if return code is not 0.
"""

try:
  rc = subprocess.check_call(['ls', 'non-existed'])
except subprocess.CalledProcessError as e:
  print("check_call throws, return code = " + str(e.returncode))



"""
   Usage: subprocess.check_output([ argv0, argv1, argv2 ,... ], stdin=None, stderr=None, shell=False, universal_newlines=False)
   Run the specified command. Wait for command to complete. Returns its output as a byte string.
   Throws subprocess.CalledProcessError if return code is not 0. In such case the output before throw
   can be found in the 'output' attribute of subprocess.CalledProcessError.
"""

try:
  output = subprocess.check_output(['ls', 'non-existed'], stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
  print("check_output throws, return code = " + str(e.returncode) + ", output = " + e.output)


"""
   All of above commands are implemented by subprocess.Popen()
   It is also the most flexible way to create and work with sub-processes.
"""

my_env = os.environ.copy()
my_env['MY_CUSTOM_ENVVAR'] = 'SOME_VALUE'
# Demo to run specified target command at given current working dir
# along with the custom environment setting.
p = subprocess.Popen(['/path/to/target_cmd', 'args1', 'args2'],
  cwd='/working/dir/to/run/target_cmd', env=my_env)
# The above sub process starts as async, to make sure it has done, 
# the main process should call wait()
rc = p.wait()

