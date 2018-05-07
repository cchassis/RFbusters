#!/usr/bin/env python
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import psutil,os, time 
from threading import Thread
import sys


class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:

            sys.stdout.write( "\r CPU USAGE : %d %% MEM USAGE : %s %%" % (round(psutil.cpu_percent(),1),str(psutil.virtual_memory().percent)) )
            sys.stdout.flush()
            time.sleep(1)
            #sys.stdout.write('\r')
            #print ('\r %r' % )
            #time.sleep(1)
            
pass 
class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        print("hello world")

        np.random.seed(19680801)
        data = np.random.randn(2, 100)

        fig, axs = plt.subplots(2, 2, figsize=(5, 5))
        axs[0, 0].hist(data[0])
        axs[1, 0].scatter(data[0], data[1])
        axs[0, 1].plot(data[0], data[1])
        axs[1, 1].hist2d(data[0], data[1])

        plt.show()



myClassA()
myClassB()
while True:
    pass
