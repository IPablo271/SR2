from gl import *

glCreateWindow(1000, 1000)

glColor(0, 1, 0)



rectangulo1 = [(100,300),(400,100),(400,400),(100,600)]
rectangulo2 = [(400,400),(600,700),(900,400),(900,100),(750,100),(750,300),(600,300),(600,100),(400,100)]
rectangulo3 = [(400,400),(600,700),(350,850),(100,600)]
rectangulo4 = [(500,762),(500,850),(550,860),(550,730)]
rectangulo5 = [(499,763),(499,850),(450,870),(450,790)]
rectangulo6 =[(499,850),(450,870),(500,890),(550,860)]    

fillfigure2(rectangulo1)
glColor(1, 0, 0)
fillfigure2(rectangulo2)
glColor(1, 0, 1)
fillfigure2(rectangulo3)
glColor(0, 0, 1)
fillfigure2(rectangulo4)
glColor(1, 1, 0)
fillfigure2(rectangulo5)
glColor(0.9, 0.6, 0.1)
fillfigure2(rectangulo6)
glFinish()



