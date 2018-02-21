High Level Approach:
***********************
The requirement is fairly straightforward: build a client program that establishes a TCP connection to the server and computes certain mathematical expressions 
to obtain a secret flag.

The basic client server communication was achieved with the help of inbuilt functions in python socket library. Since the client program needed to execute on a 
linux machine with exactly the following parameters: 

./client <-p port> <-s> [hostname] [SPIRE email]

If statements were used to parse different combinations of input. Checks were also added to ensure the port field is a number (as opposed to 'abc' for example).

A while loop was used to compute multiple mathematical operations and provisions were made to end the while loop when a BYE message is received. Also, the format of 
each message from the server was verified for compliance. 

Support for SSL has also been added.

Challenges:
***********************
I used the eval function to compute the result of the mathematical operation.
While formatting the solution message, I had forgotton to convert the numerical result into a string and this prevented me from obtaining the secret flag.
After converting the result to string format, the program executed successfully and the secret flag was obtained.

Testing:
***********************
I used a lot of print statements to identify where the execution was getting stuck at in the beginning.
Once I got the code working, I tested with various combinations of input to validate the program.

elnux3 ~) > ./client elsrv2.cs.umass.edu schilamakuri@umass.edu
c83f815664b4f4062a74da930e9e16cff2f1fe68354a6880e9c9852969daa6ca

elnux3 ~) > ./client elsrv2.cs.umass.edu schilamakuri@umass.edu
c83f815664b4f4062a74da930e9e16cff2f1fe68354a6880e9c9852969daa6ca

elnux3 ~) > ./client -p 27993 elsrv2.cs.umass.edu schilamakuri@umass.edu
c83f815664b4f4062a74da930e9e16cff2f1fe68354a6880e9c9852969daa6ca

elnux3 ~) > ./client -p 27993 -s  elsrv2.cs.umass.edu schilamakuri@umass.edu
Could not create secure socket, defaulting to using socket without SSL
Invalid server response format. Terminating the program

elnux3 ~) > ./client -s  elsrv2.cs.umass.edu schilamakuri@umass.edu
9b083e40c080b11bc7f0f215bdbf45296e0b5e61081d2f591fc656f6730f6723

elnux3 ~) > ./client -p 243 -s  elsrv2.cs.umass.edu schilamakuri@umass.edu
Unable to connect to server

elnux3 ~) > ./client -p 27993 -s  someserver.cs.umass.edu schilamakuri@umass.edu
Could not resolve host. Please input a valid DNS name or host IP

elnux3 ~) > ./client -p 27993 -s  elsrv2.cs.umass.edu someemail@umass.edu
Unknown_Husky_ID



