import socket
import helper as h
import sys

thp = (socket.gethostname(), 5555)
tbo = ("<broadcast>", 5555)
cid = h.randomString(10)
# create an INET, UDP socket
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
udpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
udpsocket.settimeout(5)

# bind the socket to a public host Server
#udpsocket.bind(thp)

if len(sys.argv) == 2:
  msg = sys.argv[1]
else:
  msg = h.randomString(5)

try:
  udpsocket.sendto(msg, tbo)
  #(msg,ipp) = udpsocket.recvfrom(1024)
  print "Response: %s" % udpsocket.recv(1024)  
except socket.timeout:
    print "No server found"

while msg != "stop":
  try:
    (msg,ipp) = udpsocket.recvfrom(1024)
    print msg
  except socket.timeout:
    pass
  udpsocket.sendto(h.randomString(3),tbo)

udpsocket.close()
