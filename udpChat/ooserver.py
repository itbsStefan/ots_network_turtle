#!/usr/bin/env python
'''

server usage:

python server.py [ip address] [port]

'''

import socket
import time
import sys
import json

class Server(object):
  """UDP Chat Server
  """

  #  this function sends a message to everyone who is "connected"
  def broadcast(self,data):
    for client in self.clients:
      self.sock.sendto(data, client[1])

  def randomName(self, length = 5):
    return "".join(random.choice(string.lowercase) for i in range(length))
  
  def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "(",self.name,")", "destroyed"
  
  def __init__(self, ip, port, name="", run = False):
    self.ip = ip
    self.port = port
    #  keep a list of "connected" clients, even though we're not really
    #  accepting connections per se. The purpose of this is to allow us
    #  to replay chat messages to other people and
    #  to see who's in the chatroom, etc
    if name == "":
      name = self.randomName()

    self.clients = []
    if name:
      self.clients.append((name, (ip, port)))

    self.name = name

    #  create a datagram socket 
    self.sock = socket.socket( socket.AF_INET, # Internet
                        socket.SOCK_DGRAM ) # UDP

    #  bind the socket to a port, to allow people to send info to it
    self.sock.bind( (ip,port) )

    self.run = False
    if run:
      self.go()

  def stop(self):
    self.run = False

  def go(self):
    """endless loop
    """
  #  main loop for the server
  #  in this loop we try to receive data on the socket
  #  and then we relay the message to other clients
    if self.run:
      print "Server is running! Cannot run twice."
    else:
      self.run = True  
      while self.run:
        data = None
        message = None
        try:
          
          # try to get a message on the socket
          data, addr = self.sock.recvfrom( 1024, socket.MSG_DONTWAIT ) # buffer size is 1024 bytes

          #  if there's a message, then parse it and add the client to the list
          #  if they're a new client
          message = json.loads(data)
          client = (message['username'], addr)
          if client not in self.clients:
            clients.append(client)
        
        #  if no message was available, just wait a while
        except socket.error:

          # wait a bit to keep from clobbering the CPU
          time.sleep(0.01)

        if data:
         
          print data
          try: 

            #  the /hello message announces the new client
            if( message['message'].startswith("/hello") ):

              outjson = {"username" : "server",\
                "message" : message['username'] + " joined the chat",\
                "color" : 35 } 

              self.broadcast( json.dumps(outjson) )

            #  the /who message is only echoed back to the client who sent it
            #  The response is a list of other people in the chat room
            elif ( message['message'].startswith("/who") ):

              outjson = {"username" : "server",\
                "message" : "people in room: " + ', '.join([y[0] for y in clients]),\
                "color" : 35 } 

              self.sock.sendto( json.dumps(outjson), client[1] )

            #  The /goodbye message let's everyone know we're leaving
            elif ( message['message'].startswith("/goodbye") ):

              outjson = {"username" : "server",\
                "message" : message['username'] + " left the chat",\
                "color" : 35 } 

              self.clients.remove(client)

              self.broadcast( json.dumps(outjson) )

            elif ( message['message'].startswith("/stop") ):

              outjson = {"username" : self.name,\
                "message" : message['username'] + " stops this server",\
                "color" : 35 } 
              self.run = False
              #self.clients.remove(client)              

            #  The /me message creates an "emote"
            elif ( message['message'].startswith("/me") ):

              newmsg = message['username'] + message['message'][3:]
              outjson = {"username" : None,\
                "message" : newmsg,\
                "color" : message['color'] } 

              self.broadcast( json.dumps(outjson) )
      
            #  All other messages are simply re-broadcasted back to all clients
            else:

              outjson = {"username" : message['username'],\
                "message" : message['message'],\
                "color" : message['color'] }
              
              self.broadcast( json.dumps(outjson) )
            
            print clients

          except ValueError:

            print "indecipherable json"
      print self.__class__.__name__,"(",self.name,")", " has stoped"


if __name__ == "__main__":
  import getopt, random, string, os

  ip = "127.0.0.1" #socket.gethostname()
  port = 5558
  try:
    opts, args = getopt.getopt(sys.argv[1:],"hri:p:n:",["help","run","ip=","port=","name="])
  except getopt.GetoptError:
    print sys.argv[0],'-i <IP-Adress> -p <Portnumber> [-n <Chatname> --run]'
    sys.exit(2)
    quit()

  print getopt.error.opt
  run = False
  name = ""

  for opt, arg in opts:
    if opt == '-h':
       print "usage:", sys.argv[0], "[-i|--ip=IPADRESS] [-p|--port=PORTNUMBER] [--name=CHATNAME] [--help] [--run]"
       sys.exit()
    elif opt in ("-i", "--ip"):
       ip = arg
    elif opt in ("-p", "--port"):
       port = int(arg)  
    elif opt in ("-n", "--name"):
       name = arg  
    elif opt in ("-r", "--run"):
       run = True

  server = Server(ip,port,name,run)
  if run == True:
    pass
  else:
    try: 
      cmd = raw_input("hit enter to start! ") 
    except ValueError: 
      pass
    if len(cmd) > 2:
      server.name = cmd
    server.go()  




