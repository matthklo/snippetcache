#!/usr/bin/env python

from __future__ import print_function

import sys, getopt

""" Demo how to get command line argument
    and getopt similar to C getopt() """

def myparser(argv):
  try:
    # The 1st argument of getopt.getopt() should be sys.argv[1:]. Otherwise it won't work.
    opt_pairs, remainings = getopt.getopt(argv, "hi:f", ["abc", "def="])
    # opt_pairs should be a list of tuples. Each tuple contains option to argument pair.
    # remainings should be a list of strings. Indicating the remaining arguments after options were stripped.
    print ("myparser: opt_pairs = " + str(opt_pairs))
    print ("myparser: remainings = " + str(remainings))
  except getopt.GetoptError as e:
    print ("syntax error")
    sys.exit(1)


# This check whether this file is run as the main program or import by other program.
if __name__ == "__main__" :
  print ("argc = " + str(len(sys.argv)))
  print ("argv = " + str(sys.argv))
  myparser(sys.argv[1:])

