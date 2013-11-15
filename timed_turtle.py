# -*- coding: utf-8 -*-
from otsTurtleClasses import Oturtle
import helper as h

t = Oturtle("Turtle", "turtle", True, ("blue","red"))
t.setup(50,None, head = 180, speed=5, size = 2)


root = t.win
fwd = 1
def task():
    global fwd
    t.forward(fwd)
    t.right(33)
    fwd += 1
    if fwd < 100:
      root.after(1, task)  # reschedule event in 1 milli second


t.ground.onclick(t.goto)
t.ground.onkey(t.ground.bye, "x")
t.win.bind("g", t.gruen)
t.ground.listen()

print t._Oturtle__oldColor # das geht immer noch



task()
t.win.mainloop()
