BEGIN {

numofacks = 0.0;
RTT = 0.0;
#Assumoing seq num of any packet is less than 8000 for entire simulation 
for (i=0; i<=8000; i++)
{start[i] = 1000.0}
#Again start time for any packet will be less than 1000 (current similation is 5 seconds)
highest_seq_num = 0
new_seq_no = 0
#Assuming run time less than 20 seconds, sampling every 0.5 seconds
for (i=0;i<20;i++)
{sampledtime[i] = i*0.5}
j = 0
lastpackettime = 0 			
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


if (flow_id==flow_id_value && (seq_no > highest_seq_num))
{highest_seq_no = seq_no} 

if (from==from_node && action == "+" && flow_id==flow_id_value && time>sampledtime[j])
{
#Storing highest sequence number in transit at a particular time. Latency will be computed up to sequence number at stored time
seqnumstore[j]=highest_seq_no
j++
} 

if (from==from_node && action == "+" && flow_id==flow_id_value) # && src==0.0 && dst==3.0)&& flow_id==77777777 && src==0.0 && dest==3.0)
{
#printf("Test");
if (time < start[seq_no])
{
#printf("start init");
start[seq_no] = time;
#Only consider start time of first packet, not re-transmitted packets
}}
if ( to==from_node && action == "r" && flow_id==flow_id_value) #&& from==1 && action == "r" && flow_id==77777777 && src==3.0 && dst==0.0)
{
stop[seq_no] = time;
#Stop time is the time when an ack is received  
numofacks = numofacks + 1
#print ("Numofacks:%f Seq_no: %d",numofacks,highest_seq_no); 
#numofacks is the same as sequence number in ns trace file
}
}

END {
#Adding last seq num value
seqnumstore[j] = highest_seq_no
j++

for ( i = 0; i <= highest_seq_no; i++ ) {
if (stop[i] != 0)
{
RTT = RTT + stop[i] - start[i]
new_seq_no = new_seq_no + 1
}
#printf("RTT:%f Start:%f Stop:%f",RTT,start[i],stop[i]);
}
print ("Numofacks:%d Seq_no:%d New_seq_no:%d",numofacks,highest_seq_no, new_seq_no);
printf("RTT:%f \nNumber of acks:%f\n", RTT, numofacks);
latency = RTT/(new_seq_no);
printf("Average latency: %f\n", latency);


for (i=0;i<j;i++)
{
#printf("\n\n")
#printf("Sampledtime:%f Seqno:%d \n", sampledtime[i],seqnumstore[i])
new_seq_no = 0
highest_seq_no = seqnumstore[i]
RTT = 0
for ( k = 0; k <= highest_seq_no; k++ ) {
if (stop[k] != 0)
{
RTT = RTT + stop[k] - start[k]
new_seq_no = new_seq_no + 1
}
#printf("RTT:%f Start:%f Stop:%f",RTT,start[i],stop[i]);
}
#print ("Seq_no:%d Num of non duplicate acks:%d\n",highest_seq_no, new_seq_no);
#printf("RTT:%f Num of non duplicate acks:%d\n", RTT, new_seq_no);
latency = RTT/(new_seq_no);
printf("Sampled time:%f Average latency: %f\n",sampledtime[i], latency);
}

}
