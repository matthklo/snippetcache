#!/usr/bin/env python

import os

""" usage: os.environ['key']   <-- this will throw KeyError if key can not be found """
print ("HOME= " + os.environ['HOME'])

try:
  print ("HO= " + os.environ['HO'])
except KeyError as e:
  print ("HO: undefined environment variable.")

""" Set a environment variable. Throw TypeError if variable is not a string. """
os.environ['HO'] = '123'

""" Determine if a variable has been defiend """
exists = 'HO' in os.environ
print ("HO defined? " + str(exists))



""" usage: os.environ.get('KEY')    <-- this returns 'None' instead of throw error when key has not defined """
val = os.environ.get("LO")
print ("LO defined? " + str(val))


""" usage: os.getenv("KEY", "default value")   <-- this returns specified default value when key has not defined 
    the default value can be type other than string.
    """
val = os.getenv("LO", 123)
print ("Value of LO: " + str(val))

""" usage: another way to set environment variable. Throw TypeError if variable is not a string. """
os.putenv("LO", "123")


