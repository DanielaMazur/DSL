import re
import json
from Tokenizer import Tokenizer
from Lexer import Lexer

class Parser(object):
  def __init__(self, lexer):
    self.lexer = lexer.getLexerTokens()
    self.parser = {}
  
  def getParserAST(self):
    for key in self.lexer: #key : 0, 1, 2, 3, ...
        code_line = self.lexer[key] # code_line : [(SHAPE_NAME, 'Triangle'), (IDENTIFIER, 'myTriangle')]
        for token in code_line:
            if token.type == 'SHAPE_NAME' and token.value not in self.parser:
                self.parser[token.value] = {}
#    print(self.parser)

    for shapeName in self.parser:
        identifiers = {}
        for key in self.lexer:
            code_line = self.lexer[key]
#            print(code_line)
            if code_line[1].type == 'IDENTIFIER' and code_line[0].value == shapeName:
                identifiers[code_line[1].value] = {}
        self.parser[shapeName] = identifiers
#    print(self.parser)

    for shapeName in self.parser:
        for identifier in self.parser[shapeName]:
            methods = {}
            for key in self.lexer:
                code_line = self.lexer[key]
                if code_line[0].type == 'IDENTIFIER' and code_line[1].type == 'DOT' and code_line[2].type == 'METHOD_NAME' and code_line[0].value == identifier:
                    arguments = []
                    i = 4
                    while(code_line[i].value != ')'):
                        if code_line[i].type == 'STRING':
                            arguments.append(str(code_line[i].value))
                        elif code_line[i].type == 'NUMERIC_TYPE':
                            arguments.append(float(code_line[i].value))
                        i += 1
                    methods[code_line[2].value] = arguments
            self.parser[shapeName][identifier] = methods
    #print(self.parser)
    return self.parser

  #printing Abstract Syntax Tree
  def printAST(self):
    for shapeName in self.parser:
        print(shapeName)
        for identifier in self.parser[shapeName]:
            print('\t', identifier)
            for method in self.parser[shapeName][identifier]:
                print('\t\t', method)
                for argument in self.parser[shapeName][identifier][method]:
                    print('\t\t\t', str(argument))
