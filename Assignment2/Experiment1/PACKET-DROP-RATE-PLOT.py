#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:00:20 2017

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
TahoeLatency = [ 0.000000, 0.022500, 0.194175]
RenoLatency = [ 0.000000, 0.031700, 0.178218]
NewrenoLatency = [ 0.000000, 0.026738, 0.186275]
VegasLatency = [ 0.000000, 0.000000, 0.236842]
"""
"""
CBR = np.array([ 8, 9, 10])
TahoeLatency = np.array([ 80410, 90918, 1010050]) #sheet2
RenoLatency = np.array([ 80410, 94381, 1010050]) #sheet1
NewrenoLatency = np.array([ 80410, 88100, 1010050]) #sheet4
VegasLatency = np.array([ 70239,86521, 955145]) #sheet3
"""
#Packetdropr 
CBR = [7, 8, 9, 10]
TahoeLatency = [  0.0, 0.000000, 2.9396, 2.8001]
RenoLatency = [  0.0, 0.000000, 3.6174, 2.5201]
NewrenoLatency = [ 0.0, 0.000000, 3.3298, 2.6601]
VegasLatency = [0.0, 0.000000, 0.000000, 2.5096]

print TahoeLatency
plt.title("Packet drop rate as a function of CBR rate")
plt.xlabel('CBR Rate (Mbps)')
plt.ylabel('Packet drop rate\n (Number of packets dropped per second)')
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