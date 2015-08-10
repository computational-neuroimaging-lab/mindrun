#!/usr/bin/env python2.6

import socket
import os,sys
from time import sleep

tcp_host = ''
tcp_port = -1
infile = ''
delay=-1

if len(sys.argv) < 4:
    print " ".join(["Usage:", os.path.basename(sys.argv[0]), \
        "-infile=<file_to_send>","-tcphost=<server address>", \
        "-tcpport=<server port>","-delay=<delay in seconds>"])
    sys.exit(1)

try:
    for cmd_str in sys.argv[1:]:
        if "-infile=" in cmd_str:
            infile=cmd_str.split("=")[1]
            continue
        if "-tcphost=" in cmd_str:
            tcp_host=cmd_str.split("=")[1]
            continue
        if "-tcpport=" in cmd_str:
            tcp_port=int(cmd_str.split("=")[1])
        if "-delay=" in cmd_str:
            delay=float(cmd_str.split("=")[1])
except:
    print >> sys.stderr, "Error decoding command line %s"% \
        (" ".join(sys.argv))+" :: "+str(sys.exc_info()[0])+"\n"
    sys.exit(1)

# verify that we received all of the neccessary arguements
if not infile or not tcp_host or tcp_port == -1 or delay == -1:
    print >> sys.stderr, "\nError decoding command line %s"% \
        (" ".join(sys.argv))+"\n"
    print >> sys.stderr, " ".join(["Usage: ", \
        os.path.basename(sys.argv[0]), \
        "-infile=<file_to_send>","-tcphost=<server address>", \
        "-tcpport=<server port>","-delay=<delay in seconds>"])+"\n"
    sys.exit(1)

# open the file
try:
    fd=open(infile,"r")
except IOError as (errno):
    print >> sys.stderr, "Could not open file %s (%d).\n"%(infile,errno)
    sys.exit(1)

# setup the socket communication with the server
# used the example from: 
#    http://docs.python.org/release/2.5.2/lib/socket-example.html
#
s = None
for res in \
    socket.getaddrinfo(tcp_host, tcp_port, socket.AF_UNSPEC, \
    socket.SOCK_STREAM):

    af, socktype, proto, canonname, sa = res
    try:
	s = socket.socket(af, socktype, proto)
    except socket.error, msg:
	s = None
	continue
    try:
	s.connect(sa)
    except socket.error, msg:
	s.close()
	s = None
	continue
    break

if s is None:
    print 'Could not establish connection to: %s (%d)'%(tcp_host,tcp_port)
    fd.close()
    sys.exit(1)

# inform user of our progress
print "\n%s: Sending the contents of %s to %s (%d) at the rate of"% \
    (os.path.basename(sys.argv[0]), infile, tcp_host, tcp_port),
print "one value every %5.3f seconds"%(delay)

# send the contents of the file to the server
cnt=0
for line in fd:
    line.strip()
    s.send(line)
    cnt=cnt+1
    # now implement the delay
    sleep(delay)

s.close()
fd.close()

print "sent %d values"%(cnt)
