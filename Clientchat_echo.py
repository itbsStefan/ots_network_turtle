from chat_echo import EchoClient
import asyncore
import sys


fp = open('PortAsynTest.txt', 'r')
fport = fp.read().decode("utf-8")
fp.close
fp = None
print "|"+fport+"|"
i = int(fport)
ip, port = ('localhost',i) # find out what port we were given

filename = "lorem.txt"
if len(sys.argv) > 1:
  filename = sys.argv[1]

message_data = open(filename, 'r').read()
client = EchoClient(ip, port, message=message_data)


asyncore.loop(timeout=30.0, use_poll=False, map=None, count=None)


