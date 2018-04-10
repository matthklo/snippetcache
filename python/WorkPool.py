#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function
import random
import Queue
import threading
import time

"""
    TODO: Documentation
"""
class WorkPool ( threading.Thread ):
    def __init__ ( self, threadNum=20 ):
        threading.Thread.__init__( self )
        self.threadNum = threadNum
        self.quit = False
        self.pendingJobQueue = Queue.Queue()
        self.doneJobQueue = Queue.Queue()

    def run ( self ):
        self.workspace = [ None for i in range(self.threadNum) ]

        while self.quit == False:

            joinAnything = False
            fireAnything = False
            available_slot = None

            # Go through each thread slot
            for idx in range(self.threadNum):
                t = self.workspace[idx]

                # Skip empty slot
                if None == t:
                    if None == available_slot:
                        available_slot = idx
                    continue
                
                # Try to join a running work thread.
                t.join(0.0)
                if not t.isAlive():
                    self.doneJobQueue.put(t.callable_obj)
                    self.workspace[idx] = None
                    joinAnything = True

            # Try to fire a pending job
            if None != available_slot:
                try:
                    j = self.pendingJobQueue.get(False)
                    t = threading.Thread(None, j, 'Job-' + str(j.myid))
                    t.callable_obj = j
                    self.workspace[available_slot] = t
                    t.start()
                    fireAnything = True
                except Queue.Empty:
                    pass

            # Sleep while idling
            if (not joinAnything) and (not fireAnything):
                time.sleep(0.1)

        #Quiting
        print('[WorkPool] Work pool is quiting.')

    # Append a job to work pool.
    # 'callable_obj' can be a function, lambda, or a class object which 
    # has implemented the '__call__' method
    def appendJob ( self, callable_obj ):
        self.pendingJobQueue.put(callable_obj)

    # Retrieve the result of a job.
    # Might return None if there is no done job yet.
    def retrieveJob ( self ) :
        try:
            return self.doneJobQueue.get(False)
        except Queue.Empty:
            return None

# ---------------------------------------------------------------

class MyJob:
    def __init__ (self, id, countdown):
        self.cntdwn = countdown
        self.myid = id

    def __call__ (self):
        with glck:
            print("[Job] ID: %s Starts." % str(self.myid))
        while self.cntdwn >= 0:
            with glck:
                print("[Job] ID: %s, CountDown: %d" % (str(self.myid), self.cntdwn))
            self.cntdwn -= 1
            time.sleep(1.0)
        with glck:
            print("[Job] ID: %s Ends." % str(self.myid))

if __name__ == '__main__':

    wp = WorkPool()
    wp.start()

    glck = threading.Lock()

    random.seed()

    for i in range(50):
        j = MyJob(i, random.randint(1,10))
        wp.appendJob(j)

    dj = set()
    while len(dj) < 50:
        r = wp.retrieveJob()
        if None == r:
            time.sleep(0.5)
            continue
        dj.add(r.myid)
    
    print("[Main] All job done. Joining work pool...")
    wp.quit = True
    wp.join()
