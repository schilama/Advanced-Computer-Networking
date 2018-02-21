#!/usr/bin/env python

import sys
import socket
from bs4 import BeautifulSoup
import re

frontier = ["/fakebook/"]
beenthere = []
secretflag = []
secretflagcount = 0

def thesocketstuff(getorpoststring):
    #creates a socket, connects to server, sends the getorpoststring to the server and returns response
    hostname = "elsrv2.cs.umass.edu"
    #port number is 80 for HTTP
    portnum = 80
    try:
        #creating a socket
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print "Socket creation failed"
        return
    try:
        #resolving hostname
        serverip = socket.gethostbyname(hostname)
    except:
        print "Could not resolve host"
        return
    try:
        #connecting to the server
        mysocket.connect((serverip,portnum))
    except:
        print "Unable to connect to server"
        return
    mysocket.sendall(getorpoststring)
    datastring = ''
    for i in range(10):
        datastring = datastring + mysocket.recv(4096)
    #print datastring
    mysocket.close()
    return datastring

def computecookie(datastring):
    #Finding cookie header value
    #Assuming server returns Set-Cookie: name=value; otherparameter; anotherparameter we will parse for name=value
    cookieregex = re.compile('Cookie:[\s,\w,=]*;')
    cookielist = cookieregex.findall(datastring)
    #print cookielist
    try:
        cookieheader = 'Cookie:'
        for i in range(0,len(cookielist)):
            #Ignore 'Cookie: ' and take the name=value;
            cookieheader = cookieheader + cookielist[i][8:]
        #Remove trailing ; (needs to be done only for the last name=value; pair)
        cookieheader = cookieheader[:len(cookieheader)-1]
        #print cookieheader
    except:
        print "No cookies found"
        return
    return cookieheader

def searchforsecretflag(datastring):
    #Using Beautiful Soup library to search for secret flag
    soup = BeautifulSoup(datastring, "lxml")
    #secretflaglist = soup.find_all("h2", class_="secret_flag")
    secretflaglist = soup.find_all(string=re.compile("FLAG:"))
    return secretflaglist

def getlinksfromcurrentURL(datastring):
    #Using Beautiful Soup library to search for links
    soup = BeautifulSoup(datastring, "lxml")
    listoflinks = []
    listofvalidlinks = []
    for link in soup.find_all('a'):
        listoflinks.append(link.get('href'))
    #only crawl valid links - a valid link has /fakebook/ in href
    fakebookregex = re.compile('/fakebook/')
    for item in listoflinks:
        if fakebookregex.match(item):
            listofvalidlinks.append(item)
    return listofvalidlinks

def parseHTTPresponsecode(datastring,cookieheader):
    global frontier
    global beenthere
    global secretflag
    global secretflagcount
    #Sample: HTTP/1.0 302 FOUND
    try:
        statuscode = (datastring.split("\n")[0]).split()[1]
    except:
        print datastring
        print datastring.split("\n")
        print (datastring.split("\n")[0]).split()
        return
    if statuscode == '200':
        #200 - OK - do nothing
        #print statuscode
        return statuscode
    elif statuscode == '403' or '404':
        #403 - Forbidden or 404 - Not Found - Abandon URL
        #print statuscode
        return statuscode
    elif statuscode == '301':
        #301 - Redirect - GET URL in server response
        #obtain new location
        #print statuscode
        locationregex = re.compile('Location:')
        locationstring = ''
        for item in datastring.split("\n"):
            if locationregex.match(item):
                locationstring = item
        #verify that redirect location is in domain http://elsrv2.cs.umass.edu
        if locationstring.find('http://elsrv2.cs.umass.edu'):
            location = locationstring[locationstring.find('http://elsrv2.cs.umass.edu') + len('http://elsrv2.cs.umass.edu'):]
        else:
            #location is invalid, do not navigate there
            return statuscode
        if location not in beenthere:
            beenthere.append(location)
            #cookieheader = computecookie(datastring)
            datastring = thesocketstuff("GET " + location + " HTTP/1.0\r\n" + cookieheader + "\r\n\r\n")
            if searchforsecretflag(datastring):
                for item in searchforsecretflag(datastring):
                    secretflag.append(item)
                    secretflagcount = secretflagcount + 1
            listofvalidlinks = getlinksfromcurrentURL(datastring)
            if listofvalidlinks:
                for item in listofvalidlinks:
                    if item not in beenthere:
                        frontier.append(item)
            parseHTTPresponsecode(datastring,cookieheader)
        return statuscode
    elif statuscode == '500':
        #print statuscode
        #500 - Internal Server Error - Retry GET until successful
        return statuscode
        #Repeated re-trying will be implemented in while loop in main function
    else:
        #print statuscode
        #some other status code
        return statuscode

def main(inputlist):

    global frontier
    global beenthere
    global secretflag
    global secretflagcount

    try:
        username = inputlist[1]
        password = inputlist[2]
    except:
        print "Please execute the program again using this format ./webcrawler [username] [password]"
        return

    #http://elsrv2.cs.umass.edu/accounts/login/?next=/fakebook/ for POST
    #First we GET the form to identify the csrf value for this session and then POST the key value pairs

    HTTPget = "GET /accounts/login/?next=/fakebook/ HTTP/1.0\r\n\r\n"
    datastring = thesocketstuff(HTTPget)

    #Using Beautiful Soup library to parse csrf value
    soup = BeautifulSoup(datastring, "lxml")
    csrftokenvalue = soup.find('input',{'name':'csrfmiddlewaretoken'})['value']
    #print csrftokenvalue

    #Finding cookie values
    cookieheader = computecookie(datastring)

    #Attempting to login now
    #Formatting the POST message
    formparameters =  "username=" + str(username) + "&password=" + str(password) + "&csrfmiddlewaretoken=" + csrftokenvalue + "&next=%2Ffakebook%2F"
    HTTPpost = '''POST /accounts/login/ HTTP/1.0\r\nHost: elsrv2.cs.umass.edu\r\nContent-Length: %d\r\n%s\r\n\r\n%s\r\n''' % (len(formparameters),cookieheader,formparameters)
    #print HTTPpost
    datastring = thesocketstuff(HTTPpost)
    #print datastring
    cookieheader = computecookie(datastring)

    count = 0
    while count < len(frontier) and count < 8000 and secretflagcount < 5 :
        continuetoget = True
        gettimeout = 0
        if frontier[count] not in beenthere:
            beenthere.append(frontier[count])
            #cookieheader = computecookie(datastring)
            #print "GET " + frontier[count] + " HTTP/1.0\r\n" + cookieheader + "\r\n\r\n"
            datastring = thesocketstuff("GET " + frontier[count] + " HTTP/1.0\r\n" + cookieheader + "\r\n\r\n")
            #print datastring
            statuscode = parseHTTPresponsecode(datastring,cookieheader)
            if statuscode == '200':
                if searchforsecretflag(datastring):
                    for item in searchforsecretflag(datastring):
                        secretflag.append(item)
                        secretflagcount = secretflagcount + 1
                listofvalidlinks = getlinksfromcurrentURL(datastring)
                if listofvalidlinks:
                    for item in listofvalidlinks:
                        if item not in beenthere:
                            frontier.append(item)
                count = count + 1
                continue
            elif statuscode == '403' or '404':
                count = count + 1
                continue
            elif statuscode == '301':
                count = count + 1
                continue
            elif statuscode == '500':
                while continuetoget:
                    gettimeout = gettimeout + 1
                    datastring = thesocketstuff("GET " + frontier[count] + " HTTP/1.0\r\n" + cookieheader + "\r\n\r\n")
                    statuscode = parseHTTPresponsecode(datastring)
                    if statuscode != '500' or gettimeout == 100:
                        continuetoget = False
                if searchforsecretflag(datastring):
                    for item in searchforsecretflag(datastring):
                        secretflag.append(item)
                        secretflagcount = secretflagcount + 1
                listofvalidlinks = getlinksfromcurrentURL(datastring)
                if listofvalidlinks:
                    for item in listofvalidlinks:
                        if item not in beenthere:
                            frontier.append(item)
                count = count + 1
                continue
            else:
                count = count + 1
                continue
        else:
            count = count + 1
            continue
    #print count
    #print secretflag
    for flag in secretflag:
        print flag[6:]

if __name__ == "__main__":
    main(sys.argv)
