from random import uniform
import pysketcher as ps
from pysketcher.backend.matplotlib import MatplotlibBackend
import math

class Line(ps.Style):
  def __init__(self, figure):
    self.x1 = uniform(-5, 5)
    self.x2 = uniform(-5, 5)
    self.y1 = uniform(-5, 5)
    self.y2 = uniform(-5, 5)

    self.figure = figure

    self.size = 0.05

    self.name1 = ""
    self.name2 = ""

    self.color = "BLACK"

  def draw(self):
    point1 = ps.Point(self.x1, self.y1)
    point2 = ps.Point(self.x2, self.y2)

    line = ps.Line(point1, point2)

    line.style.line_color = ps.Style.Color[self.color]

    point1NameCoordinates =  ps.Point(self.x1 + self.size, self.y1 + self.size)
    point2NameCoordinates =  ps.Point(self.x2 + self.size, self.y2 + self.size)

    point1Name = ps.Text(self.name1, point1NameCoordinates)
    point2Name = ps.Text(self.name2, point2NameCoordinates)

    self.figure.add(line)
    self.figure.add(point1Name)
    self.figure.add(point2Name)
  
  def setVertices(self, name1, name2):
    self.name1 = name1
    self.name2 = name2

  def setColor(self, color):
    self.color = color.upper()
  
  def setLength(self, length):   
    slope = math.atan(self.y1 / self.x1)

    self.x2 = self.x1 + (length * math.cos(slope))
    self.y2 = self.y1 + (length * math.sin(slope))

    # select new points if line gets out of canvas 
    if self.x2 > 5 or self.y2 > 5 or self.x2 < -5 or self.y2 < -5:
      self.x1 = uniform(-5, 5)
      self.x2 = uniform(-5, 5)
      self.y1 = uniform(-5, 5)
      self.y2 = uniform(-5, 5)

      return self.setLength(length)
  
  def drawLineFromPoints(self, point1, point2):
    self.x1 = point1.x
    self.x2 = point2.x
    self.y1 = point1.y
    self.y2 = point2.y

