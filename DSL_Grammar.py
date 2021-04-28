STRING = 'string'
OPEN_BRACKET = '('
CLOSE_BRACKET = ')'
DOT = '.'
NUMERIC_TYPE = '(\d+(?:\.\d+)?)'
IDENTIFIER = r'^[A-Za-z][A-Za-z0-9_]*$'
COMMA = ','

SHAPE_NAME = {
    'TRIANGLE' : 'Triangle',
    'CIRCLE' : 'Circle',
    'SQUARE' : 'Square',
    
    'POINT' : 'Point',
    'LINE' : 'Line',
    'RECTANGLE' : 'Rectangle',
    'PARALELOGRAM' : 'Paralelogram',
    'RHOMBUS' : 'Rhombus',
    'TRAPEZOID' : 'Trapezoid',
    'POLYGON' : 'Polygon',
    'PYRAMID' : 'Pyramid',
    'CONE' : 'Cone',
    'PRISM' : 'Prism',
    'SPHERE' : 'Sphere'
}

METHOD_NAME = {
    #'SET_PARAMETERS' : 'setParameters', nu e corect trebuie de sters
    'DRAW' : 'draw', #desenarea POINT, LINE, TRIANGLE, SQUARE, RECTANGLE, PARALELOGRAM, RHOMBUS, TRAPEZOID, POLYGON, CIRCLE, PYRAMID, CONE, PRISM, SPHERE
    'SET_VERTICES' : 'setVertices', #specificarea denumirea varfurilor LINE, TRIANGLE, SQUARE, RECTANGLE, PARALELORGRAM, RHOMBUS, TRAPEZOID
    
    'SET_NAME' : 'setName', #setare nume la POINT
    'SET_COORDINATES' : 'setCoordinates', #setare coordonate, pozitia in spatiu, locatia, etc POINT
    'SET_COLOR' : 'setColor', #schimbarea culorii POINT, LINE
    'SET_SIZE' : 'setSize', #setarea dimensiunii unui POINT
    'SET_POINT_ON_LINE' : 'setPointOnLine',
    'SET_LENGTH' : 'setLength', #specificarea lungimii LINE
    'DRAW_LINE_FROM_POINTS' : 'drawLineFromPoints', #desenarea intre doua puncte(e nevoie de specificare 2 POINT) LINE
    'SET_EDGE_LENGTH' : 'setEdgeLength', #specficiarea lungimea laturilor TRIANGLE, SQUARE, RECTANGLE, PARALELOGRAM, RHOMBUS, TRAPEZOID
    'SET_NAME_ANGLES' : 'setNameAngles', #specificarea denumirea unghiurilor TRIANGLE, SQUARE, RECTANGLE, PARALELOGRAM, RHOMBUS, TRAPEZOID
    'SET_ANGLES_DEGREES' : 'setAnglesDegrees', #specificarea valorii unghiurilor in grade TRIANGLE, PARALELOGRAM, RHOMBUS, TRAPEZOID
    'DRAW_MEDIAN' : 'drawMedian', #desenarea mediana in TRIANGLE
    'DRAW_PERPENDICULAR_BISECTOR' : 'drawPerpendicularBisector', #desenarea mediatoare la TRIANGLE
    'DRAW_MIDDLE_LINE' : 'drawMiddleLine', #desenara liniei mijlocii in TRIANGLE, TRAPEZOID
    'DRAW_BISECTOR' : 'drawBisector', #desenarea bisectoarei in TRIANGLE
    'DRAW_HEIGHT' : 'drawHeight', # desenarea inaltimii in TRIANGLE, TRAPEZOID, PYRAMID, CONE
    'DRAW_ORTHOCENTER' : 'drawOrthoCenter', #desenarea ortocentru(intersectia inaltimelor) la TRIANGLE
    'DRAW_CIRCUM_CENTER' : 'drawCircumCenter', #intersectia mediatoarelor la TRIANGLE
    'DRAW_WEIGHT_CENTER' : 'drawWeightCenter', #centrul de greutate, intersectia medianelor TRIANGLE
    'DRAW_CIRCUMSCRIS_CIRCLE' : 'drawCircumscrisCirle', #desenarea cercului circumscris TRIANGLE, SQUARE, RECTANGLE, TRAPEZOID, POLYGON
    'DRAW_INSCRIS_CIRCLE' : 'drawInscrisCircle', #desenarea cercului inscris TRIANGLE, SQUARE, RECTANGLE, PARALELOGRAM, RHOMBUS, TRAPEZOID, POLYGON
    'DRAW_DIAGONAL' : 'drawDiagonal', #desenarea diagonalei in SQUARE, RECTANGLE, PARALELOGRAM, RHOMBUS, TRAPEZOID, CIRCLE
    'SET_REGULAR_POLYGON': 'setRegularPolygon', #stabilirea numarului de laturi si lungimile laturililo unui regulat POLYGON
    'SET_POLYGON' : 'setPolygon', #stabilirea numarului de laturi si lungimile laturilor unui neregulat POLYGON
    'SET_RADIUS' : 'setRadius', #setarea razei unui CIRLE
    'SET_ORIGIN_NAME' : 'setOriginName', #setarea denumirea centrului CIRCLE
    'DRAW_RADIUS' : 'drawRadius', #desenarea razei CIRCLE
    'DRAW_TRIANGLE' : 'drawTriangle', #ilustrarea unui triunghi in interiorul/exteriorul CIRLCE
    'DRAW_SQUARE' : 'drawSquare', #ilustrarea unui patrat in interiorul/exteriorul CIRLCE
    'DRAW_TRAPEZOID' : 'drawTrapezoid', #ilustrarea unui trapez in interiorul/exteriorul CIRLCE
    'DRAW_POLYGON' : 'drawPolygon', #ilustrarea unui polygon cu n laturi in interiorul/exteriorul CIRLCE
    'DRAW_RHOMBUS' : 'drawRhombus', #ilustrarea unui romb in interiorul/exteriorul CIRLCE
    'DRAW_PARALELOGRAM' : 'drawParalelogram', #ilustrarea unui paralelogram in interiorul/exteriorul CIRLCE
    'DRAW_RECTANGLE' : 'drawRectangle', #ilustrarea unui dreptunghi in interiorul/exterioirul CIRLCE
    'SET_PYRAMID' : 'setPyramid', #stabilirea piramidei (baza si varful) PYRAMID
    'DRAW_INSCRIS_SPHERE' : 'drawInscrisSphere', #desenarea unei sfere inscrise in PYRAMID
    'DRAW_CIRCUMSCRIS_SPHERE' : 'drawCircumscrisSpehere', #desenarea unei sfere circumscrise la PYRAMID
    'SET_CONE' : 'setCone', #setarea parametrii uni CONE
    'SET_PRISM' : 'setPrism', #setarea parametrilor unei PRISM
    'SET_SPHERE' : 'setSphere' #setarea parametrilor unei sfere

}

SHAPE_METHODS = {
    'Point' : {
        'draw' : [],
        'setName' : ['STRING'],
        'setCoordinates' : ['NUMERIC_TYPE', 'NUMERIC_TYPE'],
        'setColor' : ['STRING'],
        'setSize' : ['NUMERIC_TYPE'],
        'setPointOnLine' : [ 'IDENTIFIER', 'IDENTIFIER', 'NUMERIC_TYPE'] #edge, start_vertex, dist_from_start
    },
    
    'Line' : {
        'draw' : [],
        'setVertices' : ['STRING', 'STRING'],
        'setLength' : ['NUMERIC_TYPE'],
        'setColor' : ['STRING'],
        'drawLineFromPoints' : ['IDENTIFIER', 'IDENTIFIER'] # e neveoie de declarat initial 2 POINT-uri
    },
    
    'Triangle' : {
        'setVertices' : ['STRING', 'STRING', 'STRING'],
        'draw' : [],
        'setEdgeLength' : ['NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE'],
        'setNameAngles' : ['STRING', 'STRING', 'STRING'],
        'setAnglesDegrees' : ['NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE'],
        'drawMedian' : ['POINT'], #start vertex
        'drawPerpendicularBisector' : ['LINE'], #latura pe care cade mediatoarea
        'drawMiddleLine' : ['LINE', 'LINE'], #linia mijlocie pe care 2 laturi sta
        'drawBisector' : ['POINT'], #start din care varf
        'drawHeight' : ['POINT'],
        'drawOrthoCenter' : [],
        'drawCircumCenter' : [],
        'drawWightCenter' : [],
        'drawCircumcrisCircle' : [],
        'drawInscrisCircle' : []
    },
    
    'Square' : {
        'draw' : [],
        'setVertices' : ['STRING', 'STRING', 'STRING', 'STRING'],
        'drawDiagonal' : ['POINT', 'POINT'], # start si end point
        'setEdgeLength' : ['NUMERIC_TYPE'],
        'drawCircumcrisCircle' : [],
        'drawInscrisCircle' : [],
        'setNameAngles' : ['STRING', 'STRING', 'STRING', 'STRING']
    },
    
    'Paralelogram' : {
        'draw' : [],
        'setVertices' : ['STRING', 'STRING', 'STRING', 'STRING'],
        'drawDiagonal' : ['POINT', 'POINT'], # start si end point
        'setEdgeLength' : ['NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE'],
        'setNameAngles' : ['STRING', 'STRING', 'STRING', 'STRING'],
        'setAngleDegrees' : ['NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE']
    },

    'Rhombus' : {
        'draw' : [],
        'setVertices' : ['STRING', 'STRING', 'STRING', 'STRING'],
        'drawDiagonal' : ['POINT', 'POINT'], # start si end point
        'setEdgeLength' : ['NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE'],
        'setNameAngles' : ['STRING', 'STRING', 'STRING', 'STRING'],
        'setAngleDegrees' : ['NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE'],
        'drawInscrisCircle' : []
    },

    'Trapezoid' : {
        'draw' : [],
        'setVertices' : ['STRING', 'STRING', 'STRING', 'STRING'],
        'drawDiagonal' : ['POINT', 'POINT'], # start si end point
        'setEdgeLength' : ['NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE'],
        'setNameAngles' : ['STRING', 'STRING', 'STRING', 'STRING'],
        'setAngleDegrees' : ['NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE', 'NUMERIC_TYPE'],
        'drawCircumscrisCircle' : [],
        'drawInscrisCircle' : [],
        'drawMiddleLine' : ['LINE', 'LINE'], #e important sa fie lature laterale, dar nu bazele
        'drawHeight' : ['POINT'] #punctul de pe baza mica
    },

    'Polygon' : {
        'setRegularPolygon' : ['NUMERIC_TYPE', 'NUMERIC_TYPE'], #nr de laturi si lungimea
        'setPolygon' : ['NUMERIC_TYPE', 'NUMERIC_TYPE[]'], #nr de laturi si list cu lungimea la fiecare latura
        'drawInscrisCircle' : [], #daca poligonul este regulat
        'drawCircumscrisCircle' : [], #daca poligonul este regulat
        'draw' : []
    },
    
    'Circle' : {
        'draw' : [],
        'setRadius' : ['NUMERIC_TYPE'],
        'setOriginName' : ['STRING'],
        'drawRadius' : [],
        'drawDiagonal' : [],
        'drawTriangle' : ['POINT', 'POINT', 'POINT', '0 sau 1'], #0 daca este inscris si 1 daca este circumscris, numeric_type = coordonate polare
        'drawSquare' : ['POINT', 'POINT', 'POINT', 'POINT', '0 sau 1'], #0 daca este inscris si 1 daca este circumscris
        'drawTrapezoid' : ['POINT', 'POINT', 'POINT', 'POINT', '0 sau 1'], #0 daca este inscris si 1 daca este circumscris
        'drawPolygon' : ['POINT[]', '0 sau 1'], #0 daca este inscris si 1 daca este circumscris
        'drawRhombus' : ['POINT', 'POINT', 'POINT', 'POINT', '0 sau 1'], #0 daca este inscris si 1 daca este circumscris
        'drawParalelogram' : ['POINT', 'POINT', 'POINT', 'POINT', '0 sau 1'], #0 daca este inscris si 1 daca este circumscris
        'drawRectangle' : ['POINT', 'POINT', 'POINT', 'POINT', '0 sau 1'] #0 daca este inscris si 1 daca este circumscris
    },
    
    'Pyramid' : {
        'draw' : [],
        'setPyramid' : ['POINT', 'POINT', 'POINT', 'POINT', 'POINT'], #baza piramidei si varful
        'drawHeight' : [],
        'drawInscrisSphere' : [],
        'drawCircumscrisSphere' : []
    },
    
    'Prism' : {
        'setPrism' : ['POINT', 'POINT', 'POINT', 'POINT', 'NUMERIC_TYPE'],
        'draw' : [],
        'drawInscrisSphere' : [], #daca este cub
        'drawCircumscrisSphere' : [], #daca este cub
        'drawDiagonal' : ['POINT', 'POINT']
    },
    
    'Sphere' : {
        'setSphere' : ['NUMERIC_TYPE', 'STRING'],
        'draw' : []
    }
}