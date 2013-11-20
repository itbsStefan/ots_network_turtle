# -*- coding: utf-8 -*-
import helper as h
import turtle
from otsTurtleClasses import Oturtle


print 10*"-=","Start Main",10*"=-"

# shortcut globals to be used for classic turtle
w=turtle.Screen()
root = w._root
cv = turtle.getcanvas()
#t = turtle.getturtle()


length = 10.0

# setup some turtles
turtle.register_shape("dreieck", ((5,-3),(0,5),(-5,-3)))
print w.getshapes()
ot = Oturtle("dreieck","dreieck")
#ot.showturtle()

print "variable ot ist Turtle:",ot.name

t1 = Oturtle("t1", "turtle", True, ("blue","purple"))
t1.setup(50,None, head = 180, speed=5, size = 2)
t1.bindKeys("Up", "Right", "Down", "Left", "Shift_R", "backslash")
t1.win.bind("b", t1.gruen)

t2 = Oturtle("t2", "turtle", True, ("red","yellow"))
t2.setup(-50, None, 0, 3, 3)
t2.bindKeys("w", "d", "s", "a", "Shift_L", "e")
t2.win.bind("v", t2.gruen)
t2.pu()

# Print some stuff on console
print t1.win, w
print t2.ground
for s in w.turtles():
  name = None
  if type(s).__name__ == "Oturtle":
    name = s.name
  print s.__class__, name

# functions to play with
def stamp():
  t1.stamp()
  t2.stamp()
def dot():
  t1.dot()
  t2.dot()
def testfun():
  x = t2.pen()
  t2.stamp()
  t2.pendown()
  t2.circle(100)
  t2.pen(x)

# global key event for turtle window
turtle.onkey(dot, "o")
turtle.onkey(stamp, "space")
t2._screen.onkey(t2.testfun,"h")
w.onkey(testfun, "t")
w.onkey(w.bye, "x")

h.show(turtle._CFG)
print "use turtlekeys to move, v b m o space h t for Actions and x for close the Window"


oldColor = None
def gruen(e):
  global oldColor
  print e
  ot.showturtle()
  oldColor = ot.color()
  ot.color("black","green")
  root.after(3000, cback)

def cback():
  global oldColor
  if isinstance(oldColor, tuple):
    ot.color(oldColor[0],oldColor[1])
root.bind("g", gruen)


fwd=1
def task():
    global fwd
    ot.penup()
    ot.forward(fwd)
    ot.stamp()
    ot.right(33)
    fwd += 1
    if fwd < 100:
      root.after(100, task)  # reschedule event in 1 milli second
root.bind("s", gruen)

root.after(1, task)

import asyncore
import logging
from chat_echo import *

f= '%(name)s: %(message)s'
logging.basicConfig(level=logging.DEBUG,format=f)

address = ('localhost', 0) # let the kernel give us a port
server = EchoServer(address)
ip, port = server.address # find out what port we were given
# write the port in a file to grab it from other scripts
fp = open('PortAsynTest.txt', 'w')
fp.write(str(port).encode("utf-8"))
fp.close
fp = None

asynloop = False
loop_counter = 0
def asyntask():
  global loop_counter, asynloop, logging
  loop_counter += 1
  #logging.debug('--->loop_counter=%s', loop_counter, str(asyncore.socket_map))
  #print "asyntask", loop_counter
  asyncore.loop(timeout=0.1, count=1)
  if asynloop:
    root.after(100, asyntask)  # reschedule event in 1 milli second

def asynloopStart(event=None):
  global asynloop,ip, port
  print
  print "asynloopStart EchoServer is on",ip, port, "already running"
  print "Press c to start a EchoClient with a hello message or run from an other console"
  print "<python Clientchat_echo.py lorem.txt> to send massive text!"
  print 7*"¸,ø¤º°`°º¤ø,"
  asynloop = True
  root.after(1, asyntask)
def asynloopStop(event=None):
  global asynloop
  print "asynloopStops now (Messages of clients will processed after restart Loop!)"
  asynloop = False
root.bind("y", asynloopStart)
root.bind("Y", asynloopStop)

def asynClientTask(event=None):
  global ip, port
  print "call EchoClient", ip, port
  client = EchoClient(ip, port, message="Hallo")

root.after(3, asynloopStart)
root.bind("c", asynClientTask)

root.mainloop()





##
## versuche 
##

#import Tkinter
#r = Tkinter.Tk()
#r.bind("<KeyPress>", h.callback)
#w.listen()
#w.onclick(t.goto)
#turtle.exitonclick()






#import threading, time
#import Tkinter

#root = Tkinter.Tk()
##root = turtle.getcanvas()
#def ping():
#  while 1:
#    time.sleep(1)
#    print root.bind()
#    root.event_generate('<<Ping>>', when='tail')
#    print "it worked"


#v = Tkinter.BooleanVar()
#v.set(0)
#def gotPing(event):
#  v.set(not v.get())

#check = Tkinter.Checkbutton(root, variable=v, text='Ping!')
#check.pack(side=Tkinter.TOP)
#butto = Tkinter.Button(root, text='Quit', command=root.quit)
#butto.pack(side=Tkinter.TOP)
#s = "Test"
#l = Tkinter.Label(root,text=s)
#l.pack(side=Tkinter.TOP)

#root.bind('<<Ping>>', gotPing)
#th = threading.Thread(target=ping)
#th.setDaemon(1)
#th.start()
