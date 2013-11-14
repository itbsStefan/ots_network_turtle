# -*- coding: utf-8 -*-
from turtle import Screen
from otsTurtleClasses import Oturtle


t = Oturtle("Turtle", "turtle", True, ("blue","red"))
t.setup(50,None, head = 180, speed=5, size = 2)

root = Screen()._root

fwd = 1
def task():
    global fwd
    t.forward(fwd)
    t.right(33)
    fwd += 1
    root.after(1, task)  # reschedule event in 1 milli second


Screen().onclick(t.goto)
Screen().onkey(Screen().bye, "x")
root.bind("g", t.gruen)
root.bind("e", t.eventCatcher)
Screen().listen()

root.after(1, task)
root.mainloop()
