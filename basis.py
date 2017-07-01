from math import *
import random

def logic_f(x, a = 0.5):
    return 1/(1-exp(-x*a))

def logic_f__(x, a = 0.5):
    return a*logic_f(x,a)*(1-logic_f(x,a))

import time

class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))