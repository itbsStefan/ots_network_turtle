# coding=utf-8
from turtle import Turtle
from random import choice    # Choose a random element from a non-empty sequence
from random import randint   # Return random integer in range [a, b], including both end points
from string import lowercase # Rerurns 'abcdefghijklmnopqrstuvwxyz'


class Oturtle(Turtle):

  name = None
  cv = None
  _keys = None
  _root = None

  def randomString(self, length = 5):
    return "".join(choice(lowercase) for i in range(length))

  def __init__(self,name = "", shape = "turtle", visible = False, colors = None):
    Turtle.__init__(self, shape, visible=visible)
    self._root = self._screen._root
    self.cv = Turtle._screen._canvas
    if name =="":
      self.name = self.randomString(8)
    else:
      self.name = name
    if colors == None:
      self.color("black", "pink")
    else:
      self.color(colors[0],colors[1])
    self._keys = []

  def printName(self):
    print self.__class__.__name__, self.name

  def setup(self, x = None, y = None, head = None, speed=None, size = 1):
    self.resizemode("auto")
    self.pensize(size)
    if speed == None:
      self.speed(randint(1,10))
    else:
      self.speed(speed)
      if speed < 0 or speed > 10:
        print "Speed has bad value set to 0 by", self.name, self
        self.speed(0)
    if head == None:
      self.setheading(randint(0,359.9))
    else:
      self.setheading(head)
    s = self.getscreen()
    h = (s.window_height()-10)/2
    w = (s.window_width()-10)/2
    if x == None:
      x = randint(-w,w)
    if y == None:
      y = randint(-h,h)
    self.up()
    self.goto(x,y)
    self.down()

  def _onkey(self, fun, key):
    """Bind fun to key-release event of key.
    Canvas must have focus. See method listen
    """
    if fun is None:
      self.cv.unbind("<KeyRelease-%s>" % key, None)
    else:
      def eventfun(event):
        fun()
      self.cv.bind("<KeyRelease-%s>" % key, eventfun)
      print self.name, "bindKey", key

  def onkey(self, fun, key):
    """Bind fun to key-release event of key.
    """
    if fun == None:
      if key in self._keys:
        self._keys.remove(key)
    else:# key not in self._keys:
      self._keys.append(key)
      self._onkey(fun, key)

  def hoch(self):
    self.setheading(90)
    self.forward(10)

  def links(self):
    self.setheading(180)
    self.forward(10)

  def rechts(self):
    self.setheading(0)
    self.forward(10)

  def runter(self):
    self.setheading(270)
    self.forward(10)

  def cursorKeys(self,keys):
    funs = ["hoch", "rechts", "runter", "links", "testfun"]
    t=0
    print type(keys).__name__
    if type(keys).__name__ == "tuple":
      print len(keys), keys
      for f in funs:
        if t < len(keys):
          break
        self._onkey(eval("self."+f+"()"), keys[t])
        print "self.",f,"()",keys[t]
        t +=1
    else:
      print "cursorKeys must be a tuple of 4 or more Chars! (up rigth down left action)"

  def testfun(self):
    x = self.pen()
    self.stamp()
    self.pendown()
    self.home()
    self.pen(x)










  def eventCatcher(self,event):
    print "event:", event.keycode, type(event).__doc__
    if type(event).__name__:
      pass


  oldColor = None
  def gruen(self,e):
    self.oldColor
    print e
    self.oldColor = self.color()
    self.color("violet","green")
    self._root.after(3000, self.cback)

  def cback(self):
    self.oldColor
    if type(self.oldColor).__name__ == "tuple":
      self.color(self.oldColor[0],self.oldColor[1])




















