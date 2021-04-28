import pysketcher as ps
from pysketcher.backend.matplotlib import MatplotlibBackend
from random import uniform
import math

DEFAULT_COLOR = 'BLACK'

class Point(ps.Style):
  def __init__(self, figure):
    self.x = uniform(-5, 5)
    self.y = uniform(-5, 5)

    self.figure = figure
    
    self.size = 0.05
    self.color = DEFAULT_COLOR
    self.name = ''

  def draw(self):
    coordinates = ps.Point(self.x, self.y)
    
    point = ps.Circle(coordinates, self.size)

    point.style.fill_color = ps.Style.Color[self.color]
    point.style.line_color = ps.Style.Color[self.color]

    pointNameCoordinates =  ps.Point(self.x + self.size + 0.8 * self.size, self.y + self.size + 0.8 * self.size)
    pointName = ps.Text(self.name, pointNameCoordinates)

    self.figure.add(point)
    self.figure.add(pointName)
      
  def setSize(self, size):
    self.size = size
  
  def setColor(self, color):
    self.color = color.upper()
  
  def setName(self, name):
    self.name = name
  
  def setCoordinates(self, x, y):
    self.x = x
    self.y = y
  
  def setPointOnLine(self, line, startPoint, distance):
    slope = math.atan((line.y1 - line.y2) / (line.x1 - line.x2))

    maxX = max(line.x1, line.x2)

    if startPoint.x == maxX:
      self.x = startPoint.x - (distance * math.cos(slope))
      self.y = startPoint.y - (distance * math.sin(slope))
    else:
      self.x = startPoint.x + (distance * math.cos(slope))
      self.y = startPoint.y + (distance * math.sin(slope))


