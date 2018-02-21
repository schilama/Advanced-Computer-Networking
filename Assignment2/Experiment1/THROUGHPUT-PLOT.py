#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:35:02 2017

@author: sruthi
"""

import matplotlib.pyplot as plt
import numpy as np

"""  
CBR = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TahoeLatency = [0.062924, 0.062926, 0.062919, 0.062959,  0.062982, 0.062965, 0.063292, 0.080410, 0.090918, 1.010050]
RenoLatency = [0.062924, 0.062926, 0.062919, 0.062959, 0.062982, 0.062965, 0.063292, 0.080410, 0.094381, 1.010050]
NewrenoLatency = [0.062924, 0.062926, 0.062919, 0.062959, 0.062982, 0.062965, 0.063292, 0.080410, 0.088100, 1.010050]
VegasLatency = [0.062799, 0.062862, 0.062864, 0.062869, 0.062777, 0.062943,  0.063263, 0.070239, 0.086521, 0.955145]
"""
"""
CBR = [ 7, 8, 9, 10]
TahoeLatency = [92.94, 72.83, 40.47, 3.70]
RenoLatency = [92.94, 72.83, 35.01, 3.70]
NewrenoLatency = [92.94, 72.83, 38.40, 3.70]
VegasLatency = [88.02, 70.85, 39.53, 2.58]
"""
"""
CBR = [ 8, 9, 10]
TahoeLatency = [ 0.080410, 0.090918, 1.010050]
RenoLatency = [ 0.080410, 0.094381, 1.010050]
NewrenoLatency = [ 0.080410, 0.088100, 1.010050]
VegasLatency = [ 0.070239, 0.086521, 0.955145]
"""
"""
CBR = np.array([ 8, 9, 10])
TahoeLatency = np.array([ 80410, 90918, 1010050]) #sheet2
RenoLatency = np.array([ 80410, 94381, 1010050]) #sheet1
NewrenoLatency = np.array([ 80410, 88100, 1010050]) #sheet4
VegasLatency = np.array([ 70239,86521, 955145]) #sheet3
"""
#Throughputr with from and to node and flow defined
CBR = [7, 8, 9, 10]
TahoeLatency = [2437.72, 1909.62, 1059.92, 95.56]
RenoLatency = [ 2437.72, 1909.62, 916.69, 95.56]
NewrenoLatency = [ 2437.72, 1909.62, 1005.76, 95.56]
VegasLatency = [ 2222.39, 1788.77, 997.98, 64.69]

print TahoeLatency
plt.title("Average throughput as a function of CBR rate")
plt.xlabel('CBR Rate (Mbps)')
plt.ylabel('Average Throughput (Kbps)')
tahoe, = plt.plot(CBR,TahoeLatency,color='r',label='Tahoe', alpha=1.0, marker = '*', linestyle='-.')
reno, = plt.plot(CBR,RenoLatency,color='y',label='Reno', alpha=0.5, marker = '*' , linestyle='-')
newreno, = plt.plot(CBR,NewrenoLatency,color='g',label='Newreno', alpha=1.0, marker = 's', linestyle=':')
vegas, = plt.plot(CBR,VegasLatency,color='m',label='Vegas', alpha=0.5, marker = '+', linestyle='--')
plt.legend(handles=[tahoe,reno,newreno,vegas])
"""
plt.yticks(np.arange(VegasLatency.min(), Vegaslatency.max(), 100))
plt.grid(axis='y')
"""
#print y

plt.show()