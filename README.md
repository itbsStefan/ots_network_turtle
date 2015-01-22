ots_network_turtle
==================

OpenTechSchool Networking Turtle Awesomeness

1. Die Idee ist ein Turtelfenster zu erweitern in den man eigene einzelne 
Pythoncodezeilen absetzen kann. Selbst ausführt und auch ins Netwerk sendet. 
(untere Rand Eingabezeile)

2. Rechte Seite erweitern mit einer Textanzeige von Codezeilen welche aus den 
Brodcastmeldungen aus dem Netzwerk kommen.

Ein guter Startpunkt könnte die im Unterordner workshop enthaltene Demo Anwendung sein.
  cd workshop
  python turtleDemo.py

Sruktur wäre für die ots_network_turtle zu übernehmen, funktionierende Teile aus der main.py entnehmen und als Demodatei ''tdemo_netturtle.py'' zuerstellen.  

Zwischenziel
============

Eventloop nutzen dazu wenn die Taste "g" gedrück wird, soll sich die turtle 
auf grün umfärben und automatisch nach 3 Sekunden zurück färben.

Turtles in der mainLoop lafuen zu lassen eigene Tasten für jedes Obejkt binden.
Während im Hintergrund ein (Server) Socket Verbindungen annimmt 
sowie den content, den es bekommt.
Alles auf der Kommandozeile ausgeben - ohne Threads!


ø¤º°`°º¤ø,¸,ø¤º°`°º¤ø,¸,ø¤º°`°º¤ø,¸,ø¤º°`°º¤ø,¸,ø¤º°`°º¤ø,¸,ø¤º°`°º¤ø,¸,ø¤º°`°º

let's go 
just start 

  python main.py

use turtlekeys to move, v b m o space h t for Actions and x for close the Window
asynchron EchoServer is automaticly running

Press c to start a EchoClient with a hello message 
or run from an other console

python Clientchat_echo.py lorem.txt

Messages will send in Background wihle you can move Turtles

script pyln
-----

just a shell script to shortcut python-executables in the same directory.
Use it to make a symbolic-linkname without .py to your python-file
    pyln main.py
Then you can use instead of "python main.py" only "main" to run
This Links will be in the same directory where pyln is so if you copy it to your ~/bin it will work there and leave your working directory clean.

