# coding=utf-8
from turtle import Turtle
from random import choice    # Choose a random element from a non-empty sequence
from random import randint   # Return random integer in range [a, b], including both end points
from string import lowercase # Rerurns 'abcdefghijklmnopqrstuvwxyz'


class Oturtle(Turtle):

  _x = ""
  def getx(self): return self._x
  def setx(self, value): self._x = value
  def delx(self): del self._x
  x = property(getx, setx, delx, "I'm the 'x' property.")

  @property
  def name(self):
    return self._name
  @name.setter
  def name(self, value):
    self._name = value
  _name = None
  _ground = None # is the used Turtle._screen instance of Screen()
  cv = None
  _keys = None
  _root = None
  __inAction = False

  def randomString(self, length = 5):
    return "".join(choice(lowercase) for i in range(length))

  def __init__(self,name = "", shape = "turtle", visible = False, colors = None):
    Turtle.__init__(self, shape, visible=visible)
    self._root = self._screen._root
    self.cv = Turtle._screen._canvas
    if name =="":
      self._name = self.randomString(8) # zufälliges setzen ohne Prüfung
    else:
      self.name = name                  # über die Setter wird geprüft
    if colors == None:
      self.color("black", "pink")
    else:
      self.color(colors[0],colors[1])
    self._keys = []
    self._ground = self._screen

  @property
  def ground(self):
    return self._ground
  @ground.setter
  def ground(self, value):
    self._ground = value
  @ground.deleter
  def ground(self):
    del self._ground
  @property
  def win(self):
    return self._root



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

  def togglePen(self):
    if self.isdown():
      self.penup()
    else:
      self.pendown()

  def bindKeys(self, up, right, down, left, togglePen=False, action=False):
    self._screen.onkey(self.hoch, up)
    self._screen.onkey(self.rechts, right)
    self._screen.onkey(self.runter, down)
    self._screen.onkey(self.links, left)
    if togglePen:
      self._screen.onkey(self.togglePen, togglePen)
    if action:
      self._screen.onkey(self.gruen, action)
    self._screen.listen()
    print self.name, "kann mit den Tasten: hoch="+up+" rechts="+right+" runter="+down+" links="+left+" bewegt,"
    print "mit "+str(togglePen)+" der Stift gesetzt und falls action="+str(action)+" ausgeführt werden."

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
      self._screen.listen()
    else:
      print "cursorKeys must be a tuple of 4 or more Chars! (up rigth down left action)"

  def testfun(self):
    #x = self.pen()
    self.stamp()
    #self.pendown()
    self.home()
    #self.pen(x)










  def eventCatcher(self,event):
    """ Try t.win.bind("<KeyPress>", h.callback)
        to find a String to bind the key
    """
    print "EventCatcher:",event.keysym, event.keycode, "x:",event.x,event.x_root
    if type(event).__name__:
      pass


  __oldColor = None
  def gruen(self,e):
    if self.__inAction & 2:
      print self.name, "startet erst wieder die Methode wenn vorhergehende Aufruf abgearbeitet ist"
      return
    self.__inAction = self.__inAction | 2
    print e.char, e.widget, e.time, e.x, e.x_root,e.keysym, e.keycode
    self.__oldColor = self.color()
    self.color("violet","green")
    self._root.after(3000, self.cback)

  def cback(self):
    if isinstance(self.__oldColor, tuple): 
    #if type(self.__oldColor).__name__ == "tuple": # if isinstance(sf, (int, float)):
      self.color(self.__oldColor[0],self.__oldColor[1])
      self.__oldColor = None
    self.__inAction = self.__inAction & 253

  def nikulaushaus(self):
    pass
  def goBackInView(self):
    pass

  __spiraleschritt=1
  def spirale(self):
    self.forward(self.__spiraleschritt)
    self.right(33)
    self.__spiraleschritt += 1
    self._root.after(1, self.spirale)  # reschedule event in 1 milli second




if __name__ == "__main__":
  print 70*"-"
  ot = Oturtle("Schildkröte", "turtle", True, ("blue","red"))
  ot.setup(50,None, head = 180, speed=5, size = 2)

  ot.bindKeys("u", "k", "j", "h", "p") # enthält self._screen.listen()

  ot.win.bind("g", ot.gruen) # gruen hat noch den Eventparameter daher direkt
  ot.ground.onkey(ot.spirale, "s")
  ot.ground.onkey(ot.testfun, "Home") # geht nur wenn listen() aufgerufen war/wird
  print "Tasten s g und Pos1 führen Methoden der",ot.name,"aus."
  ot.ground.onkey(ot.ground.bye, "x")
  print "x schließt das Fenster"

  ot.win.bind("<KeyPress>", ot.eventCatcher)
  ot.win.mainloop()







