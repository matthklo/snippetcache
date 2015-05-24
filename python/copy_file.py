#!/usr/bin/env python

# Required for Python2.6/2.7 to handle Python3 print syntax
from __future__ import print_function

# Comment to the end of line

""" Use string as multi-lines comments
    123
    abc
    """

def mycopy(input_file, output_file):
  try:
    with open(input_file, 'rb') as rf, open(output_file, 'wb') as wf:
      for line in rf:
        # Parameter of print: file: the file descriptor to output to.
        #                     end: the tailing character (default \n)
        print(line, file=wf, end='')
  except IOError as err:
    print ('Failed on opening either input or output file: ' + str(err))

mycopy("foo", "bar")

