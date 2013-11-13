import turtle

turtle.forward(1)
root = turtle.Screen()._root

fwd = 1


def task():
    global fwd
    turtle.forward(fwd)
    turtle.right(33)
    fwd += 1
    root.after(1, task)  # reschedule event in 1 milli second

root.after(1, task)
root.mainloop()
