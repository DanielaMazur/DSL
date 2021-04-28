import pysketcher as ps
from pysketcher.backend.matplotlib import MatplotlibBackend
figure = ps.Figure(-5.0, 5.0, -5.0, 5.0, MatplotlibBackend)
from interpretation.Point import Point
A = Point(figure)
from interpretation.Point import Point
B = Point(figure)
from interpretation.Point import Point
C = Point(figure)
from interpretation.Point import Point
D = Point(figure)
from interpretation.Line import Line
AB = Line(figure)
from interpretation.Line import Line
CD = Line(figure)
A.setCoordinates(-3.0,0.0)
A.setName("A")
A.setColor("red")
A.draw()
B.setCoordinates(0.0,0.0)
B.setName("B")
B.setColor("red")
B.draw()
C.setCoordinates(3.0,0.0)
C.setName("C")
C.setColor("red")
C.draw()
D.setCoordinates(4.0,0.0)
D.setName("D")
D.setColor("red")
D.draw()
AB.drawLineFromPoints(A,B)
AB.setColor("blue")
AB.draw()
CD.drawLineFromPoints(C,D)
CD.setColor("blue")
CD.draw()
figure.save('interpretation/assets/final.png')