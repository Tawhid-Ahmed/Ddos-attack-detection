# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:52:08 2023

@author: tawhi
"""
import sys
import timeit
import time
import numpy as np
np.random.seed(42)
import pandas as pd
from pandas import HDFStore
start = timeit.default_timer()
def fun(): 
    time.sleep(72)
fun()
# hdf = pd.read_hdf('E:/Study/MSC-Octobar 2022/Cloud security/clour security project/lucid-ddos-master/sample-dataset/10t-10n-10n-dataset-train.hdf5')
# hdf.head()
stop = timeit.default_timer()
total_time = stop - start

# output running time in a nice format.
mins, secs = divmod(total_time, 60)
hours, mins = divmod(mins, 60)

sys.stdout.write("Total running time: %d:%d:%d.\n" % (hours, mins, secs))