STRING = 'string'
OPEN_BRACKET = '('
CLOSE_BRACKET = ')'
DOT = '.'
NUMBERIC_TYPE = '(\d+(?:\.\d+)?)'
IDENTIFIER = r'^[A-Za-z][A-Za-z0-9_]*$'
COMMA = ','

SHAPE_NAME = {
  'TRIANGLE' : 'Triangle',
  'CIRCLE' : 'Circle',
  'SQUARE' : 'Square'
}

METHOD_NAME = {
  'SET_PARAMETERS' : 'setParameters',
  'DRAW' : 'draw',
  'SET_VERTICES' : 'setVertices'
}

SHAPE_METHODS = {
  SHAPE_NAME['TRIANGLE'] :{
    METHOD_NAME['SET_PARAMETERS'] : ['NUMBERIC_TYPE', 'NUMBERIC_TYPE', 'NUMBERIC_TYPE'],
    METHOD_NAME['DRAW'] : [],
    METHOD_NAME['SET_VERTICES'] : ["STRING", "STRING", "STRING"]
  },
  SHAPE_NAME['SQUARE'] :{
  },
}
