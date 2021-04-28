class Interpreter():
  def __init__(self, parser):
      self.parser = parser.getParserAST()
    
  def interpret(self):
    file = open('generatedFile.py', 'w')

    file.write("import pysketcher as ps\nfrom pysketcher.backend.matplotlib import MatplotlibBackend\n")
    file.write("figure = ps.Figure(-5.0, 5.0, -5.0, 5.0, MatplotlibBackend)\n")

    # first declare all variables
    for variableType, restAST in self.parser.items():
      for variableName, methods in restAST.items():
        file.write(f"from interpretation.{variableType} import {variableType}\n")
        file.write(f"{variableName} = {variableType}(figure)\n")

    for variableType, restAST in self.parser.items():
      for variableName, methods in restAST.items():
        for method, argumentList in methods.items():
          stringArgumentList = ""
          for argument in argumentList:
            stringArgumentList += str(argument) + ","
          stringArgumentList = stringArgumentList[:-1]
          file.write(f"{variableName}.{method}({stringArgumentList})\n")

    file.write("figure.save('interpretation/assets/final.png')")
    file.close()

    import generatedFile