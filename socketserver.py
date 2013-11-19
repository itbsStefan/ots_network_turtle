import socket

# create an INET, STREAMing socket
serversocket = socket.socket(    socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host,
# and a well-known port
serversocket.bind((socket.gethostname(), 5555))
# become a server socket
serversocket.listen(5)

clientsocket = None
clientsocket1 = None
connected = True
while connected:
  # accept incoming connections
  if clientsocket != None:
    clientsocket.send(" will accept others ")
    (clientsocket1,adress1) = (clientsocket,adress)

  (clientsocket,adress) = serversocket.accept()
  if clientsocket1 != None:
    clientsocket.send("accepted")
    clientsocket1.send("please holt the line")

  print 'Incoming connection from %s' % repr(adress)  
  #handler = echoserverasyncore.EchoHandler(clientsocket)

  msg = clientsocket.recv(1024)

  clientsocket.send(msg+"! echo") 
  print "Server recive and send:", msg, msg+"! echo"


