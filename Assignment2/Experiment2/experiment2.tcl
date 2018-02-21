#Create a simulator object
set ns [new Simulator]

set cbrrate [lindex $argv 0]
set tcpvariant1 [lindex $argv 1]
set tcpvariant2 [lindex $argv 2]
set cbrstart [lindex $argv 3]
set cbrstop [lindex $argv 4]
set tcpvar1start [lindex $argv 5]
set tcpvar1stop [lindex $argv 6]
set tcpvar2start [lindex $argv 7]
set tcpvar2stop [lindex $argv 8]
set finishsim [lindex $argv 9]
set filename [lindex $argv 10]

#Open the trace file
set tf [open $filename w]
$ns trace-all $tf

proc finish {} {
	global ns tf
	$ns flush-trace 
	close $tf
	exit 0
	}

#Create six nodes
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]

#Create links between the nodes
$ns duplex-link $n1 $n2 10Mb 10ms DropTail
$ns duplex-link $n2 $n3 10Mb 10ms DropTail
$ns duplex-link $n2 $n5 10Mb 10ms DropTail
$ns duplex-link $n3 $n4 10Mb 10ms DropTail
$ns duplex-link $n3 $n6 10Mb 10ms DropTail

#Setup a UDP connection
set udp [new Agent/UDP]
$ns attach-agent $n2 $udp
set null [new Agent/Null]
$ns attach-agent $n3 $null
$ns connect $udp $null
$udp set fid_ 33333333

#Setup a CBR over UDP connection
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
$cbr set rate_ $cbrrate
$cbr set random_ false

#Setup first TCP connection
set tcp1 [new Agent$tcpvariant1]
#$tcp set class_ 2
$ns attach-agent $n1 $tcp1
set sink1 [new Agent/TCPSink]
$ns attach-agent $n4 $sink1
$ns connect $tcp1 $sink1
$tcp1 set fid_ 77777777

#Setup FTP over first TCP connection
set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp1 set type_ FTP

#Setup second TCP connection
set tcp2 [new Agent$tcpvariant2]
#$tcp set class_ 2
$ns attach-agent $n5 $tcp2
set sink2 [new Agent/TCPSink]
$ns attach-agent $n6 $sink2
$ns connect $tcp2 $sink2
$tcp2 set fid_ 55555555

#Setup FTP over second TCP connection
set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp2
$ftp2 set type_ FTP


#Schedule events for the CBR and TCP agents
$ns at $cbrstart "$cbr start"
$ns at $tcpvar1start "$ftp1 start"
$ns at $tcpvar1stop "$ftp1 stop"
$ns at $tcpvar2start "$ftp2 start"
$ns at $tcpvar2stop "$ftp2 stop"
$ns at $cbrstop "$cbr stop"
$ns at $finishsim "finish"

#Run the simulation
$ns run
