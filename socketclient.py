import socket
from time import time
import helper as h

clientname = h.randomString(6)
print "My Name is",clientname
#create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM) # tcp SOCK_STREAM | udp SOCK_DGRAM

s.connect((socket.gethostname(),5555))

s.send(clientname+" "+ str(time()))
msg = s.recv(1024)
print "1 "+msg+" back on "+ str(time())
msg = s.recv(1024)
print "2 "+msg
msg = s.recv(1024)
print "3 "+msg
msg = s.recv(1024)
print "4 "+msg



s.shutdown(1)


