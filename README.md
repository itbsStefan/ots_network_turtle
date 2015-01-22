ots_network_turtle
==================

OpenTechSchool Networking Turtle Awesomeness

* Die Idee ist ein Turtelfenster zu erweitern in den man eigene einzelne 
Pythoncodezeilen absetzen kann. Selbst ausführt und auch ins Netwerk sendet. 
(untere Rand Eingabezeile)

* Rechte Seite erweitern mit einer Textanzeige von Codezeilen welche aus den 
Brodcastmeldungen aus dem Netzwerk kommen.

Ein guter Startpunkt könnte die im Unterordner workshop enthaltene Demo Anwendung sein. [`workshop` Demo](workshop/about_turtledemo.txt)

	cd workshop
	python turtleDemo.py

Sruktur wäre für die ots_network_turtle zu übernehmen, funktionierende Teile aus der main.py entnehmen und als Demodatei ''tdemo_netturtle.py'' zuerstellen.  

Zwischenziel
============

- ein eigenes [Logo](tastepy.svg) in Vektorformat erstellen Vorbild: `tastejsLogo.png`

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


#### pydoc

Um Python zu lernen ist es notwendig sich mit der Documentationssyntax und Werkzeuge auszukennen.
Ein sehr einfaches und dennoch mächtiges ist der Code der in pydoc enthalten ist.
Als Basis ist der Quellcode von 2.7 und 3.4er Version in den Dateien pydoc*Code.py im Repository mit einer eigenen Kopie und eigen Namen könntest Du dir dein eigenes Hilfetool schreiben.

```
	cp pydoc2.7Code.py mydoc.py
	pyln mydoc
	mydoc help
```

Ausgabe:
```
------ starting python /home/stefan/coWork/ots/netTurtlePy/mydoc.py
pydoc - the Python documentation tool

mydoc.py <name> ...
    Show text documentation on something.  <name> may be the name of a
    Python keyword, topic, function, module, or package, or a dotted
    reference to a class or function within a module or module in a
    package.  If <name> contains a '/', it is used as the path to a
    Python source file to document. If name is 'keywords', 'topics',
    or 'modules', a listing of these things is displayed.

mydoc.py -k <keyword>
    Search for a keyword in the synopsis lines of all available modules.

mydoc.py -p <port>
    Start an HTTP server on the given port on the local machine.

mydoc.py -g
    Pop up a graphical interface for finding and serving documentation.

mydoc.py -w <name> ...
    Write out the HTML documentation for a module to a file in the current
    directory.  If <name> contains a '/', it is treated as a filename; if
    it names a directory, documentation is written for all the contents.

------ end of mydoc.py
```

###### markdown

[Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

https://raw.githubusercontent.com/adam-p/markdown-here/master/README.md

