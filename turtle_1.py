import turtle as tor
tor.title("Primer intento de un ibujo de estrella")

#setuo = a: ancho b: largo c: (eje x) d: (eje y)
tor.setup(640, 480, 0, 0)

#Primer dato eje "X" Segundo dato Eje "Y"


tor.fillcolor("yellow") #Color de relleno
tor.begin_fill()#comienzo del relleno
tor.goto(40,100)
tor.goto(80,0)
tor.goto(180,0) #Eje y = 0
tor.goto(180,0)
tor.goto(100,-50) #50 para que en la mano derecha de la estrella se vea mejor 

#segunda parte (Pata derecha de la estrella)
tor.goto(180,-150)
tor.goto(40,-90)

#(Pata izquierda de la estrella)
tor.goto(-80,-150)
tor.goto(-15,-50)

#(Mano derecha de la izquierda)
tor.goto(-95,0)
tor.goto(0,0)

tor.end_fill() # Termino del relleno
tor.exitonclick()
