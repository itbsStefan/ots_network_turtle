#!/usr/bin/env python

import socket
import os
import sys
import thread
import time
import json
from ooserver import Server

class Client(object):
  """UDP Chat Client
  """

  def __init__(self, server, name, color):
    self.sip = server.ip
    self.sport = server.port
    self.username = name
    self.color = color
    self.sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP

  def get_messages(self):
    global sock, username, color
    while True:
      data = None
      try:
        data, addr = sock.recvfrom( 1024, socket.MSG_DONTWAIT ) # buffer size is 1024 bytes
      except socket.error:
        # wait a bit
        time.sleep(0.01)
      if data:
        #print data
        try:
          
          #  parse the json from the server
          message = json.loads(data)

          #  if the message is from us, then ignore it
          if(message['username'] != username):
            msg_str = message['message']

            #  if there is no user name, don't display it
            if(message['username']):
              msg_str = message['username'] + ": " + msg_str

            #  print the message, with colors if allowed
            if len(message['message']) > 0:
              if allow_color:
                print "\033[%sm%s\033[0m" % (message['color'], msg_str)
              else:
                print msg_str
        except ValueError:
          print "error: tried to decode something invald"

  def get_input(self):
    global sock, username, color
    try:
      while True:
        #message = username + ": " + raw_input()
        #sock.sendto( message, (server_ip, int(server_port) ) )
        message = { "username" : username, "message" : raw_input().strip(), "color" : color  }
        sock.sendto( json.dumps(message), (server_ip, int(server_port)) )

    except KeyboardInterrupt:
      print "byebye now"

  def runLocalChat(self):
    thread.start_new_thread(get_input, ())
    thread.start_new_thread(get_messages, ())

    #  upon "connecting", send /hello and /who to announce our arrival and get a list
    #  of other people in the room
    message = { "username" : self.username, "message" : "/hello", "color" : self.color  }
    self.sock.sendto( json.dumps(message), (self.sip, int(self.sport)) )
    message = { "username" : self.username, "message" : "/who", "color" : self.color  }
    self.sock.sendto( json.dumps(message), (self.sip, int(self.sport)) )
    try: 
      while 1:
        time.sleep(0.01)
    except KeyboardInterrupt:
      print "bye"
    message = { "username" : self.username, "message" : "/goodbye", "color" : self.color  }
    self.sock.sendto( json.dumps(message), (self.sip, int(self.sport)) )
    sys.exit(0)



if __name__ == "__main__":
  import getopt, random, string, os

  ip = socket.gethostname()
  port = 5558
  try:
    opts, args = getopt.getopt(sys.argv[1:],"hri:p:n:c:",["help","ip=","port=","name=", "color="])
  except getopt.GetoptError:
    print sys.argv[0],'-i <IP-Adress> -p <Portnumber> [-n <Chatname> -c <ColorNummber>]'
    sys.exit(2)
    quit()

  print getopt.error.opt
  name = ""
  color = 42
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
    elif opt in ("-c", "--color"):
       color = arg

  sname = name+"s Server"
  #server = Server(ip,port,sname,False)
  print "starte Server", sname
  #thread.start_new_thread(server.go, ())
  ##server.go()

  opt = ''.join(("--run --ip=",ip," --port=",str(port)," --name=",sname))
  os.system("python ooserver.py "+opt+" &")

  if name == "":
    name = server.randomName(8)
  client = client(server,name,color)
  print "starte Client", name, sname
  
  try: 
    cmd = raw_input("hit enter to start! ") 
  except ValueError: 
    pass
  if len(cmd) > 2:
    server.name = cmd
  client.runLocalChat()