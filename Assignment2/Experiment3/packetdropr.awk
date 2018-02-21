BEGIN {

# Initialization. Set two variables. fsDrops: packets drop. numFs: packets sent

fsDrops = 0;

numFs = 0;

startTime = 400;

stopTime = 0;

}

{

action = $1;

time = $2;

from = $3;

to = $4;

type = $5;

pktsize = $6;

flow_id = $8;

src = $9;

dst = $10;

seq_no = $11;

packet_id = $12;


# Store start time
if (from == from_node) {
     if (time < startTime) {
            startTime = time
     }
}


# Update total received packets' size and store packets arrival time
if (action == "r" && to == to_node) {
   if (time > stopTime) {
            stopTime = time
      }
}

if (from == from_node && to == "1" && action=="+")

numFs++;

if (flow_id==flow_id_value && action == "d")

fsDrops++;

}

END {

printf("StartTime = %.4f StopTime = %.4f RunTime = %.4f\n", startTime, stopTime, stopTime - startTime);

printf("number of packets sent:%d lost:%d\n", numFs, fsDrops);

printf("Packet Drop Rate = %.4f\n", fsDrops/(stopTime - startTime));

}
