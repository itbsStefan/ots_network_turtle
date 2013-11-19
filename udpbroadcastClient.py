import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
s.settimeout(5)

filename = sys.argv[0]
if len(sys.argv) == 2:
    filename = sys.argv[1]

with open(filename, 'r') as f:
    s.sendto(f.read(), ("<broadcast>", 5555))
try:
    print "Response: %s" % s.recv(1024)
except socket.timeout:
    print "No server found"

s.close()

