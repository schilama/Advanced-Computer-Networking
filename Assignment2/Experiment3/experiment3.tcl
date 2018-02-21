#Create a simulator object
set ns [new Simulator]

set cbrrate [lindex $argv 0]
set queuetype [lindex $argv 1]
set tcpvariant [lindex $argv 2]
set sinktype [lindex $argv 3]
set cbrstart [lindex $argv 4]
set cbrstop [lindex $argv 5]
set tcpstart [lindex $argv 6]
set tcpstop [lindex $argv 7]
set finishsim [lindex $argv 8]
set filename [lindex $argv 9]

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
$ns duplex-link $n2 $n3 10Mb 10ms $queuetype
$ns duplex-link $n2 $n5 10Mb 10ms DropTail
$ns duplex-link $n3 $n4 10Mb 10ms DropTail
$ns duplex-link $n3 $n6 10Mb 10ms DropTail

#Setup a UDP connection
set udp [new Agent/UDP]
$ns attach-agent $n5 $udp
set null [new Agent/Null]
$ns attach-agent $n6 $null
$ns connect $udp $null
$udp set fid_ 33333333

#Setup a CBR over UDP connection
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
$cbr set rate_ $cbrrate
$cbr set random_ false

#Setup a TCP connection
set tcp [new Agent$tcpvariant]
#$tcp set class_ 2
$ns attach-agent $n1 $tcp
set sink [new Agent$sinktype]
$ns attach-agent $n4 $sink
$ns connect $tcp $sink
$tcp set fid_ 77777777

#Setup a FTP over TCP connection
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

#Schedule events for the CBR and TCP agents
$ns at $cbrstart "$cbr start"
$ns at $tcpstart "$ftp start"
$ns at $tcpstop "$ftp stop"
$ns at $cbrstop "$cbr stop"
$ns at $finishsim "finish"

#Run the simulation
$ns run
