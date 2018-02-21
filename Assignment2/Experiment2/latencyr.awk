BEGIN {

highest_sequence_no = 0;

for( i=0; i<2000; i++)
{
  start_time[i] = 400;
}
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

if (from == from_node)
{
  if ( seq_no > highest_seq_no )

  highest_seq_no = seq_no;
}

if (from==from_node && to==1 && action=="+")
numFs++;

11
if (flow_id==flow_id_value && action == "d")

fsDrops++;


if ( time < start_time[seq_no] && from == from_node)

start_time[seq_no] = time;

if ( action == "r" && to == from_node ) {

end_time[seq_no] = time;

}

}

END {

total_packet_duration = 0;

printf("Highest Sequence Number = %d", highest_seq_no);

for ( seq_no = 0; seq_no <= highest_seq_no; seq_no++ ) {

start = start_time[seq_no];

end = end_time[seq_no];

packet_duration = end - start;

if(start < end)
{
  #printf("%f %f\n", start_time[seq_no], packet_duration);
  total_packet_duration += packet_duration;
}
}
printf("average latency = %.4f\n", total_packet_duration/(numFs-fsDrops));
}
                 
