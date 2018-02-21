#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:35:02 2017

@author: sruthi
"""

import matplotlib.pyplot as plt
import numpy as np

#Throughputr with from and to node and flow define
CBR = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NewrenoLatency = [2438.81, 2437.22, 2435.14, 2436.10, 2307.64, 1879.73, 1560.88, 997.62, 708.21, 169.52]
RenoLatency = [2431.24, 2431.06, 2431.21, 2429.18, 2300.65, 1872.78, 1548.56, 996.21, 374.92, 65.14]

plt.title("NewReno vs Reno\nAverage throughput as a function of CBR rate")
plt.xlabel('CBR Rate (Mbps)')
plt.ylabel('Average Throughput (Kbps)')

newreno, = plt.plot(CBR,NewrenoLatency,color='b',label='Newreno', alpha=1.0, marker = 's', linestyle=':')
reno, = plt.plot(CBR,RenoLatency,color='g',label='Reno', alpha=1.0, marker = '*' , linestyle='-')

plt.legend(handles=[newreno,reno])
plt.show()

#Second graph

NewRenoLatency = [2436.09, 2434.01, 2434.23, 2435.98, 2368.21, 2103.79, 1923.56, 1397.85, 838.21, 65.14]
VegasLatency = [2228.09, 2228.09, 2227.16, 2221.04, 2128.39, 1580.03, 914.83, 564.19, 236.93, 387.61]

plt.title("NewReno vs Vegas\nAverage throughput as a function of CBR rate")
plt.xlabel('CBR Rate (Mbps)')
plt.ylabel('Average Throughput (Kbps)')

newreno, = plt.plot(CBR,NewRenoLatency,color='r',label='Newreno', alpha=1.0, marker = '*', linestyle='-.')
vegas, = plt.plot(CBR,VegasLatency,color='m',label='Vegas', alpha=1.0, marker = '+', linestyle='--')

plt.legend(handles=[newreno,vegas])
plt.show()
