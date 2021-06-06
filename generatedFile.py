import pysketcher as ps
from pysketcher.backend.matplotlib import MatplotlibBackend
figure = ps.Figure(-5.0, 5.0, -5.0, 5.0, MatplotlibBackend)
from interpretation.Cube import Cube
A = Cube(figure)
A.drawDiagonal(3.0,5.0)
A.setVertices("A","B","C","D","F","G","H","I")
A.draw()
figure.save('interpretation/assets/final.png')