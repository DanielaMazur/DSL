from interpretation.Square import Square
import pysketcher as ps

class Cube(ps.Style):
    def __init__(self, figure):
        self.figure = figure
        self.edgeLength = 2

        self.name1 = ""
        self.name2 = ""
        self.name3 = ""
        self.name4 = ""   
        self.name5 = ""
        self.name6 = ""
        self.name7 = ""
        self.name8 = ""

        self.initCube()

    def draw(self):
        self.square1.draw()
        self.square2.draw("DASHED")

        self.figure.add(self.connectionLine1)
        self.figure.add(self.connectionLine2)
        self.figure.add(self.connectionLine3)
        self.figure.add(self.connectionLine4)

    def initCube(self):
        self.square1 = Square(self.figure)
        self.square1.setEdgeLength(self.edgeLength)
        self.square1.setCenter(-self.edgeLength / 2, -self.edgeLength /  2)

        self.square2 = Square(self.figure)
        self.square2.setEdgeLength(self.edgeLength)
        self.square2.setCenter(self.edgeLength / 2, self.edgeLength /  2)

        self.connectionLine1 = ps.Line(self.square1.point1, self.square2.point1)
        self.connectionLine2 = ps.Line(self.square1.point2, self.square2.point2)
        self.connectionLine3 = ps.Line(self.square1.point3, self.square2.point3)
        self.connectionLine4 = ps.Line(self.square1.point4, self.square2.point4)
        self.connectionLine4.style._line_style = ps.Style.LineStyle.DASHED

    def setLength(self, newEdgeLength):
        self.edgeLength = newEdgeLength
        self.initCube()
    
    def drawDiagonal(self, vertexNumber1, vertexNumber2):
        self.listOfVertices = [self.square1.point1, self.square1.point2, self.square1.point3, self.square1.point4,
                               self.square2.point1, self.square2.point2, self.square2.point3, self.square2.point4]
        
        diagonal = ps.Line(self.listOfVertices[int(vertexNumber1 - 1)], self.listOfVertices[int(vertexNumber2 - 1)])
        diagonal.style.line_style = ps.Style.LineStyle.DOTTED
        diagonal.style.line_color = ps.Style.Color.RED
        diagonal.style.line_width = 2

        self.figure.add(diagonal)

    def setVertices(self, name1, name2, name3, name4, name5, name6, name7, name8):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.name4 = name4   
        self.name5 = name5
        self.name6 = name6
        self.name7 = name7
        self.name8 = name8

        nameOffset = 0.07

        point1NameCoordinates =  ps.Point(self.square1.x1 - nameOffset, self.square1.y1 + nameOffset)
        point2NameCoordinates =  ps.Point(self.square1.x2 + nameOffset, self.square1.y2 + nameOffset)
        point3NameCoordinates =  ps.Point(self.square1.x3 + 2.5 * nameOffset, self.square1.y3 - 2.5 * nameOffset)
        point4NameCoordinates =  ps.Point(self.square1.x4 - 2.5 * nameOffset, self.square1.y4 - 2.5 * nameOffset)
        point5NameCoordinates =  ps.Point(self.square2.x1 - nameOffset, self.square2.y1 + nameOffset)
        point6NameCoordinates =  ps.Point(self.square2.x2 + nameOffset, self.square2.y2 + nameOffset)
        point7NameCoordinates =  ps.Point(self.square2.x3 + 2.5 * nameOffset, self.square2.y3 - 2.5 * nameOffset)
        point8NameCoordinates =  ps.Point(self.square2.x4 - 2.5 * nameOffset, self.square2.y4 - 2.5 * nameOffset)

        point1Name = ps.Text(self.name1, point1NameCoordinates)
        point2Name = ps.Text(self.name2, point2NameCoordinates)
        point3Name = ps.Text(self.name3, point3NameCoordinates)
        point4Name = ps.Text(self.name4, point4NameCoordinates)
        point5Name = ps.Text(self.name5, point5NameCoordinates)
        point6Name = ps.Text(self.name6, point6NameCoordinates)
        point7Name = ps.Text(self.name7, point7NameCoordinates)
        point8Name = ps.Text(self.name8, point8NameCoordinates)

        self.figure.add(point1Name)
        self.figure.add(point2Name)
        self.figure.add(point3Name)
        self.figure.add(point4Name)
        self.figure.add(point5Name)
        self.figure.add(point6Name)
        self.figure.add(point7Name)
        self.figure.add(point8Name)
    
    def drawLength(self):
        lineLengthTextCoordinates = ps.Point(self.square2.point2.x + 0.3, self.square2.point3.y - (self.square2.point3.y - self.square2.point2.y) / 2)
        
        edgeLengthText = ps.Text(self.edgeLength, lineLengthTextCoordinates)

        self.figure.add(edgeLengthText)
