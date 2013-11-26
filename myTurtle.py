# coding=utf-8
import turtle
l=30
s=60

#turtle.forward(3*l)


def show(dictionary):
  print "=========================="
  print "=  Turtle Configuration  ="
  print "=========================="
  for key in sorted(dictionary.keys()):
    print key, ":", dictionary[key]
  print "=========================="
  print

from turtle import *
def n_eck(n, size):
  for i in range(n):
    rt(360./n)
    fd(size)
def mn_eck(n, size):
  for i in range(n):
    rt(360./n)
    n_eck(n, size)

#bgcolor("black")
pencolor("red")
pensize(3)
speed(10)
#mn_eck(36, 20)



a=2
b=4
import math
c = math.sqrt(a**2 + b**2)
print c

t1 = turtle.Turtle()

def switchpen():
  global t1
  if t1.isdown():
    t1.pu()
  else:
    t1.pd()



t1.shape("turtle")
t1.color("blue","purple")
t1.resizemode("auto")
t1.pensize(2)
t1.speed(16)
t1.up()
t1.goto(-80, -340)
t1.down()

t2 = turtle.getturtle()
t2.up()
t2.shape("turtle")
t2.color("red","yellow")
t2.resizemode("auto")
t2.speed(8)
t2.setheading(t2.towards(t1))
t2.goto(280, 40)
t2.down()


count = 1
while t2.distance(t1) > 4:
  print count
  t1.fd(3.5)
  t1.lt(0.6)
  t2.setheading(t2.towards(t1))
  t2.fd(3.3)
  if count > 200:
    t2.fd(1.3)
  if count % 20 == 0:
      t1.stamp()
      t2.stamp()
      switchpen()
  count += 1

turtle.up()
turtle.setheading(270)
turtle.forward(15)
turtle.setheading(180)
turtle.forward(5)

def hexagon(s1=10, s2=60):
	print "x",turtle.xcor(),"  y",turtle.ycor()
	for i in range(6):
		print i, 'hexagon', s1,s2
		dashforward(s1)
		turtle.left(s2)

def dashforward(l):
	ll=l/6.0
	for i in range(6):
		turtle.forward(ll)
		if turtle.pen()["pendown"]:
			turtle.penup()
		else:
			turtle.pendown()


turtle.color('yellow', 'blue')
colors = ["red","gray","purple","pink","brown","orange"]

for i in range(6):
    print i
    turtle.color(colors[i], 'blue')
    hexagon(l,s)
    turtle.forward(l)
    turtle.right(s)

# x 30.0   y -51.9615242271

c = math.sqrt(30.0**2 + 51.9615242271**2)
turtle.penup()
turtle.setheading(270+30)
turtle.forward(c/2.0)
turtle.color('green', 'blue')
turtle.dot()
turtle.setheading(90)
turtle.forward(150)


def xxx():
	turtle.home()
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)

	turtle.left(25)
	turtle.color('red', 'green')

	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)

length = 10.0
def lengthPlus():
	global length
	length+=1.0
	print "Strichlänge ist jetzt: ",length

def lengthMinus():
	global length
	length-=1.0
	print "Strichlänge ist jetzt: ",length

def moveTurtle(length, direction):
	print "taste gedrückt",length ,direction
	turtle.setheading(direction)
	turtle.forward(length)
	
def togglePen():
	if turtle.pen()["pendown"]:
		turtle.penup()
	else:
		turtle.pendown()
	if t2.pen()["pendown"]:
		t2.penup()
	else:
		t2.pendown()
	print "Penstatus t2",t2.pen()["pendown"]

def dot():
	turtle.dot()

def turtleUp():
	moveTurtle(length, 90)

def turtleLeft():
	moveTurtle(length, 180)

def turtleRight():
	moveTurtle(length, 0)

def turtleDown():
	moveTurtle(length, 270)


def move():
	din = raw_input("Go left or right? ")
	direction = din.strip().lower()
	print "okay then",direction
	if direction == "left":
		turtle.left(90)
		turtle.forward(length)
		dashforward(100)
	if direction == "right":
		turtle.right(90)
		turtle.forward(length)
		hexagon()

turtle.onkey(turtleUp, "Up")  #  90
turtle.onkey(turtleDown, "Down")# 270
turtle.onkey(turtleLeft, "Left")# 180
turtle.onkey(turtleRight, "Right")#  0
turtle.onkey(togglePen, "p")
turtle.onkey(dot, "o")
turtle.onkey(lengthPlus, "bracketright")
turtle.onkey(lengthMinus, "slash")
turtle.onkey(move, "m")

def callback(e):
	print e.keysym, repr(e.char)



w=turtle.Screen()
#help(w)
#w.bind("<KeyPress>", callback)

run = True
def stop():
  global run
  run = False
turtle.onkey(stop, "q")

#while run:
w.onclick(turtle.goto)


def moveT2(length, direction):
	print "taste gedrückt",length ,direction
	#t2.setheading(direction)
	#t2.forward(length)
	t1.setheading(direction)
	t1.forward(length)

def turtle2Up():
	moveT2(length, 90)

def turtle2Left():
	moveT2(length, 180)

def turtle2Right():
	moveT2(length, 0)

def turtle2Down():
	moveT2(length, 270)

turtle.onkey(turtle2Up, "w")  #  90
turtle.onkey(turtle2Down, "s")# 270
turtle.onkey(turtle2Left, "a")# 180
turtle.onkey(turtle2Right, "d")#  0


t1.goto(-50, 0)
t1.setheading(0)
t2.goto(50, 0)
t2.setheading(180)


show(turtle._CFG)
print "use curserkeys to move turtle1 and  w|a|s|d for tutle2 (purple)"


def line(x1, y1, x2, y2):
  pu(); goto(x1, y1); pd(); goto(x2, y2)
def graph(f):
  x = -4
  pu(); goto(x, f(x)); pd()
  while x < 4:
    x += 0.1
    goto(x, f(x))

setworldcoordinates(-4,-2,4,2)
line(-4,0,4,0)
line(0,-2,0,2)
pensize(3)
from math import cos
graph(cos)
dx = 1.e-6
def derivative(f):
  def d(x):
    return (f(x+dx)-f(x))/dx
  return d
pencolor("red")
graph(derivative(cos))




reset()
shape("circle")
pu(); goto(150,0)
fillcolor("red")
shapesize(5, 1, 4)
for i in range(72):
    fd(12)
    lt(5)
    tilt(7.5)
    dummy = stamp()




turtle.listen()
turtle.exitonclick()

