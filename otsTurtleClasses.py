# coding=utf-8
from turtle import Turtle
from random import choice    # Choose a random element from a non-empty sequence
from random import randint   # Return random integer in range [a, b], including both end points
from string import lowercase # Rerurns 'abcdefghijklmnopqrstuvwxyz'


class Oturtle(Turtle):

  name = None
  cv = None
  _keys = None

  def randomString(self, length = 5):
    return "".join(choice(lowercase) for i in range(length))

  def __init__(self,name = "", shape = "turtle", visible = False, colors = None):
    Turtle.__init__(self, shape, visible=visible)
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

  def onkey(self, fun, key):
    """Bind fun to key-release event of key.
    """
    if fun == None:
      if key in self._keys:
        self._keys.remove(key)
      elif key not in self._keys:
        self._keys.append(key)
      self._onkey(fun, key)




