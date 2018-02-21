<h3>Assignment 1 (part 1): Simple Client</h3>
<p>
<b>This project is due at 11:59pm on September 20, 2017. </b>
</p><p>
<h3>Description</h3>
This assignment is intended to familiarize you with writing simple network code.
You will implement a client program which communicates with a server using sockets.
The server will ask your program to solve hundreds of simple mathematical expressions.
If your program successfully solves all of the expressions, then the server will return
a <i>secret flag</i> that is unique for each student. If you receive the <i>secret flag</i>,
then you know that your program has run successfully, and you will receive full credit for
the assignment.
</p><p>
<h3>EdLab</h3>
Code will be tested on EdLab machines. Access information to EdLab will be sent to your 
SPIRE email address. Please email the TA (ksung@cs.umass.edu) if you have trouble logging in.
</p><p>
<h3>Development</h3>
You can write your code in whatever language you choose, as long as your code compiles and runs
on <b>unmodified</b> EdLab Linux machines <b>on the command line</b>. Do not use libraries that are not
installed by default on EdLab machines. Similarly, your code must compile and run on the
command line. You may use IDEs (e.g. Eclipse) during development, but do not turn in your IDE
project without a Makefile. Make sure you code has <b>no dependencies</b> on your IDE.
</p><p>
<h3>Protocol</h3>
The server runs on the machine <i>elsrv2.cs.umass.edu</i> and listens for requests on a TCP socket bound
to port <i>27993</i>. This exercise
has four types of messages: HELLO, STATUS, SOLUTION, and BYE. Each message is an ASCII string
consisting of multiple fields separated by spaces (0x20) and terminated with a line feed (0x0A, \n).
The maximum length of each message is 256 bytes. Messages are case sensitive.
</p><p>
The protocol works as follows. The client initiates the protocol by creating a TCP socket connection
to the server. Once the socket is connected, the client sends a
HELLO message to the server. The format of the HELLO message is:
<pre>cs653fall2017 HELLO [your SPIRE email]\n</pre>
In your program you should replace [your SPIRE email] with your SPIRE email.
You must supply your SPIRE email so the server can look up the appropriate <i>secret flag</i> for you.
The server will reply with a STATUS message. The format of the STATUS message is:
<pre>cs653fall2017 STATUS [a number] [a math operator] [another number]\n</pre>
The three variable fields represent a simple mathematical expression, e.g. "5 + 10". The
server may return plus, minus, multiplication, or division expressions. All numbers will be
between 1 and 1000. Your program
must solve the mathematical expression and return the answer to the server in a SOLUTION
message. The SOLUTION message has the following format:
<pre>cs653fall2017 [the solution]\n</pre>
It is okay for the solution to be negative. In the case of division, round the answer down
to the nearest integer (do not send floating point numbers to the server).
</p><p>
The server will respond to the SOLUTION message with either another STATUS message, or a BYE message.
If the server terminates the connection, that means your solution was incorrect. If the server sends
another STATUS message, your program must solve the expression and return another SOLUTION message.
The server will ask your program to solve hundreds of expressions; the exact number of expressions
is chosen at random. Eventually, the server will return a BYE message. The BYE message has the following
format:
<pre>cs653fall2017 [a 64 byte secret flag] BYE\n</pre>
Once your program has received the BYE message, it can close the connection to the server. If the
server returns "Unknown_Husky_ID" in the BYE message, that means it did not recognize the email that
you supplied in the HELLO message. Otherwise, the 64-byte string is your <i>secret flag</i>: write
this value down, since you need to turn it in along with your code.
</p><p>
<h3>Your client program</h3>
Your client program must execute on the command line using the following command. 
<pre>$ ./client &lt;-p port&gt; &lt;-s&gt; [hostname] [SPIRE email]</pre>
Your program must follow this
command line syntax <b>exactly</b>, i.e. your program must be called <i>client</i> and it must
accept these exact parameters in exactly this order. If you cannot name your program <i>client</i>
(i.e. your program is in Java and you can only generate <i>client.class</i>) then you <b>must</b>
include a script called <i>client</i> in your submission that accepts these parameters and then executes
your actual program. Keep in mind that all of your submissions will be evaluated by grading scripts;
if your program does not conform <b>exactly</b> to the specification then the grading scripts may
fail, which will result in loss of points.
</p><p>
The <i>-p port</i> parameter is optional; it specifies the TCP port that
the server is listening on. If this parameter is not supplied on the command line, assume the port is
27993. The <i>-s</i> flag is optional; if given, the client should use an SSL encrypted socket connection. Your client only needs to support <i>-s</i> if you are trying to get the extra credit points.
The [hostname] parameter is required, and specifies the name of the server (either a DNS name or an IP
address in dotted notation). 
The [SPIRE email]
parameter is required.
</p><p>
Your program should print <b>exactly one line of output</b>: the <i>secret flag</i> from the server's
BYE message. If your program encounters an error, it may print an error message before terminating.
Your program <b>should not write any files to disk</b>, including writing to the <i>secret_flags</i>
file.
</p><p>
<h3>Other Considerations</h3>
You may test your client code with our server as many times as you like. Your client should
conform to the protocol described above, otherwise the server will terminate the connection
silently. Your client program must verify the validity of messages by strictly checking their
format, i.e. the server may send corrupted messages just to try and crash your software.
If a received message is not as expected,
such as an incorrect field or wrong message type, you must assert an error and terminate
your program. You should be strict; if the returned message does not exactly conform to the specification
above, you should assert an error. Remember that network-facing code should be written
defensively.
</p><p>
<h3>Submitting Your Project</h3>
To turn-in your project, you should submit your (thoroughly documented) code along with three other files:
<ul><li>A Makefile that compiles your code (if needed).</li>
<li>A plain-text (no Word or PDF) README file. In this file, you should briefly describe your high-level
approach, any challenges you faced, and an overview of how you tested your code.</li>
<li>A file called <i>secret_flags</i>. This file should contain the <i>secret flag</i> in plain ASCII.</li>
</ul>
Submit your project as a zip file containing these files in the root directory on Moodle. Do not put the files in a subdirectory.
</p><p>
<h3>Grading</h3>
This project is worth 4 points. If your program compiles, and you successfully submit the
<i>secret flag</i>, then you will receive full credit. We will randomly check
student's code to make sure that it works correctly. All student code will be scanned by plagarism
detection software to ensure that students are not copying code from the Internet or each other.
</p><p>
<h3>Extra Credit</h3>
It is possible to earn 1 extra credit point on this assignment. To get the extra credit point, you
must modify your client such that it supports SSL connections. If the <i>-s</i> parameter is given
to your program, it should connect to the server using an encrypted SSL socket and complete the
protocol normally (i.e. HELLO, STATUS, SOLUTION, and BYE). You may assume that the server's SSL port is
27994, unless the port is overridden on the command line using the <i>-p</i> option. The SSL certificate
is self-signed, so you may need to add the certificate as trusted, depending on how you implement the 
client: <a href="cacert.pem">cacert.pem</a>
</p><p>
When you successfully run your SSL-enabled client against the SSL version of the server, you will receive a new secret flag
(that is different from the normal secret flag). You should add this SSL secret
flag in the line after the normal flag in the <i>secret_flags</i> file when you turn in your project. You will only receive the
extra credit point if your code successfully implements the <i>-s</i> option, and you include the
SSL secret flag in the <i>secret_flags</i> file.
</p>
