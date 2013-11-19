import asyncore
import socket
from time import time

class EchoHandler(asyncore.dispatcher_with_send):

  def handle_read(self):
    data = self.recv(8192)
    if data:
      self.send(data)
      print data

class EchoServer(asyncore.dispatcher):

  host = None
  port = None
  def __init__(self, host, port):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.set_reuse_addr()
    self.host = host
    self.port = port

  def clientConnectTo(self, host = socket.gethostname(), port = 5555):
    nc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp SOCK_STREAM | udp SOCK_DGRAM
    nc.connect((host,port))
    nc.send("send: "+self.host+" "+self.port)

  def serverBindLoop(self):
    self.bind((self.host, self.port))
    self.listen(5)
    asyncore.loop()

  def handle_accept(self):
    pair = self.accept()
    if pair is not None:
      sock, addr = pair
      print 'Incoming connection from %s' % repr(addr)
      handler = EchoHandler(sock)

if __name__ == "__main__":
  #server = EchoServer('localhost', 8080) asyncore.loop()
 
  #from tcpserverasyncore import EchoServer 
  server = EchoServer('localhost', 5555)
  server.serverBindLoop()
