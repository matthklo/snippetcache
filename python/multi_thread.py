#!/usr/bin/env python

import threading, time, sys

# Make MyThread class inherit from threading.Thread
class MyThread(threading.Thread):
  # Note: The __init__ of a class always expect self as the 1st argument.
  def __init__(self, seconds, stepSeconds):
    threading.Thread.__init__(self)
    # Register 'constructor arguments' in the instance object map.
    self.seconds = seconds
    self.stepSeconds = stepSeconds

  # Every member function of a class should take 'self' as the 1st argument.
  # run() is the thread body.
  def run(self):
    secs = 0
    while secs < self.seconds:
      # Note: print() is not thread safe in Python. Use sys.stdout.write(str +'\n') instead.
      msg = "Thread: " + str(self.ident) + " sleep for " + str(self.stepSeconds) + " seconds."
      sys.stdout.write(msg + '\n')
      time.sleep(self.stepSeconds)
      secs += self.stepSeconds
    else:
      msg = "Thread: " + str(self.ident) + " finishes."
      sys.stdout.write(msg + '\n')

def try_join(t):
  if t.isAlive() == False:
    return True
  t.join(0)
  return not t.isAlive()

if __name__ == "__main__" :
  threads = []
  for i in range(10):
    t = MyThread(2+i, 0.2)
    threads.append(t)
    t.start()

  while (True):
    results = map(try_join, threads)
    if all(results):
      break


