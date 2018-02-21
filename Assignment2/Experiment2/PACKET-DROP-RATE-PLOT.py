#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:00:20 2017

@author: sruthi
"""

import matplotlib.pyplot as plt
import numpy as np

#Throughputr with from and to node and flow define
CBR = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NewrenoLatency = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 2.3120, 3.6007, 4.5685]
RenoLatency = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,1.6675, 5.9857, 2.3750]

plt.title("NewReno vs Reno\nPacket drop rate as a function of CBR rate")
plt.xlabel('CBR Rate (Mbps)')
plt.ylabel('Packet drop rate \n(Number of packets dropped per second)')

newreno, = plt.plot(CBR,NewrenoLatency,color='b',label='Newreno', alpha=1.0, marker = 's', linestyle=':')
reno, = plt.plot(CBR,RenoLatency,color='g',label='Reno', alpha=1.0, marker = '*' , linestyle='-')

plt.legend(handles=[newreno,reno])
plt.show()

#Second graph

NewRenoLatency = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.6614, 2.4273, 2.7942]
VegasLatency = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.6560, 3.6197, 0.0000]

plt.title("NewReno vs Vegas\nPacket drop rate as a function of CBR rate")
plt.xlabel('CBR Rate (Mbps)')
plt.ylabel('Packet drop rate \n(Number of packets dropped per second)')

newreno, = plt.plot(CBR,NewRenoLatency,color='r',label='Newreno', alpha=1.0, marker = '*', linestyle='-.')
vegas, = plt.plot(CBR,VegasLatency,color='m',label='Vegas', alpha=1.0, marker = '+', linestyle='--')

plt.legend(handles=[newreno,vegas])
plt.show()