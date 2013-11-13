# coding=utf-8
import turtle
from otsTurtleClasses import Oturtle

def show(dictionary):
  print "=========================="
  print "=  Turtle Configuration  ="
  print "=========================="
  for key in sorted(dictionary.keys()):
    print key, ":", dictionary[key]
  print "=========================="
  print

def callback(e):
	print e.keysym, repr(e.char)

w=turtle.Screen()
#t = turtle.getturtle()

length = 10.0
turtle.register_shape("dreieck", ((5,-3),(0,5),(-5,-3)))

ot = Oturtle("dreieck","dreieck")
#ot.showturtle()
ot.printName()




t1 = turtle.Turtle()
t1.shape("dreieck")
t1.color("blue","purple")
t1.resizemode("auto")
t1.pensize(2)
t1.speed(5)
t1.up()
t1.setheading(180)
t1.goto(50, 0)
t1.down()

t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("red","yellow")
t2.resizemode("auto")
t2.speed(3)
t2.up()
t2.setheading(0)
t2.goto(-50, 0)
t2.down()






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

turtle.onkey(turtleUp, "Up")  #  90
turtle.onkey(turtleDown, "Down")# 270
turtle.onkey(turtleLeft, "Left")# 180
turtle.onkey(turtleRight, "Right")#  0
turtle.onkey(togglePen, "p")


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

turtle.onkey(turtle2Up, "w")  #  90
turtle.onkey(turtle2Down, "s")# 270
turtle.onkey(turtle2Left, "a")# 180
turtle.onkey(turtle2Right, "d")#  0



def stamp():
  t1.stamp()
  t2.stamp()
def dot():
  t1.dot()
  t2.dot()
turtle.onkey(dot, "o")
turtle.onkey(stamp, "i")


show(turtle._CFG)
print "use curserkeys to move turtle1 and  w|a|s|d for tutle2 (purple)"

turtle.listen()
turtle.exitonclick()







