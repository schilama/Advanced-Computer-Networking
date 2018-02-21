#!/usr/bin/env python 

from scapy.all import *
import socket
import sys

def main(argv):

	try:
		hostname = argv[1]
	except:
		print "Hostname is a required parameter. Please execute the program again and specify the hostname."
		sys.exit

	#Send DNS Query to elsrv2.cs.umass.edu on port 5300 and gather the response
	response = sr(IP(dst="elsrv2.cs.umass.edu")/UDP(dport=5300)/DNS(rd=1,qd=DNSQR(qname=hostname)), verbose=0, multi=1, timeout=3)
	
	resolvediplist = []

	#As per Hold-On if DNS injection were to occur, we should expect to see the injected response first
	for i in range(len(response[0])):
   		ip = response[0][IP][i][1][DNS].an.rdata
   		resolvediplist.append(ip)
	
	#So resolve IP of hostname to the one in the last received DNS response
	if len(response[0]) == 1:
		print "No packets were injected. Resolved IP is:",ip
	else:
		print "Injected response:",resolvediplist[0]
		print "Real response:",ip

if __name__ == "__main__":
    main(sys.argv)