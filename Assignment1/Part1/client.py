#!/usr/bin/env python

import sys
import socket
import ssl

def main(inputlist):
    #print inputlist
    #print "hey this program works!"

    if len(inputlist) == 6:
    # ./client -p port -s hostname spire_email
        try:
            portnum = int(inputlist[2])
        except:
            print "Please execute the program again with a valid port number"
            return
        SSLset = 1
        hostname = inputlist[4]
        spire_email = inputlist[5]

    elif len(inputlist) == 5:
        # ./client -p portnum hostname spire_email
        try:
            portnum = int(inputlist[2])
        except:
            print "Please execute the program again with a valid port number"
            return
        SSLset = 0
        hostname = inputlist[3]
        spire_email = inputlist[4]

    elif len(inputlist) == 4:
        # ./client -s hostname spire_email
        portnum =  27994
        SSLset = 1
        hostname = inputlist[2]
        spire_email = inputlist[3]

    elif len(inputlist) == 3:
        # ./client hostname spire_email
        portnum = 27993
        SSLset = 0
        hostname = inputlist[1]
        spire_email = inputlist[2]

    else:
        # There are insufficient arguments, prompt for execution with proper inputs
        print "Please execute the program again with syntax: ./client <-p port> <-s> hostname spire_email"
        return

    #print portnum
    #print SSLset
    #print hostname
    #print spire_email

    try:
        #creating a socket
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print "Yay the socket is created"
    except:
        print "Socket creation failed"
        return
    try:
        #resolving hostname
        serverip = socket.gethostbyname(hostname)
        #print serverip
    except:
        print "Could not resolve host. Please input a valid DNS name or host IP"
        return
    try:
        #connecting to the server
        mysocket.connect((serverip,portnum))
        #print "Socket is successfully connected to %s" %serverip
    except:
        print "Unable to connect to server"
        return

    if (SSLset):
        #SSL support
        try:
            mysocket = ssl.wrap_socket(mysocket, cert_reqs = ssl.CERT_REQUIRED, ca_certs = "cacert.pem")
            #print "Secure socket created"
        except:
            print "Could not create secure socket, defaulting to using socket without SSL"

    #Formatting the hello message
    #HELLO = "cs653fall2017 HELLO schilamakuri@umass.edu\n"
    HELLO = "cs653fall2017 HELLO " + spire_email + "\n"

    #Sending a hello message
    mysocket.sendall(HELLO)

    loopcondition = True

    while (loopcondition):
        #Receiving status message from server
        serverresponse = mysocket.recv(256)
        #print serverresponse
        mylist = serverresponse.split()
        #print mylist
        if len(mylist) == 5:
            #potential STATUS message, format must be cs653fall2017 STATUS [a number] [a math operator] [another number]\n
            if (mylist[0] == 'cs653fall2017') and (mylist[1] == 'STATUS') and (mylist[3] == '+' or '-' or '*' or '/'):
                #verify if mylist[2] and mylist[4] are numbers between 1 and 1000
                #print "Server returned a status message"
                try:
                    #print int(mylist[2])
                    #print int(mylist[4])
                    if (1 <= int(mylist[2]) <= 1000) and (1 <= int(mylist[4]) <= 1000):
                        #print "Valid status, computing solution message"
                        stringforeval = mylist[2] + mylist[3] + mylist[4]
                        #print stringforeval
                        result = eval(stringforeval)
                        #print result
                        #Format the solution message
                        SOLUTION = 'cs653fall2017 ' + str(result) + '\n'
                        #print SOLUTION
                        mysocket.sendall(SOLUTION)
                except:
                    print "Invalid server response format. Terminating the program"
                    loopcondition = False
                    return
        elif len(mylist) == 3:
            #potential BYE message, format must be cs653fall2017 [a 64 byte secret flag] BYE\n
            if (mylist[0] == 'cs653fall2017') and (mylist[2] == 'BYE'):
                #Awesome, we got the secret flag
                print mylist[1]
                loopcondition = False
        else:
            #server response is invalid
            print "Invalid server response format. Terminating the program"
            loopcondition = False
            return

if __name__ == "__main__":
    main(sys.argv)
