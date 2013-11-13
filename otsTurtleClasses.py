# coding=utf-8
from turtle import Turtle
from random import choice
from string import lowercase

class Oturtle(Turtle):

  def randomString(self, length = 5):
    return "".join(choice(lowercase) for i in range(length))

  def __init__(self,name = "", shape = "turtle", visible = False, colors = None):
    Turtle.__init__(self, shape, visible=visible)
    if name =="":
      self.name = self.randomString(8)
    else:
      self.name = name
    if colors == None:
      self.color("black", "pink")

  def printName(self):
    print self.__class__.__name__, self.name


