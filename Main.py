from Tokenizer import Tokenizer
from Lexer import Lexer
from Parser import Parser
from SemanticAnalyzer import SemanticAnalyzer
from interpretation.Interpreter import Interpreter

program = open("Program.txt", "r")
lines = program.readlines()

tokenizer = Tokenizer(lines)
lexer = Lexer(tokenizer)
semantic = SemanticAnalyzer(lexer)
semantic.getSemanticErrors()

parser = Parser(lexer)
interpreter = Interpreter(parser)


print(parser.getParserAST())
parser.printAST()

interpreter.interpret()