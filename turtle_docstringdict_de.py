docsdict = {

'_Screen.bgcolor' :
        """Setzt/gibt zurück: die Hintergrundfarbe des Turtlegrafik-Fensters.
        ---        
        Optionale/s Argument/e: ein Farb-String oder drei Zahlen im 
	Bereich 0 .. colormode oder ein Tupel aus drei solchen Zahlen. 
        
        Beispiele (für ein TurtleScreen-Objekt namens screen):
        >>> screen.bgcolor("orange")
        >>> screen.bgcolor()
        'orange'
        >>> screen.bgcolor(0.5,0,0.5)
        >>> screen.bgcolor()
        '#800080'        
""",

'_Screen.bgpic' :
        """Setzt Hintergrundbild aus der gif-Datei picname / gibt picname zurück.

        Optionales Argument:
        picname -- Ein String, Name einer gif-Datei oder "nopic".
        
        Wenn picname ein Dateiname ist: setzt das entsprechende Hintergrundbild.
	Wenn picname "nopic" ist: entfernt das Hintergrundbild (sofern vorhanden).
	Wenn picname None ist: gibt den Dateinamen das aktuellen 
	Hintergrundbildes zurück
        
        Beispiel (für eine TurtleScreen namens screen):
        >>> screen.bgpic()
        'nopic'
        >>> screen.bgpic("landscape.gif")
        >>> screen.bgpic()
        'landscape.gif'
""",

'_Screen.bye' :
        """Schließt das Turtlegrafik-Fenster

        Beispiel (für eine TurtleScreen namens screen):
        >>> screen.bye()
""",

'_Screen.clearscreen' :
        """Löscht alle Zeichnungen und alle Turtles auf dem Turtlegrafik-Fenster.

        Alias-name: clearscreen | clear 

        Setzt leere TurtleScreen auf ihren Anfangszustand zurück: weißer
        Hintergrund, kein Hintergrundbild, keine Ereignis-Bindungen und
        tracing eingeschaltet. 
	
        Kein Argument.

        Beispiel (für eine TurtleScreen namens screen):
        >>> screen.clear()

        Anmerkung: Diese Methode it als Funktion nur unter dem
        Namen clearscreen() vorhanden.
""",

'_Screen.colormode' :
        """Gibt den colormode zurück oder setzt ihn auf 1.0 oder 255.
        
        Optionales Argument:
        cmode -- None oder einer der Werte 1.0 oder 255

        Die r, g, b - Werte von Farbtripeln müssen im Bereiche 0..cmode sein.

        Beispiel (für eine TurtleScreen namens screen):
        >>> screen.colormode()
        1.0
        >>> screen.colormode(255)
        >>> turtle.pencolor(240,160,80)
""",

'_Screen.delay' :
        """Setzt den delay-Wert für das Grafik-Update in Millisekunden.

        Optionales Argument:
        delay -- nicht negative ganze Zahl
        
        Der delay-Wert ist die Zeit zwischen zwei aufeinanderfolgenden 
	Grafik-Updates. Ohne Argument aufgerufen, gibt delay() den aktuellen 
	delay-Wert zurück.

        Beispiel (für eine TurtleScreen namens screen):
        >>> screen.delay(15)
        >>> screen.delay()
        15
""",

'_Screen.exitonclick' :
        """Startet mainloop() - beendet sie nach Mausklick.

        Kein Argument.

        Bindet bye() Method an das Mausklick-Ereignis auf die TurtleScreen.
        Wenn der Wert von "using_IDLE" - im Konfigurations-Dictionary False
        ist (Standard-Wert), wird mainloop() gestartet.
        Wenn die IDLE mit der -n Option verwendet wird (no subprocess),
        sollte dieser Wert in turtle.cfg auf True gesetzt werden. In diesem
        Fall ist IDLE's mainloop auch für das client-script aktiv.

        Dies ist eine Methode der _Screen-Klasse und des Screen()-Objekts
        und nicht verfügbar für TurtleScreen-Objekte.

        Beispiel (for das Screen()-Objekt namens screen):
        >>> screen.exitonclick()
""",

'_Screen.getcanvas' :
        """Gibt das Canvas-Objekt dieser TurtleScreen zurück.

        Kein Argument.

        Beispiel (für eine TurtleScreen namens screen):
        >>> cv = screen.getcanvas()
        >>> cv
        <turtle.ScrolledCanvas instance at 0x010742D8>
""",

'_Screen.getshapes' :
        """Gibt eine Liste aller aktuell verfügbaren Turtle-Shapes zurück.

        Kein Argument.
        
        Beispiel (für eine TurtleScreen namens screen):
        >>> screen.getshapes()
        ['arrow', 'blank', 'circle', ... , 'turtle']
""",

'_Screen.listen' :
        """Setzt den Focus auf das Turtle-Grafik-Fenster. 

        Kein  Argument.

        Der Focus wird auf das Grafik-Fenster gesetzt, um Tastatur-Ereignisse
        zu registrieren.
        Dummy Argumente sind angegeben, damit listen als Argument an
        die onclick-Methode übergeben werden kann.
        

        Beispiel (für eine TurtleScreen namens screen):
        >>> screen.listen()        
""",

'_Screen.mainloop' :
        """Startet die Ereignis-Schleife durch Aufruf der mainloop() Funktion von Tkinter.

        Kein Argument.

        Muuss die letzte Anweisung in einem Turtle-Grafik-Programm sein.
        Darf nicht verwendet werden, wenn ein script in der IDLE mit dem -n
        Schalter ausgeführt wird (No subprocess) - um Turtle-Grafik interaktiv
        zu verwenden.

        Beispiel (für eine TurtleScreen namens screen):
        >>> screen.mainloop()

        
""",

'_Screen.mode' :
        """Setzt den Turtle-Modus ('standard'/'logo'/'world') und führt reset() aus.

        Optionales Argument:
        mode -- eine der Zeichenketten 'standard', 'logo' oder 'world'
        
        Modus 'standard' ist kompatibel with turtle.py älterer Python Versionen (bis 2.5).
        Modus 'logo' ist kompatible mit der Turtlegrafik der meisten Logo-Implementationen.
        Modus 'world' verwendet benutzerdefinierte 'worldcoordinates'.
              *Achtung*: in diesem Modus erscheinen Winkel verzerrt, wenn das
              Verhältnis der Einheiten in x-/y-Richtung nicht gleich 1 ist.
        Wenn mode nicht angegeben ist, wird der aktuellen Turtle-Modus zurückgegeben.

             Modus    anfängliche Turtle-Orientierung     positive Winkel
         ------------|-------------------------------|----------------------   
          'standard'       nach rechts (Osten)         im Gegenuhrzeigersinn
            'logo'         nach oben   (Norden)        im Uhrzeiersinn

        Beispiel (für eine TurtleScreen namens screen):
        >>> mode('logo')   # setzt anfängliche Turtle-Orientierung nach Norden
        >>> mode()
        'logo'
""",

'_Screen.numinput' :
        """Öffne eine Dialog-Fenster für die Eingabe einer Zahl.
    
        Argumente:
        title -- String, der Titel des Dialogfensters.
        prompt -- String, Beschreibung der einzugebenden numerischen Größe.
        default: Standard-Wert für die einzugebende Größe
        minval: Minimaler Wert für die einzugebende Größe
        maxval: Maximaler Wert für die einzugebende Größe

        Die einzugebende Zahl muss im Bereich minval .. maxval liegen, wenn
        diese Werte angegeben sind. Wird eine Zahl eingegeben, die nicht in
        diesem Bereich liegt, wird ein entsprechender Hinweis ausgegeben
        und der Dialog bleibt offen.
        Die eingegebene Zahl wird zurückgegeben.
        Wenn der Dialog abgebrochen wird, wird None zurückgegeben.
        
        Beispiel:
        >>> numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)
""",

'_Screen.onkeypress' :
        """Bindet fun an das Ereignis: Drücken der Taste key.

        Argumente:
        fun -- Eine Funktion ohne Argumente 
        key -- ein String: Taste (z. B. "a") oder Tasten-Symbol (z. B. "space")

        Damit es Tastatur-Ereignisse registrieren kann, muss das
        Turtle-Grafik-Fenster den Fokus haben. (Siehe Methode listen())

        Beispiel (für eine TurtleScreen namens screen):

        >>> def f():
                fd(50)
                lt(60)

        >>> screen.onkeypress(f, "Up")
        >>> screen.listen()
        
        ### Subsequently the turtle can be moved by
        ### repeatedly pressing the up-arrow key, 
        ### consequently drawing a hexagon
""",

'_Screen.onkeyrelease' :
        """Bindet fun an das Ereignis: Loslassen der Taste key.

        Alias-Namen: onkeyrelease | onkey

        Argumente:
        fun -- Eine Funktion ohne Argumente 
        key -- ein String: Taste (z. B. "a") oder Tasten-Symbol (z. B. "space")

        Damit es Tastatur-Ereignisse registrieren kann, muss das
        Turtle-Grafik-Fenster den Fokus haben. (Siehe Methode listen())

        Beispiel (für eine TurtleScreen namens screen):

        >>> def f():
                fd(50)
                lt(60)

                
        >>> screen.onkey(f, "Up")
        >>> screen.listen()
        
        ### Subsequently the turtle can be moved by
        ### repeatedly pressing the up-arrow key, 
        ### consequently drawing a hexagon
""",

'_Screen.onscreenclick' :
        """Bindet fun an das Maus-Klick-Ereignis auf die Zeichenfläche.

        Alias-Namen: onscreenclick | onclick

        Argumente:
        fun -- Eine Funktion mit zwei Argumenten, den Koordinaten des
               angeklickten Punktes auf der Zeichenfläche.
        num -- Die nummer der Maustaste, Standardwert ist 1

        Beispiel (für eine TurtleScreen namens screen):

        >>> screen.onclick(goto)

        ### In der Folge bewirkt Klicken auf die Zeichenfläche, 
        ### dass die (anonyme) Turtle zu dem angeklickten Punkt bewegt wird.

        >>> screen.onclick(None)
        
        ### Ereignis-Bindung wird entfernt 
""",

'_Screen.ontimer' :
        """Installiere einen timer, der nach t Millisekunden fun aufruft.

        Argumente:
        fun -- Eine Function ohne Argumente.
        t -- eine Zahl >= 0

        Beispiel (für eine TurtleScreen mit Namen screen):

        >>> running = True
        >>> def f():
                if running:
                        fd(50)
                        lt(60)
                        screen.ontimer(f, 250)

        >>> f()   ### lässt die (anonyme) Turtle rundherum laufen
        >>> running = False           
        
""",

'_Screen.register_shape' :
        """Fügt eine Turtle-Shape zu der Shape-Liste des Turtle-Grafik-Fensters hinzu.

        Alias-Namen: register_shape | addshape

        Argumente:
        (1) Name ist der Name einer gif-Datei und shape ist None:
            Installiert das entsprechende Bild als Shape.
            !! Bild-Shapes werden NICHT mit der Turtle gedreht,
            !! daher zeigen sie nicht die orientierung der Turtle an.
        (2) Name ist ein beliebiger String und Shape ist ein Tupel
            von Koordinatenpaaren:
            Installiert die entsprechende Polygon-Shape
        (3) Name ist ein beliebiger String und shape ist ein
            (zusammengesetztes) Shape-Object:
            Installiert die entsprechende zusammengesetzte Shape.
            
        Shapes werden mit dem Aufruf shape(shapename) eingestellt.

        Aufruf: register_shape("turtle.gif")
        --oder: register_shape("tri", ((0,0), (10,10), (-10,10)))
        
        Beispiel (für eine TurtleScreen mit Namen screen):
        >>> screen.register_shape("triangle", ((5,-3),(0,5),(-5,-3)))
""",

'_Screen.resetscreen' :
        """Setzt alle Turtles auf der Zeichenfläche in den Anfangszustand zurück.

        Alias-Namen: resetscreen | reset

        Kein Argument.

        Beispiel (für eine TurtleScreen mit Namen screen):
        >>> screen.reset()
""",

'_Screen.screensize' :
        """Setze die Größe der Zeichenfläche des Turtlegrafik-Fensters.

        Optionale Argumente:
        canvwidth -- positive ganze Zahl, neue Breite der Zeichenfläche in Pixel
        canvheight --  positive ganze Zahl, neue Höhe der Zeichenfläche in Pixel
        bg -- Farb-String oder Farb-Tupel, neue Hintergrundfarbe
        Ohne Argumente: gibt die aktuellen Werte (canvaswidth, canvasheight) zurück

        Die Größe des Zeichenfensters wird nicht geändert. Um Teile der Zeichenfläche
        außerhalb des Fensters zu sehen, können die Bildlaufleisten verwendet werden.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.screensize(2000,1500)
            ### e. g. to search for an erroneously escaped turtle ;-)        
""",

'_Screen.setup' :
        """ Setze Größe und Position des Turtlegrafik-Fensters.

        Argumente:
        width: als ganze Zahl die Fensterbreite in Pixel, als Kommazahl
               der Bruchteil der Bildschirmbreite, den das Fenster einnimmt.
               Standarwert ist 50% der Bildschirmbreite.
        height: als ganze Zahl die Fensterhöhe in Pixel, als Kommazahl
               der Bruchteil der Bildschirmhöhe, den das Fenster einnimmt.
               Standarwert ist 75% der Bildschirmhöhe.
        startx: wenn positiv, Entfernung des Fensters vom linken Bildschirmrand
               in Pixel; wenn negativ, Entfernung vom rechten Bildschirmrand.
               Standarwert, startx=None, zentriert das Fenster horizontal.
        starty: wenn positiv, Entfernung des Fensters vomoberen Bildschirmrand
               in Pixel; wenn negativ, Entfernung vom unteren Bildschirmrand.
               Standarwert, starty=None, zentriert das Fenster vertikal.      

        Beispiele (für eine TurtleScreen mit Namen screen):
        >>> screen.setup (width=200, height=200, startx=0, starty=0)

        setzt Fentergröße auf 200x200 pixels, in der oberen linken
        Bildschirmecke.

        >>> screen.setup(width=.75, height=0.5, startx=None, starty=None)

        Setzt die Fenstergröße auf 75% der Bildschirmbreite und 50%
        der Bildschirmhöhe und zentriert das Fenster auf dem Bildschirm.        
""",

'_Screen.setworldcoordinates' :
        """Installiert ein benutzerdefiniertes ('Welt-')Koordinatensystem. 

        Argumente:
        llx -- ein Zahl. x-Koordinate der linken unteren Ecke der Zeichenfläche
        lly -- ein Zahl. y-Koordinate der linken unteren Ecke der Zeichenfläche
        urx -- ein Zahl. x-Koordinate der oberen rechten Ecke der Zeichenfläche
        ury -- ein Zahl. x-Koordinate der oberen rechten Ecke der Zeichenfläche

        Richtet ein benutzerdefinierte Koordinatensystem ein und schaltet auf
        den Modus 'world' um, falls nötig. Das führt ein screen.reset() aus.
        Wenn der Modus 'world' bereits aktiv ist, werden alle Zeichnungen mit
        dem neuen Koordinatensystem neu gezeichnet.

        ACHTUNG: in benutzerdefinierte Koordinatensystemen können Winkel
        verzerrt aussehen. (Siehe auch: Screen().mode())

        Beispiel (für eine TurtleScreen mit Namen screen):
        >>> screen.setworldcoordinates(-10,-0.5,50,1.5)
        >>> for _ in range(36):
                left(10)
                forward(0.5)
""",

'_Screen.textinput' :
        """Öffne eine Dialog-Fenster für die Eingabe eines Strings.
    
        Argumente:
        title -- String, der Titel des Dialogfensters.
        prompt -- String, Beschreibung der einzugebenden Information.

        Der eingegebene String wird zurückgegeben.
        Wenn der Dialog abgebrochen wird, wird None zurückgegeben.
        
        Beispiel:
        >>> textinput("NIM", "Name of first player:")
""",

'_Screen.title' :
        """Setzt den Titel des Turtle-Grafik-Fensters.

        Argument:
        titlestring -- ein String, der im Titelbalken des Grafik-Fensters
                       angezeigt wird.

        Das ist eine Methode des Screen()-Objekts. Nicht verfügbar für TurtleScreen-
        Objecte.

        Beispiel (für das Screen()-Objekt namens screen):
        >>> screen.title("Willkommen zum Schildkröten-Zoo!")
""",

'_Screen.tracer' :
        """tracer() dreht Turtle-Animation an/ab und setzt Grafik-Update-Verzögerung.

        Optionale Argumente:
        n -- nichtnegative ganze Zahl
        delay -- nichtnegative ganze Zahl
        
        If n angegeben ist, wird nur jedes n.te reguläre Screen-Update
        ausgeführt. (Dies kann verwendet werden um die Zeichnung komplexer
        Grafiken zu beschleunigen. Zum delay-Argument: siehe _Screen.delay())

        Beispiel (für eine TurtleScreen mit Namen screen):
        >>> screen.tracer(8, 25)
        >>> dist = 2
        >>> for i in range(200):
                fd(dist)
                rt(90)
                dist += 2        
""",

'_Screen.turtles' :
        """Gibt eine Liste der Turtles auf der Zeichenfläche zurück.

        Beispiel (für eine TurtleScreen mit Namen screen):
        >>> screen.turtles()
        [<turtle.Turtle object at 0x00E11FB0>]        
""",

'_Screen.update' :
        """Perform a TurtleScreen update.

        Kein Argument.
        
        Beispiel (für eine TurtleScreen mit Namen screen):
        >>> screen.update()
""",

'_Screen.window_height' :
        """ Gibt die Höhe des Turtlegrafik-Fensters zurück.

        Beispiel (für eine TurtleScreen mit Namen screen):
        >>> screen.window_height()
        480
        
""",

'_Screen.window_width' :
        """Gibt die Breite des Turtlegrafik-Fensters zurück.

        Kein Argument.

        Beispiel (für eine TurtleScreen mit Namen screen):
        >>> screen.window_width()
        640
        
""",

'Turtle.back' :
        """Bewegt die Turtle um distance rückwärts.

        Alias-Namen: back | backward | bk

        Argument:
        distance -- eine Zahl

        
        Bewegung rückwärts heißt, in die Richtung, die der
        Orientierung der Turtle entgegengesetzt ist.
        Die Ausrichtung der Turtle ändert sich dabei nicht.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
""",

'Turtle.begin_fill' :
        """Beginnt das Zeichnen einer Figur, die gefüllt werden soll.

        Kein Argument.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.begin_fill()
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.end_fill()
""",

'Turtle.begin_poly' :
        """Beginnt die Aufzeichnung der Eckpunkte eines Polygons.

	Die Eckpunkte werden in einer Punktliste gesammelt.
	Die aktuelle Turtleposition ist der erste Eckpunkt des
	Polygons. (Siehe auch: end_poly() und get_poly()
	
	Kein Argument.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.begin_poly()
""",

'Turtle.circle' :
        """ Zeichnet Kreis mit gegebenem Radius.

        Argumente:
        radius -- eine Zahl
        extent (optional) -- eine Zahl (Winkel-Bereich)
        steps (optional) -- eine ganze Zahl (Schrittanzahl)

	Der Kreismittelpunkt ist radius Einheiten links von der
	Turtle; der Winkel extent gibt an, welcher Teil des
	Kreises gezeichnet wird. Wenn extent fehlt, wird (als
	Voreinstellung) ein voller Kreis gezeichnet.
        
	Wenn extent kein voller Kreis ist, dann ist ein Endpunkt
	des Bogens die aktuelle Turtle-Position. Wenn der Radius
	positiv ist, wird der Bogen im Gegenuhrzeigersinn gezeichnet.
	Für negative Radien wird der wird der Bogen im Uhrzeigersinn
	gezeichnet. Nachdem Zeichnen des Bogens ist die Orientierung
	der Turtle um extent geändert.
        
	Da der Kreis durch ein eingeschriebenes reguläres Polygon
	angenähert wird, bestimmt steps die Anzahl der Schritte, die
	dafür verwendet wird. Wenn steps nicht angegeben wird, wird
	ein automatisch ermittelter Wert verwendet. Kann verwendet
	werden um gleichseitige Vielecke zu zeichnen.

        Aufruf: circle(radius)                  # voller Kreis
        --oder: circle(radius, extent)          # Bogen
        --oder: circle(radius, extent, steps)
        --oder: circle(radius, steps=6)         # regelmäßiges Sechseck

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.circle(50)
        >>> turtle.circle(120, 180)  # Halbkreis
""",

'Turtle.clear' :
        """Löscht die Zeichnungen der Turtle. Die Turtle wird nicht bewegt.

        Kein Argument.

        Löscht die Zeichnungen der Turtle vom Grafikfenster.
        Zustand und Position der Turtle bleiben ungeändert, ebenso
        wie die Zeichnungen anderer Turtles. 

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.clear()
""",

'Turtle.clearstamp' :
        """Löscht den Stempelabdruck mit der Kennung stampid.

        Argument:
        stampid - ganze Zahl, muss der Rückgabewert eines früheren
                  stamp() Aufrufes sein.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.color("blue")
        >>> astamp = turtle.stamp()
        >>> turtle.fd(50)
        >>> turtle.clearstamp(astamp)
        
""",

'Turtle.clearstamps' :
        """Lösche alle oder n der vorhandenen Stempelabdrucke der Turtle.

        Optionales Argument:
        n -- ganze Zahl

        Wenn n gleich None ist: löscht alle Stempelabdrucke der Turtle,
        Wenn n > 0 ist: löscht die ersten n Stempelabdrucke.
        Wenn n < 0 ist: löscht die n zuletzt erzeugten Stempelabdrucke.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> for i in range(8):
                turtle.stamp(); turtle.fd(30)
        ...
        >>> turtle.clearstamps(2)
        >>> turtle.clearstamps(-2)
        >>> turtle.clearstamps()
""",

'Turtle.clone' :
        """Erzeugt einen Klon der Turtle und gibt ihn zurück.

        Kein Argument.

        Erzeugt einen Klon der Turtle, ein neues Turtle-Objekt mit der
        gleichen Position, Orientierung und den gleichen Eigenschaften.

        Beispiel (für eine Turtle namens mick):
        mick = Turtle()
        joe = mick.clone()
""",

'Turtle.color' :
        """Setzt oder gibt zurück: die Zeichenstiftfarbe und die Füllfarbe.

        Argumente:
        Es sind mehrere Formate für die Argumente erlaubt:
        Sie verwenden 0, 1, 2, oder 3 Argumente wie folgt:

        color()
            Gibt die aktuellen Werte der Zeichenstiftfarbe und Füllfarbe
            als ein Paar von Farbbeschreibungs-Strings zurück, wie sie von
            pencolor() und fillcolor() zurückggeben werden.
        color(colorstring), color((r,g,b)), color(r,g,b)
            Argumente wie bei pencolor(), setzt sowohl die Zeichenstiftfarbe
            wie auch die Füllfarbe auf den angegebenen Wert.
        color(colorstring1, colorstring2),
        color((r1,g1,b1), (r2,g2,b2))
            gleichwertig mit pencolor(colorstring1) und fillcolor(colorstring2)
            and analog, wenn das andere Format für die Agumente verwendet wird.

        Wenn die Turtle-Shape ein Polygon ist, wird der Umriss und das Innere
        des Polygons mit den angegebenen Farben dargestellt.
        Weitere Informationen bei: pencolor(), fillcolor()

        Beispiel (für ein Turtle-Objekt namens turtle):        
        >>> turtle.color('red', 'green')
        >>> turtle.color()
        ('red', 'green')
        >>> colormode(255)
        >>> color((40, 80, 120), (160, 200, 240))
        >>> color()
        ('#285078', '#a0c8f0')        
""",

'Turtle.degrees' :
        """Setze Einheit für die Winkelmessung auf Grad.

	Optionales Argument:
	fullcircle -- eine Zahl (Standardwert ist 360.0)
        
        Setzt die Einheit für die Winkelmessung, d. h. die Anzahl
        der Grade eines Vollkreises. Standardwert ist 360 Grad.
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.left(90)
        >>> turtle.heading()
        90
        >>> turtle.degrees(400.0)  # angle measurement in gon
        >>> turtle.heading()
        100        
""",

'Turtle.distance' :
        """Gib die Entfernung der Turtle von (x,y) zurück.

        Argumente:
        x -- eine Zahl oder ein Paar/Vektor von Zahlen oder eine Turtle
        y -- eine Zahl oder None 

        Aufruf: distance(x, y)         # Zwei Koordinaten
        --oder: distance((x, y))       # Ein Paar (Tupel) von Koordinaten
        --oder: distance(vec)          # z. B. ein Rückgabewert von pos()
        --oder: distance(mypen)        # wobei mypen eine andere Turtle ist
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.pos()
        (0.00, 0.00)
        >>> turtle.distance(30,40)
        50.0
        >>> pen = Turtle()
        >>> pen.forward(77)
        >>> turtle.distance(pen)
        77.0
""",

'Turtle.dot' :
        """Zeichnet einen Punkt mit Durchmesser size in der Farbe color

        Optionale Argumente:
        size -- eine Zahl >= 1 
        color -- Farbstring oder ein numerisches Farbtupel

        Zeichnet kreisförmigen Punkt mit Durchmesser size in der Farbe color.
	Wenn die Farbe nicht angegeben wird, wird  die Turtle-Farbe verwendet.
	Wenn auch size nicht angegeben wird, wird pensize()+4 verwendet.
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        
        >>> turtle.dot()
        >>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)     
""",

'Turtle.end_fill' :
        """Füllt die Figur, die seit dem letzten begin_fill() gezeichnet wurde..

        Kein Argument.
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.begin_fill()
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.end_fill()      
""",

'Turtle.end_poly' :
        """Beendet die Aufzeichnung der Eckpunkte eines Polygons.

        Kein Argument.

        Die aktuelle Turtle-Position ist der letzte Punkt des Polygons.
        Dieser wird mit dem ersten Punkt verbunden.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.end_poly()        
""",

'Turtle.fillcolor' :
        """Setzt die Füllfarbe oder gibt sie zurück.

        Argumente:
        Vier Formate für die Argumente sind möglich:
          - fillcolor()
            Gibt die aktuelle Füllfarbe zurück als Farbbeschreibungs-String,
            möglicherweise im Hexadezimal-Format (siehe Beispiel).
            Kann als Argument für andere color/pencolor/fillcolor Aufrufe
            verwendet werden.
          - fillcolor(colorstring)
            s ist ein Tkinter-Farbstring, wie z. B. "red" oder "yellow"
          - fillcolor((r, g, b))
            *ein Tuplel* von r, g und b Werten, die eine RGB-Farbe darstellen.
            Jede der Werte r, g und b ist aus dem Bereich 0..colormode,
            wobei colormode entweder 1.0 oder 255 ist.
          - fillcolor(r, g, b)
            r, g und b stellen eine RGB-Farbe mit Werten im Bereich 0..colormode dar.

        Wenn die Turtle-Shape ein Polygon ist, wird das Innere
        des Polygons mit der angegebenen Farbe dargestellt.
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.fillcolor('violet')
        >>> col = turtle.pencolor()
        >>> turtle.fillcolor(col)
        >>> turtle.fillcolor(0, .5, 0)
""",

'Turtle.filling' :
        """Gibt aktuellen Füll-Zustand zurück (True oder False).
    
        Kein Argument.

        Gibt True zurück, wenn Füllen eingeschaltet ist, d. h.
        nach einem begin_fill() - Aufruf, und False sonst.
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.begin_fill()
        >>> if turtle.filling():
                turtle.pensize(5)
        else:
                turtle.pensize(3)
""",

'Turtle.forward' :
        """Bewegt die Turtle um distance nach vorne.

        Alias-Namen: forward | fd

        Argument:
        distance -- eine Zahl (ganze Zahl oder Gleitkommazahl)

        Bewege die Turtle um distance nach vorne,
        in Richtung der Orientierung der Turtle.

        Beispiel (für ein Turtle-Objekt namens turtle):        
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)
""",

'Turtle.get_poly' :
        """Gibt das zuletzt aufgezeichnete Polygon zurück.

        Kein Argument.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> p = turtle.get_poly()
        >>> turtle.register_shape("meineLieblingsShape", p)
""",

'Turtle.getscreen' :
        """Gibt das Screen()-Objekt zurück, auf dem die Turtle zeichnet.

        Kein Argument.

        Gibt das TurtleScreen()-Objekt zurück, auf dem die Turtle zeichnet.
        Für diese Objekt können dann die Screen-Methoden aufgerufen werden.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> ts = turtle.getscreen()
        >>> ts
        <turtle.TurtleScreen object at 0x0106B770>
        >>> ts.bgcolor("pink")        
""",

'Turtle.get_shapepoly':
        """Gib das Polygon der aktuellen transformierten Turtleform zurück.

        Kein Argument.

        Gib das Polygon der aktuellen transformierten Turtleform zurück,
        das ist das Polygon, das der Darstellung der Turtle auf dem
        Bildschirm, gestreckt, verdreht, geschert, entspricht.
        
        Examples:
        >>> shape("square")
        >>> shapetransform(4, -1, 0, 2)
        >>> get_shapepoly()
        ((50, -20), (30, 20), (-50, 20), (-30, -20))
""",

'Turtle.getturtle' :
        """Gibt das Turtle-Objekt selbst zurück.

        Alias-Namen: getturtle | getpen

        Kein Argument.
        
        Einzige sinnvolle Verwendung: als Funktion, die
        die 'anonyme Turtle' zurück gibt.
        
        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <turtle.Turtle object at 0x0187D810>
        >>> turtles()
        [<turtle.Turtle object at 0x0187D810>]
""",

'Turtle.goto' :
        """Bewegt die Turtle zum Punkt mit absoluten Koordinaten (x,y).

        Alias-Namen: goto | setpos | setposition
        
        Argumente:
        x -- eine Zahl     oder ein Paar/Vektor von Zahlen
        y -- eine Zahl     oder None
        
        Aufruf: goto(x, y)    # zwei Koordinaten
        --oder: goto((x, y))  # ein Paar von  Koordinaten
        --oder: goto(vec2D)   # wie z. B. von pos() zurückgegeben.
        
	Bewegt die Turtle zum Punkt mit absoluten Koordinaten (x,y).
        Wenn die Feder unten ist, wird eine Strecke gezeichnet.
	Die Orientierung der Turtle wird nicht geändert.

        Beispiele (für ein Turtle-Objekt namens turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.goto((20,80))
        >>> turtle.position()
        (20.00,80.00)
        >>> turtle.setposition(tp)
        >>> turtle.pos()
        (0.00,0.00)
""",

'Turtle.heading' :
        """Gib die aktuelle Orientierung der Turtle zurück.

        Kein Argument.
        
        Die Orientierung ist der Winkel zwischen der Richtung,
        in die die Turtle schaut und der Startausrichtung der
        Turtle.
        Im Modus 'standard' ist die Startausrichting 'ost' und
        positive Winkel werden im Gegenuhrzeigesinn gemessen.
        Im Modus 'logo' ist die Startausrichting 'nord' und
        positive Winkel werden im Uhrzeigesinn gemessen.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.left(67)
        >>> turtle.heading()
        67.0        
""",

'Turtle.hideturtle' :
        """Macht die Turtle unsichtbar.

        Alias-Namen: hideturtle | ht

        Kein Argument.

	Es ist oft sinnvoll, dies während der Erstellung komplizierter
	Grafiken zu verwenden, weil das Verstecken der Turtle die
	Geschwindigkeit des Zeichenvoprgangs merkbar erhöht.
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        
        >>> turtle.hideturtle()        
""",

'Turtle.home' :
        """Bewegt die Turtle zu ihrer Ursprungsposition (0, 0).        
        Kein Argument.

        Bewegt die Turtle zu ihrer Ursprungsposition mit den
        Koordinaten (0, 0) und setzt ihre Orientierung auf die
        Anfangsorientierung (die vom mode abhängt.)
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.home()     
""",

'Turtle.isdown' :
        """Gibt True zurück, wenn Zeichenstift unten, False wenn er oben ist.

        Alias-Namen: isdown | pendownp
        
        Kein Argument.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.penup()
        >>> turtle.isdown()
        False
        >>> turtle.pendown()
        >>> turtle.isdown()
        True        
""",

'Turtle.isvisible' :
        """Gibt True zurück, wenn die Turtle sichtbar ist, False sonst.

        Alias-Namen: isvisible | shownp
        
        Kein Argument.
        
        Beispiel (für ein Turtle-Objekt namens turtle):

        >>> turtle.hideturtle()
        >>> if not turtle.isvisible():
                print "Turtle ist unsichtbar!"
                
        Turtle ist unsichtbar!
""",

'Turtle.left' :
        """Dreht die Turtle um angle Winkeleinheiten nach links.

        Alias-Namen: left | lt
        
        Argument:
        angle -- eine Zahl (ganze Zahl oder Gleitkommazahl)

        Dreht die Turtle um angle Winkeleinheiten nach links.
        (Voreingestellte Winkeleinheit ist Grad; das kann mit
        den Funktionen degrees() und radians() geändert werden.)
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0        
""",

'Turtle.onclick' :
        """Bindet fun an das Maus-Klick-Ereignis auf diese Turtle.

        Argumente:
        fun -- Eine Funktion mit zwei Argumenten, den Koordinaten des
               angeklickten Punktes auf der Zeichenfläche.
        num -- Die Nummer der Maustaste, Standardwert ist 1
        add -- True or False. Wenn True, wird die neue Bindung hinzugefügt,
               andernfalls ersetzt sie die frühere Bindung.

        Beispiel für die anonyme Turtle, d. h. prozeudralen Programmierstil:

        >>> def turn(x, y):
                left(360)
                
        >>> onclick(turn)  # Klicken auf die Turtle wird sie nun drehen
        >>> onclick(None)  # Ereignisbindung wird aufgehoben
""",

'Turtle.ondrag' :
        """Bindet fun an das Ziehen dieser Turtle mit gedrückter Maustaste.

        Argumente:
        fun -- Eine Funktion mit zwei Argumenten, den Koordinaten des
               angeklickten Punktes auf der Zeichenfläche.
        num -- Die Nummer der Maustaste, Standardwert ist 1

        Vor jedem 'drag'-Ereignis tritt ein Klick-Ereignis auf die Turtle ein.
        ACHTUNG: speed(0) verwenden - andernfalls bewegt sich die Turtle
                 zu langsam.
        ACHTUNG: Rekusionsgrenze hinaufsetzen! (Andernfalls droht Überlauf des
                 Recursions-Stacks.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> import sys
        >>> sys.setrecursionlimit(20000)
        >>> turtle.speed(0)
        >>> turtle.ondrag(turtle.goto)

        ### Subsequently clicking and dragging a Turtle will
        ### move it across the screen thereby producing handdrawings
        ### (if pen is down).
""",

'Turtle.onrelease' :
        """Bindet fun an das Loslassen eines Mausknopfes auf diese Turtle.

        Argumente:
        fun -- Eine Funktion mit zwei Argumenten, den Koordinaten des
               angeklickten Punktes auf der Zeichenfläche.
        num -- Die Nummer der Maustaste, Standardwert ist 1

        Example (for a MyTurtle instance named joe):
        >>> class MyTurtle(Turtle):
                def glow(self,x,y):
                        self.fillcolor("red")
                def unglow(self,x,y):
                        self.fillcolor("")
                        
        >>> joe = MyTurtle()
        >>> joe.onclick(joe.glow)
        >>> joe.onrelease(joe.unglow)
        ### clicking on joe turns fillcolor red,
        ### unclicking turns it to transparent.
        
""",

'Turtle.pen' :
        """Setzt/gibt zurück: die Eigenschaften des Zeichenstiftes.

        Argumente:
            pen -- Ein dictionary mit einigen oder allen der unten angegebenen
                   Schlüssel
            **pendict -- kein, ein oder mehrere Schlüsselwort-Argumente mit den
                   unten angegebenen Schlüsseln.

	Setzt/gibt zurück: die Eigenschaften des Zeichenstiftes. in einem
	pen-Dictionary mit folgende Schlüssel/Wert-Paaren:
           "shown"      :   True/False
           "pendown"    :   True/False
           "pencolor"   :   Farb-String oder Farb-Tupel
           "fillcolor"  :   Farb-String or Farb-Tupel
           "pensize"    :   positive Zahl
           "speed"      :   Zahl im Bereich 0..10
           "resizemode" :   "auto" oder "user" oder "noresize"
           "stretchfactor": positive Zahl
           "outline"    :   positive Zahl
           "stretchfactor" : (Zahl, Zahl) (beide nicht Null)
           "tilt"       :   Zahl
           "shearfactor":   Zahl 
           
        Dieses Dictionary kann als Argument für nachfolgende pen()-
	Aufrufe verwendet werden um einen früheren pen-Zustand wieder
	herzustellen. Mit Schlüsselwort-Argumenten können mehrere
	Turtle-Eigenschaften in einem Statement gesetzt werden.
	
        Beispiele (für ein Turtle-Objekt namens turtle):
        
        >>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
        >>> turtle.pen()
        {'pensize': 10, 'resizemode': 'auto', 'pendown': True, 'fillcolor': 'black',
        'speed': 3, 'shown': True, 'outline': 1, 'tilt': 0.0, 'pencolor': 'red',
        'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0}
        >>> penstate=turtle.pen()
        >>> turtle.color("yellow","")
        >>> turtle.penup()
        >>> turtle.pen()
        {'pensize': 10, 'resizemode': 'auto', 'pendown': True, 'fillcolor': '',
        'speed': 3, 'shown': True, 'outline': 1, 'tilt': 0.0, 'pencolor': 'yellow',
        'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0}
        >>> turtle.pen(penstate, fillcolor="green")
        >>> turtle.pen()
        {'pensize': 10, 'resizemode': 'auto', 'pendown': True, 'fillcolor': 'green',
        'speed': 3, 'shown': True, 'outline': 1, 'tilt': 0.0, 'pencolor': 'red',
        'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0}
""",

'Turtle.pencolor' :
        """Setzt die Zeichenstiftfarbe oder gibt sie zurück.

        Argumente:
        Vier Formate für die Argumente sind möglich:
          - pencolor()
            Gibt die aktuelle Zeichenstiftfarbe zurück als Farbbeschreibungs-String,
            möglicherweise im Hexadezimal-Format (siehe Beispiel).
            Kann als Argument für andere color/pencolor/fillcolor Aufrufe
            verwendet werden.
          - pencolor(colorstring)
            s ist ein Tkinter-Farbstring, wie z. B. "red" oder "yellow"
          - pencolor((r, g, b))
            *ein Tuplel* von r, g und b Werten, die eine RGB-Farbe darstellen.
            Jede der Werte r, g und b ist aus dem Bereich 0..colormode,
            wobei colormode entweder 1.0 oder 255 ist.
          - pencolor(r, g, b)
            r, g und b stellen eine RGB-Farbe mit Werten im Bereich 0..colormode dar.

        Wenn die Turtle-Shape ein Polygon ist, wird der Umriss 
        des Polygons mit der angegebenen Farbe dargestellt.
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.pencolor('brown')
        >>> tup = (0.2, 0.8, 0.55)
        >>> turtle.pencolor(tup)
        >>> turtle.pencolor()
        '#33cc8c'    
""",

'Turtle.pendown' :
        """Senkt den Zeichenstift -- zeichnet bei Bewegungen.

        Alias-Namen: pendown | pd | down

        Kein Argument.
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.pendown()
""",

'Turtle.pensize' :
        """Setzt die Strichdicke des Zeichenstifts oder gibt sie zurück.

        Alias-Namen: pensize | width

        Argument:
        width -- eine positive Zahl
        
	Setzt die Strichdicke des Zeichenstifts oder gibt sie zurück.
	Wenn resizemode auf 'auto' gestellt ist und die Turtleshape
	ein Polygon ist, wird das Polygon mit derselben Strichdicke
	dargestellt.
        
        Beispiel (für ein Turtle-Objekt namens turtle):        
        >>> turtle.pensize()
        1
        turtle.pensize(10)  # von hier weg werden Linien mit
                            # Strichdicke 10 Pixel gezeichnet.       
""",

'Turtle.penup' :
        """Hebt den Zeichenstift an -- zeichnet bei Bewegungen NICHT.

        Alias-Namen: penup | pu | up
        
        Kein Argument
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.penup()
""",

'Turtle.position' :
        """Gibt die aktuelle Position der Turtle als Vektor zurück.

        Alias-Namen: position | pos

        Kein Argument.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.pos()
        (0.00, 240.00)
""",

'Turtle.radians' :
        """ Setzt die Maßeinheit für die Winkelmessung auf radians.

        Kein Argument.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.heading()   
        90
        >>> turtle.radians()
        >>> turtle.heading()
        1.5707963267948966
""",

'Turtle.reset' :
        """Versetzt Turtle in Anfangszustand und löscht ihre Zeichnungen.

        Kein Argument.

        Versetzt die Turtle in Anfangszustand und löscht ihre Zeichnungen.
        Genauer: Genauer: setzt die Turtle in den Mittelpunkt des Fensters
        und alle Attribute auf ihre Anfangswerte (mit Ausnahme der Turtleform). 

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.position()
        (0.00,-22.00)
        >>> turtle.heading()
        100.0
        >>> turtle.reset()
        >>> turtle.position()
        (0.00,0.00)
        >>> turtle.heading()
        0.0        
""",

'Turtle.resizemode' :
        """Setzt den resize-Modus oder gibt ihn zurück.

        Argument(optionale): Eine der Zeichenketten "auto", "user", "noresize"

	Die verschiedenen resize-Modi haben folgende Wirkung:
          - "auto": passt die Größe der Turtle automatisch an den Wert
	            von pensize an.
          - "user": Darstellung der Turtle wird durch die Werte von
	            stretchfactor und outlinewidth (outline) festgelegt.
	            Diese werden durch die Funktion/Methode shapesize() gesetzt.
          - "noresize" es findet keine Anpassung der Turtle-Darstellung statt.
        
        Aufruf: resizemode("user") # zum Beispiel
        --oder: resizemode()

        Beispiel (für ein Turtle-Objekt namens turtle):
        
        >>> turtle.resizemode("noresize")
        >>> turtle.resizemode()
        'noresize'        
""",

'Turtle.right' :
        """Dreht die Turtle um angle Winkeleinheiten nach rechts.

        Alias-Namen: right | rt
        
        Argument:
        angle -- eine Zahl (ganze Zahl oder Gleitkommazahl)

        Dreht die Turtle um angle Winkeleinheiten nach rechts.
        (Voreingestellte Winkeleinheit ist Grad; das kann mit
        den Funktionen degrees() und radians() geändert werden.)
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0        
""",

'Turtle.setheading' :
        """Orientiert die Turtle in Richtung to_angle.

        Alias-Namen: sethaeding | seth

        Argument:
        to_angle -- ein Zahl
        
        Orientiert die Turtle in Richtung to_angle.
        Die Orientierung erfolgt unter Berücksichtigung
        des eingestellten Modus. (Siehe mode()).
        Hier sind einige gebräuchliche Richtungen in Grad:
        
         standard - Modus:       logo-Modus:                  
        -------------------|--------------------
            0 - ost                0 - nord
           90 - nord              90 - ost
          180 - west             180 - süd
          270 - süd              270 - west
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90      
""",

'Turtle.settiltangle' :
        """Dreht die Turtleform in die angegebene Richtung.

        Optionales Argument:
        angle -- Zahl

        Dreht die Turtleform *in* die durch den Winkel angegebene
        Richtung. Ändert NICHT die Orientierung der Turtle, d. h.
        ihre Bewegungsrichtung.
              
        Beispiele (für eine Turtle namens turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.settiltangle(45)
	>>> stamp()
        >>> turtle.fd(50)
        >>> turtle.settiltangle(-45)
	>>> stamp()
        >>> turtle.fd(50)
        
""",

'Turtle.setundobuffer' :
        """Setzt den die Größe des undo-Speichers oder schaltet ihn aus.

        Argument:
        size -- ganze Zahl oder None

        Wenn size eine ganze Zahl ist wird ein leerer undo-Puffer der
        angegebenen Größe installiert. Size gibt die Maximalanzahl der
        Turtle-Befehle an, die mit undo() rückgängig gemacht werden
        können.
        Wenn size None ist, arbeitet die Turtle ohne undo-Speicher.
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.setundobuffer(42)        
        
""",

'Turtle.setx' :
        """Setzt die erste Koordinate der Turtle auf x.

        Argument:
        x -- eine Zahl

        Setzt die erste Koordinate der Turtle auf x, lässt die zweite
        Koordinate ungeändert. Die Bewegung erfolgt daher in x-Richtung.
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.position()
        (0.00, 240.00)
        >>> turtle.setx(10)
        >>> turtle.position()
        (10.00, 240.00)
        
""",

'Turtle.sety' :
        """Setzt die zweite Koordinate der Turtle auf y.

        Argument:
        y -- eine Zahl

        Setzt die zweite Koordinate der Turtle auf y, lässt die erste
        Koordinate ungeändert. Die Bewegung erfolgt daher in y-Richtung.
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.position()
        (0.00, 240.00)
        >>> turtle.setx(10)
        >>> turtle.position()
        (10.00, 240.00)
        
""",

'Turtle.shape' :
        """Setzt die Turtleform auf name oder gibt ihren Namen zurück.
        
        (Optionales) Argument:
        name -- String

        Name einer Turtleform aus dem Turtle-Dictionry.
           Dieses kann mit getshapes() abgefragt werden.

        Setzt die Turtleform auf name oder gibt den Namen der Turtleform
        zurück. Die mit name bezeichnete Turtleform muss in dem
        shape-Dictionary von TurtleScreen existieren. Anfänglich gibt es
        sechs Polygon-Formen: 'arrow', 'turtle', 'circle'. 'square',
        'triangle', 'classic' und dazu 'blank' als leeres Bild.
        Siehe auch: register_shape()
	
        Beispiel (für ein Turtle-Objekt namens turtle):
        
        >>> turtle.shape()
        'arrow'
        >>> getshapes()
        ['arrow', 'blank', 'circle', 'square', 'triangle', 'turtle']
        >>> turtle.shape("turtle")
        >>> shape()
        'turtle'        
""",

'Turtle.shapesize' :
        """Setzt/gibt zurück: Streckungsfaktoren und Umrissliniendicke.

        Alias-Namen: shapesize | turtlesize

        Optinonale Argumente:
        stretch_wid : positive Zahl
        stretch_len : positive Zahl
           outline  : positive Zahl

        Setzt die Streckungsfaktoren in x- bzw. y-Richtung
        und die Dicke der Umrisslinie. Setzt resizemode auf "user".
        Daher wird die Turtle entsprechend diesen Werten dargestellt:
        stretch_wid ist der Streckungsfaktor senkrecht zur Orientierung
        stretch_len ist der Streckungsfaktor in Richtung der Orientierung
                    der Turtle
        outline     legt die Dicke der Umrisslinie der Turtle fest.
           
        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("user")
        >>> turtle.shapesize(5, 5, 12)
        >>> turtle.shapesize(outline=8)
""",

'Turtle.shapetransform' :
        """Setze/Gib zurück die Transformations-Matrix für die Turtleform.
    
        Optionale Argumente:
        t11, t12, t21, t22 -- Zahlen.

        Wenn kein Matrix-Element angegeben wird, wird die Transformations-
        Matrix zurück gegeben.
        Andernfalls werden die angegebenen Elemente gesetzt und die
        Turtleform entsprechend der neuen Matrix dargestellt, mit der
        ersten Zeile t11, t12 und der zweiten Zeile t21, t22.
        Streckungsfaktor, Verdrehungswinkel und Scherungsfaktor werden
        entsprechend angepasst.
    
        Beispiele:
        >>> shape("square")
        >>> shapesize(4,2)
        >>> shearfactor(-0.5)
        >>> shapetransform()
        >>> (4.0, -1.0, -0.0, 2.0)
""",

'Turtle.shearfactor':
        """    Set or return the current shearfactor.
    
        Optionales Argument:
        shear -- Zahl, der Tangens des Scherungswinkels.
        
        Schert die Turtleform entsprechend dem angegebenen Scherungsfaktor.
        Der Scherungsfaktor ist der Tangens des Scherungswinkels. Das
        ist jener Winkel, um den Linien parallel zur Orientierung der
        Turtle gedreht werden.        
        Die Orientierung (Bewegungsrichtung) der Turtle wird nicht
        geändert.
        Wenn der Scherungsfaktor nicht angegeben ist, wird der aktuelle
        Scherungsfaktor zurückgegeben.

        Examples:
        >>> shape("circle")
        >>> shapesize(5,2)
        >>> shearfactor(0.5)
        >>> shearfactor()
        >>> 0.5
""",

'Turtle.showturtle' :
        """Macht die Turtle sichtbar.

        Alias-Namen: showturtle | st

        Kein Argument.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> turtle.hideturtle()
        >>> turtle.showturtle()
        
""",

'Turtle.speed' :
        """Setzt/gibt zurück: Bewegungsgeschwindigkeit der Turtle (0 .. 10)

        Optionales Argument:
        speed -- ganze Zahl im Bereich 0 .. 10 (oder ein Strung, s. u.)

        Setzt die Geschwindigkeit für die Animation der Turtle auf einen
        ganzzahligen Wert im Bereich 0 .. 10.
        Wenn kein Argument angegeben ist, wird die aktuelle Geschwindigkeit
        zurückgegeben.
        
        Wenn das Argument eine Zahl größer als 10 oder kleiner als 0.5
	ist, wird speed auf 0 gesetzt.
	speed kann auch einer der folgenden fünf Strings sein, die wie
	angegeben den Zahlenwerten von speed entsprechen:
            'fastest' :  0
            'fast'    :  10
            'normal'  :  6 
            'slow'    :  3
            'slowest' :  1
	Werte von speed im Bereich von 1 bis 10 bewirken eine zunehmend 
	schnellere Animation der Turtle-Bewegung (auch der Drehung).
        ***************
        speed = 0 : *KEINE* ANIMATION! forward/back bewirken, dass die 
	Turtle vom Startpunkt zum Endpunkt springt. Entsprechend 
	bewirken left/right eine augenblicklichen Orientierungsänderung.
        ***************
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        
        >>> turtle.speed(3)
""",

'Turtle.stamp' :
        """Erzeugt 'Stempelabdruck' der Turtleform auf der Zeichenfläche.

        Kein Argument.

        Erzeugt 'Stempelabdruck' der Turtleform auf der Zeichenfläche.
        Gibt eine Kennung für den Stempelabdruck zurück - zum allfälligen
        Löschen mit clearstamp().
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        
        >>> turtle.stamp()
        34
        >>> probe = turtle.stamp()
        >>> clearstamp(probe)
        
""",

'Turtle.tilt' :
        """Dreht die Turtleform *um* den angegebenen Winkel.

        Argument:
        angle - eine Zahl

        Verdreht die Turtleform *um* den angegebenen Winkel, ausgehend
        vom aktuellen Verdrehungswinkel. Die Orientierung (Bewegungsrichtung)
        der Turtle wird dabei *NICHT* verändert.
              
        Beispiele (für eine Turtle namens turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
""",

'Turtle.tiltangle' :
        """Gibt den aktuellen Verdrehungswinkel der Turtleform zurück.

        Kein Argument.

        Gibt den aktuellen Verdrehungswinkel der Turtleform,
        d. h. den Winkel zwischen der Orientierung der Turtleform
        und der Orientierung (Bewegungsrichtung) der Turtle zurück.
        
        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(45)
        >>> turtle.tiltangle()
        >>>         
""",

'Turtle.towards' :
        """Gibt die Orientierung zum Punkt (x,y) zurück.

        Argumente: zwei Zahlen (d. h. zwei Koordinaten)
	     oder: x ist ein Paar (2er-Tupel) oder Vektor aus zwei
		   Zahlen und y ist None
	     oder: x ist ein Turtle-Objekt (eine Turtle) und y ist None
        
        Aufruf: towards(<zahl>,<zahl>)    # zwei Koordinaten
        --oder: towards((<zahl>,<zahl>))  # ein Paar (2-Tuple) von Koordinaten
        --oder: towards(<2-vector>) # wie es z. B. von pos() zurückgegeben wird.	                                
        --oder: towards(mypen)            # wobei mypen eine andere Turtle ist
        
        Gibt die Orientierung der Linie von der Turtle zum Punkt (x,y) zurück,
        das ist der Winkel zwischen
         - der Linie von der aktuellen Turtle-Position zu (x,y)
         - und der Startorientierung der Turtle (siehe: heading()).
        Im Modus 'standard' ist die Startorientierung 'ost'
        und positive Winkel werden im Gegenuhrzeigersinn gemessen.
        Im Modus 'logo' ist die Startorientierung 'nord'
        und positive Winkel werden im Uuhrzeigersinn gemessen.
        (siehe mode())
        
        Beispiel (für ein Turtle-Objekt namens turtle):
        
        >>> turtle.pos()
        (10.00, 10.00)
        >>> turtle.towards(0,0)
        225.0        
""",

'Turtle.undo' :
        """Macht (wiederholt) die letzte Turtle-Aktion rückgängig.

        Kein Argument.

        Macht (wiederholt) die letzte Turtle-Aktion rückgängig.
        Die Anzahl der Aktionen, die rückgängig gemacht werden können,
        ist durch die Größe des undo-Speichers gegeben.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> for i in range(4):
                turtle.fd(50); turtle.lt(80)
                
        >>> for i in range(8):
                turtle.undo()        
""",

'Turtle.undobufferentries' :
        """Gibt die Anzahl der im undo-Speicher gespeicherten Aktionen zurück.

        Kein Argument.

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> while undobufferentries():
                undo()        
""",

'Turtle.write' :
        """Schreibt Text an die aktuelle Turtle-Position.

        Argumente:
        arg -- String (Text, der auf die TurtleScreen geschreiben wird.)
        move (optional) -- True/False
        align (optional) -- einer der Strings "left", "center" or right"
        font (optional) -- ein Tripel (fontname, fontsize, fonttype)

        Schreibt Text an die aktuelle Turtle-Position, ausgerichtet
        entsprechend dem Wert von align ("left", "center" oder right")
        und mit der für font angeebenen Schriftart.
        Wenn move True ist, wird die Turtle zum rechten unteren Ende
	des Textes bewegt. Voreinstellung für move ist False.

        Beispiel (für ein Turtle-Objekt namens turtle):
        
        >>> turtle.write('The race is on!')
        >>> turtle.write('Home = (0, 0)', True, align="center")        
""",

'Turtle.xcor' :
        """ Gibt die x Koordinate der Turtle zurück.

        Kein Argument..

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.xcor()
        50.0
        
""",

'Turtle.ycor' :
        """ Gibt die y Koordinate der Turtle zurück.

        Kein Argument..

        Beispiel (für ein Turtle-Objekt namens turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.ycor()
        86.6025403784
        
"""
}
