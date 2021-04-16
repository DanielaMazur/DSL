import json
import re

from DSL_Grammar import SHAPE_NAME, SHAPE_METHODS, STRING, NUMERIC_TYPE, IDENTIFIER, OPEN_BRACKET, CLOSE_BRACKET, DOT, METHOD_NAME, COMMA

class Token(object):
  def __init__(self, type, value):
      self.type = type
      self.value = value

  def __str__(self):
    """String representation of the class instance.
        Examples:
            (INTEGER, 3)
            (PLUS, '+')
            (MUL, '*')"""

    return '({type}, {value})'.format(type=self.type, value=repr(self.value))
    #Mihai Moglan: am sters cuv "Token" - imi crea dificultati in rezolvare

  def __repr__(self):
    return self.__str__()


class Lexer(object):
  def __init__(self, tokenizer):
      self.tokens = tokenizer.tokenize()

  def getTokenType(self, word):
    if word[0]=='"' and word[-1]=='"':
      return 'STRING'
    elif word in SHAPE_NAME.values():
      return 'SHAPE_NAME'
    elif bool(re.search(IDENTIFIER, word)) and word not in SHAPE_NAME.values() and word not in METHOD_NAME.values():
      return 'IDENTIFIER'
    elif word in METHOD_NAME.values():
      return 'METHOD_NAME'
    elif word == OPEN_BRACKET:
      return 'OPEN_BRACKET'
    elif word == CLOSE_BRACKET:
      return 'CLOSE_BRACKET'
    elif word == DOT:
      return 'DOT'
    elif word == COMMA:
      return 'COMMA'   
    elif re.findall(NUMERIC_TYPE, word):
      return 'NUMERIC_TYPE'

  def getLexerTokens(self):
    lexer = {}
    for token in self.tokens:
      line = self.tokens[token]
      line_lexer = []
      for word in line:
        tokenType = self.getTokenType(word)
        line_lexer.append(Token(tokenType, word))
        lexer[int(token)] = line_lexer

    return lexer