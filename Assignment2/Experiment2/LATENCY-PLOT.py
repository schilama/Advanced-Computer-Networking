1#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:31:33 2017
111111
@author: sruthi
"""
import matplotlib.pyplot as plt
import numpy as np

#Throughputr with from and to node and flow define
CBR = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NewrenoLatency = [0.0633, 0.0633, 0.0633, 0.0633, 0.0668, 0.0818, 0.0984, 0.0747, 0.0787, 0.2501]
RenoLatency = [0.0634, 0.0634, 0.0634, 0.0634, 0.0670, 0.0821, 0.0988, 0.0776, 0.1307, 1.1280]

plt.title("NewReno vs Reno\nLatency as a function of CBR rate")
plt.xlabel('CBR Rate (Mbps)')
plt.ylabel('Latency (Seconds)')

newreno, = plt.plot(CBR,NewrenoLatency,color='b',label='Newreno', alpha=1.0, marker = 's', linestyle=':')
reno, = plt.plot(CBR,RenoLatency,color='g',label='Reno', alpha=1.0, marker = '*' , linestyle='-')

plt.legend(handles=[newreno,reno])
plt.show()

#Second graph

NewRenoLatency = [0.0633, 0.0633, 0.0632, 0.0633, 0.0654, 0.0734, 0.0802, 0.0804, 0.0814, 1.1360]
VegasLatency = [0.0632, 0.0632, 0.0632, 0.0632, 0.0655, 0.0742, 0.0810, 0.0840, 0.1261, 0.0998]

plt.title("NewReno vs Vegas\nLatency as a function of CBR rate")
plt.xlabel('CBR Rate (Mbps)')
plt.ylabel('Latency (Seconds)')

newreno, = plt.plot(CBR,NewRenoLatency,color='r',label='Newreno', alpha=1.0, marker = '*', linestyle='-.')
vegas, = plt.plot(CBR,VegasLatency,color='m',label='Vegas', alpha=1.0, marker = '+', linestyle='--')

plt.legend(handles=[newreno,vegas])
plt.show()