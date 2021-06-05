import pysketcher as ps
from pysketcher.backend.matplotlib import MatplotlibBackend
figure = ps.Figure(-5.0, 5.0, -5.0, 5.0, MatplotlibBackend)
from interpretation.Cube import Cube
A = Cube(figure)
A.setLength(2.5)
A.drawDiagonal(4.0,6.0)
A.setVertices("A","B","C","D","E","F","G","H")
A.drawLength()
A.draw()
figure.save('interpretation/assets/final.png')