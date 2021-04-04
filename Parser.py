import re
import json

class Parser(object):
  def __init__(self, lexer):
    self.lexer = lexer
    self.parser = {}
  
  def getParserAST(self):
    for key in self.lexer:
        code_line = self.lexer[key]
        for token in code_line:
            if token[1] == 'shapeName' and token[0] not in self.parser:
                self.parser[token[0]] = {}

    for shapeName in self.parser:
        identifiers = {}
        for key in self.lexer:
            code_line = self.lexer[key]
            if len(code_line) > 1 and code_line[1][1] == 'identifier' and code_line[0][0] == shapeName:
                identifiers[code_line[1][0]] = {}
        self.parser[shapeName] = identifiers

    for shapeName in self.parser:
        for identifier in self.parser[shapeName]:
            methods = {}
            for key in self.lexer:
                code_line = self.lexer[key]
                if len(code_line) > 1 and code_line[0][0] == identifier and code_line[1][1] == 'DOT' and code_line[2][1] == 'methodName':
                    arguments = []
                    i = 4
                    while(code_line[i][0] != ')'):
                        if code_line[i][1] == 'string':
                            arguments.append(str(code_line[i][0]))
                        elif code_line[i][1] == 'numericType':
                            arguments.append(float(code_line[i][0]))
                        i += 1
                    methods[code_line[2][0]] = arguments
            self.parser[shapeName][identifier] = methods
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
