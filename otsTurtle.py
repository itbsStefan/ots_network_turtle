# coding=utf-8
import turtle
l=30
s=60

#turtle.forward(3*l)


a=2
b=4
import math
c = math.sqrt(a**2 + b**2)
print c

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
	print "Penstatus",turtle.pen()["pendown"]

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
turtle.onkey(dot, "d")
turtle.onkey(lengthPlus, "bracketright")
turtle.onkey(lengthMinus, "slash")
turtle.onkey(move, "m")

def callback(e):
	print e.keysym, repr(e.char)



w=turtle.Screen()
#help(w)
#w.bind("<KeyPress>", callback)

turtle.listen()

turtle.exitonclick()

