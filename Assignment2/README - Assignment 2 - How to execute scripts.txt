This document describes how to run the NS-2 and AWK scripts.
Please note that the scripts do not have error handling for incorrect inputs.

Experiment 1
******************
ns experiment1.tcl [cbrrate] [tcpvar] [cbrstart] [cbrstop] [tcpstart] [tcpstop] [finishsim] [filename]

cbrrate = 1mb, 2mb, .... 10mb
tcpvar = /TCP for Tahoe, /TCP/Reno for Reno, /TCP/Newreno for New Reno, /TCP/Vegas for Vegas TCP variants
cbrstart = start time of CBR flow (e.g. 0.0)
cbrstop = stop time of CBR flow
tcpstart = start time of tcp flow  
tcpstop = stop time of tcp flow
finishsim = stop time of simulation (ensure simulation ends after tcp and cbr flows have ended)
filename = name of trace file with .tr extension

Sample: ns experiment1.tcl 1mb /TCP 0 5 1 4 20 1mbTahoe.tr 

Other details: 
TCP flow N1 to N4 (nodes 0 to 3 in trace files)
CBR flow N2 to N3 (nodes 1 to 2 in trace files)
TCP flow id = 77777777
CBR flow id = 33333333

Experiment 2
***********************
ns experiment2.tcl [cbrrate] [tcpvar1] [tcpvar2] [cbrstart] [cbrstop] [tcpvar1start] [tcpvar1stop] [tcpvar2start] [tcpvar2stop][finishsim] [filename]

cbrrate = 1mb, 2mb, .... 10mb
tcpvar1 = /TCP/Reno for Reno, /TCP/Newreno for New Reno, /TCP/Vegas for Vegas TCP variants
tcpvar2 = /TCP/Reno for Reno, /TCP/Newreno for New Reno, /TCP/Vegas for Vegas TCP variants
cbrstart = start time of CBR flow (e.g. 0.0)
cbrstop = stop time of CBR flow
tcpvar1start = start time of first tcp flow  
tcpvar1stop = stop time of first tcp flow
tcpvar2start = start time of second tcp flow  
tcpvar2stop = stop time of second tcp flow
finishsim = stop time of simulation (ensure simulation ends after tcp and cbr flows have ended)
filename = name of trace file with .tr extension

Sample: ns experiment2.tcl 9mb /TCP/Reno /TCP/Reno 0 5 1 4 1 4 20 9mbRenoReno.tr 

Other details: 
First TCP flow N1 to N4 (nodes 0 to 3 in trace files)
Second TCP flow N5 to N6 (nodes 4 to 5 in trace files)
CBR flow N2 to N3 (nodes 1 to 2 in trace files)
First TCP flow id = 77777777
Second TCP flow id = 55555555
CBR flow id = 33333333

Experiment 3
******************
ns experiment3.tcl [cbrrate] [queuetype] [tcpvar] [sinktype] [cbrstart] [cbrstop] [tcpstart] [tcpstop] [finishsim] [filename]

cbrrate = 1mb, 2mb, .... 10mb
queuetype = DropTail,RED
tcpvar = /TCP/Reno for Reno, /TCP/Sack1 for TCP variants
sinktype = /TCPSink for regular sink, /TCP/Sack1 for SACK enabled sink
cbrstart = start time of CBR flow (e.g. 0.0)
cbrstop = stop time of CBR flow
tcpstart = start time of tcp flow  
tcpstop = stop time of tcp flow
finishsim = stop time of simulation (ensure simulation ends after tcp and cbr flows have ended)
filename = name of trace file with .tr extension

Sample: ns experiment3.tcl 9mb RED /TCP/Reno /TCPSink 2 4 0 5 20 9mbRedReno.tr 

Other details: 
TCP flow N1 to N4 (nodes 0 to 3 in trace files)
CBR flow N5 to N6 (nodes 4 to 5 in trace files)
TCP flow id = 77777777
CBR flow id = 33333333

AWK scripts
************
All three scripts (latency, throughput and packetdrop rates) can be run as follows:

gawk -v from_node=<# of node in trace file> -v to_node=<# of node in tracefile> -v flow_id_value=<# of flow id> -f awkscriptname.awk tracefilename.tr

Plots for graphs:
******************
Plotting was done using matplot lib. This has not been fully automated. 
We execute the scripts, obtain the relevant values and input them manually into the plotting scripts in X and Y axes to obtain the graphs.
We have included relevant graphs along with this README file.


