import pysketcher as ps
from pysketcher.backend.matplotlib import MatplotlibBackend
figure = ps.Figure(-5.0, 5.0, -5.0, 5.0, MatplotlibBackend)
from interpretation.Paralelogram import Paralelogram
A = Paralelogram(figure)
A.setAnglesDegrees(72.0)
A.setEdgeLength(5.0,4.0)
A.setNameAngles("1","2","3","4")
A.draw()
figure.save('interpretation/assets/final.png')