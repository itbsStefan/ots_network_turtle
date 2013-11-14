# coding=utf-8
import helper as h
import turtle
from otsTurtleClasses import Oturtle



w=turtle.Screen()
t = turtle.getturtle()
cv = turtle.getcanvas()

root = turtle.Screen()._root

length = 10.0
turtle.register_shape("dreieck", ((5,-3),(0,5),(-5,-3)))
print w.getshapes()
ot = Oturtle("dreieck","dreieck")
#ot.showturtle()
ot.printName()





t1 = Oturtle("t1", "turtle", True, ("blue","purple"))
t1.setup(50,None, head = 180, speed=5, size = 2)

t2 = Oturtle("t2", "turtle", True, ("red","yellow"))
t2.setup(-50, None, 0, 3, 3)
t2.pu()

for s in w.turtles():
  name = None
  if type(s).__name__ == "Oturtle":
    name = s.name
  print s.__class__, name



def togglePen():
	if t1.pen()["pendown"]:
		t1.penup()
	else:
		t1.pendown()
	if t2.pen()["pendown"]:
		t2.penup()
	else:
		t2.pendown()
	print "Penstatus t2",t2.pen()["pendown"]

w.onkey(togglePen, "p")


def moveTurtle(length, direction):
	#print "taste gedrückt",length ,direction
	t1.setheading(direction)
	t1.forward(length)
	
def turtleUp():
	moveTurtle(length, 90)

def turtleLeft():
	moveTurtle(length, 180)

def turtleRight():
	moveTurtle(length, 0)

def turtleDown():
	moveTurtle(length, 270)

w.onkey(turtleUp, "Up")  #  90
w.onkey(turtleDown, "Down")# 270
w.onkey(turtleLeft, "Left")# 180
w.onkey(turtleRight, "Right")#  0



def moveT2(length, direction):
	#print "taste gedrückt",length ,direction
	t2.setheading(direction)
	t2.forward(length)

def turtle2Up():
	moveT2(length, 90)

def turtle2Left():
	moveT2(length, 180)

def turtle2Right():
	moveT2(length, 0)

def turtle2Down():
	moveT2(length, 270)

w.onkey(turtle2Up, "w")  #  90
w.onkey(turtle2Down, "s")# 270
w.onkey(turtle2Left, "a")# 180
w.onkey(turtle2Right, "d")#  0



def stamp():
  t1.stamp()
  t2.stamp()
def dot():
  t1.dot()
  t2.dot()
turtle.onkey(dot, "o")
turtle.onkey(stamp, "space")


h.show(turtle._CFG)
print "use curserkeys to move turtle1 and  w|a|s|d for tutle2 (purple) and x for close the Window"


def testfun():
  x = t2.pen()
  t2.stamp()
  t2.pendown()
  t2.circle(100)
  t2.pen(x)

t2.onkey(testfun,"j")
w.onkey(testfun, "k")


#import Tkinter
#r = Tkinter.Tk()
#r.bind("<KeyPress>", h.callback)

w.listen()
w.onclick(t.goto)
#turtle.exitonclick()
w.onkey(w.bye, "x")





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


oldColor = None
def gruen(e):
  global oldColor
  oldColor = t2.color()
  t2.color("black","green")
  root.after(3000, cback)

def cback():
  global oldColor
  if type(oldColor).__name__ == "tuple":
    t2.color(oldColor[0],oldColor[1])

root.bind("g", gruen)

fwd=1
def task():
    global fwd
    t1.penup()
    t1.forward(fwd)
    t1.stamp()
    t1.right(33)
    fwd += 1
    root.after(100, task)  # reschedule event in 1 milli second

root.after(1, task)





root.mainloop()

#turtle.mainloop()
#w.mainloop()

