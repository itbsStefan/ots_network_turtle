# -*- coding: utf-8 -*-
def show(dictionary, title = "Turtle Configuration"):
  #print "%03d - |%7s|" % (title)
  l = len(title)+6
  print l*"="
  print "= ",title, " ="
  print l*"="
  for key in sorted(dictionary.keys()):
    t = type(dictionary[key])
    print "%-14s (%8s) : %-10s" % (key,t.__name__,str(dictionary[key]))
  print l*"="
  print

def callback(e): # r = Tkinter.Tk() r.bind("<KeyPress>", callback)
  print e.keysym, repr(e.char)

