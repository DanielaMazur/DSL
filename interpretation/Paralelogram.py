import pysketcher as ps
import math
from interpretation.Point import Point

class Paralelogram(ps.Style):
    def __init__(self, figure):
        self.figure = figure

        self.name1 = ""
        self.name2 = ""
        self.name3 = ""
        self.name4 = ""   

        self.centerX = 0
        self.centerY = 0
        self.angle = math.pi/3
        self.setEdgeLength(2, 1)

    def setAnglesDegrees(self, angleDegrees):
        self.angle = angleDegrees/180*math.pi
        self.setEdgeLength(self.edgeLength_1, self.edgeLength_2)

    def draw(self, lineStyle = 'SOLID'):
        line1 = ps.Line(self.point1, self.point2)
        line2 = ps.Line(self.point2, self.point3)
        line3 = ps.Line(self.point3, self.point4)
        line4 = ps.Line(self.point4, self.point1)

        line3.style.line_style = ps.Style.LineStyle[lineStyle.upper()]
        line4.style.line_style = ps.Style.LineStyle[lineStyle.upper()]

        nameOffset = 0.07

        point1NameCoordinates =  ps.Point(self.x1 - nameOffset, self.y1 + nameOffset)
        point2NameCoordinates =  ps.Point(self.x2 + nameOffset, self.y2 + nameOffset)
        point3NameCoordinates =  ps.Point(self.x3 + 2.5 * nameOffset, self.y3 - 2.5 * nameOffset)
        point4NameCoordinates =  ps.Point(self.x4 - 2.5 * nameOffset, self.y4 - 2.5 * nameOffset)

        point1Name = ps.Text(self.name1, point1NameCoordinates)
        point2Name = ps.Text(self.name2, point2NameCoordinates)
        point3Name = ps.Text(self.name3, point3NameCoordinates)
        point4Name = ps.Text(self.name4, point4NameCoordinates)

        self.figure.add(point1Name)
        self.figure.add(point2Name)
        self.figure.add(point3Name)
        self.figure.add(point4Name)

        self.figure.add(line1)        
        self.figure.add(line2)        
        self.figure.add(line3)        
        self.figure.add(line4)

    def drawSmallDiagonal(self):
        if self.angle > math.pi/2:
            newPoint_1 = ps.Point(self.x2, self.y2)
            newPoint_2 = ps.Point(self.x4, self.y4)
        else:
            newPoint_1 = ps.Point(self.x3, self.y3)
            newPoint_2 = ps.Point(self.x1, self.y1)


        diagonal = ps.Line(newPoint_1, newPoint_2)

        self.figure.add(diagonal)
    
    def drawBigDiagonal(self):
        if self.angle < math.pi/2:
            newPoint_1 = ps.Point(self.x2, self.y2)
            newPoint_2 = ps.Point(self.x4, self.y4)
        else:
            newPoint_1 = ps.Point(self.x3, self.y3)
            newPoint_2 = ps.Point(self.x1, self.y1)


        diagonal = ps.Line(newPoint_1, newPoint_2)

        self.figure.add(diagonal)

    def setPoints(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
    
    def setEdgeLength(self, newEdgeLength_1, newEdgeLength_2):
        self.edgeLength_1 = newEdgeLength_1
        self.edgeLength_2 = newEdgeLength_2

        self.x1 = self.centerX - self.edgeLength_1/2 + self.edgeLength_2*math.sin(self.angle)*1/2
        self.y1 = self.centerY + (math.sin(self.angle)*self.edgeLength_2) * 1/2

        self.x2 = self.x1 + self.edgeLength_1
        self.y2 = self.y1

        self.x4 = self.centerX - self.edgeLength_1*1/2 - self.edgeLength_2*math.cos(self.angle) + self.edgeLength_2*math.sin(self.angle)*1/2
        self.y4 = self.centerY - (math.sin(self.angle)*self.edgeLength_2) * 1/2

        self.x3 = self.x4 + self.edgeLength_1
        self.y3 = self.y4

        self.point1 = ps.Point(self.x1, self.y1)
        self.point2 = ps.Point(self.x2, self.y2)
        self.point3 = ps.Point(self.x3, self.y3)
        self.point4 = ps.Point(self.x4, self.y4)
    
    def setVertices(self, point1Name, point2Name, point3Name, point4Name):
        self.name1 = point1Name
        self.name2 = point2Name
        self.name3 = point3Name
        self.name4 = point4Name   
    
    def setNameAngles(self, angleName1, angleName2, angleName3, angleName4):
        angle1WithName = ps.ArcWithText(angleName1, ps.Point(self.x1, self.y1), 0.4, ps.Angle(-math.pi + self.angle), ps.Angle(math.pi - self.angle))
        angle2WithName = ps.ArcWithText(angleName2, ps.Point(self.x2 , self.y2), 0.4, ps.Angle(-math.pi), ps.Angle(self.angle))
        angle3WithName = ps.ArcWithText(angleName3, ps.Point(self.x3, self.y3), 0.4, ps.Angle(self.angle), ps.Angle(math.pi - self.angle))
        angle4WithName = ps.ArcWithText(angleName4, ps.Point(self.x4, self.y4), 0.4, ps.Angle(0.0), ps.Angle(self.angle))

        self.figure.add(angle1WithName)
        self.figure.add(angle2WithName)
        self.figure.add(angle3WithName)
        self.figure.add(angle4WithName)
    
