1#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:31:33 2017
111111
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

CBR = [ 7, 8, 9, 10]
TahoeLatency = [0.063292, 0.080410, 0.090918, 1.010050]
RenoLatency = [0.063292, 0.080410, 0.094381, 1.010050]
NewrenoLatency = [0.063292, 0.080410, 0.088100, 1.010050]
VegasLatency = [0.063263, 0.070239, 0.086521, 0.955145]

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
print TahoeLatency
plt.title("Latency as a function of CBR rate")
plt.xlabel('CBR Rate (Mbps)')
plt.ylabel('Latency (Seconds)')
tahoe, = plt.plot(CBR,TahoeLatency,color='r',label='Tahoe', alpha=1.0, marker = '*', linestyle='-.')
reno, = plt.plot(CBR,RenoLatency,color='y',label='Reno', alpha=0.5, marker = '*' , linestyle='-')
newreno, = plt.plot(CBR,NewrenoLatency,color='g',label='Newreno', alpha=1.0, marker = 's', linestyle=':')
vegas, = plt.plot(CBR,VegasLatency,color='m',label='Vegas', alpha=0.5, marker = '+', linestyle='--')
plt.legend(handles=[tahoe,reno,newreno,vegas])
plt.yticks(np.arange(VegasLatency.min(), Vegaslatency.max(), 100))
plt.grid(axis='y')
#print y

plt.show()