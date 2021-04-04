from Tokenizer import Tokenizer
from Lexer import Lexer
from Parser import Parser
from SemanticAnalyzer import SemanticAnalyzer
import re

program = open("Program.txt", "r")
lines = program.readlines()

tokenizer = Tokenizer(lines)
lexer = Lexer(tokenizer)
semantic = SemanticAnalyzer(lexer)
semantic.getSemanticErrors();
