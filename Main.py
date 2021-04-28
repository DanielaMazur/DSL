from Tokenizer import Tokenizer
from Lexer import Lexer
from Parser import Parser
from SemanticAnalyzer import SemanticAnalyzer

program = open("Program.txt", "r")
lines = program.readlines()

tokenizer = Tokenizer(lines)
lexer = Lexer(tokenizer)
semantic = SemanticAnalyzer(lexer)
semantic.getSemanticErrors()

parser = Parser(lexer)

print(parser.getParserAST())
parser.printAST()

