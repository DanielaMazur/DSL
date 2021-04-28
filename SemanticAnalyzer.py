from DSL_Grammar import SHAPE_NAME, SHAPE_METHODS, STRING, NUMERIC_TYPE, IDENTIFIER, OPEN_BRACKET, CLOSE_BRACKET, DOT, METHOD_NAME

class SemanticAnalyzer(object): 
    def __init__(self, lexer):
        self.lexer = lexer
        self.registeredVariables = {}

    def getVariableDeclarationErrors(self, variableDeclarationLine):
        if len(variableDeclarationLine) == 1:
            raise Exception("Variable Name is missing")
        
        variableNameType = variableDeclarationLine[1].type

        if variableNameType == 'IDENTIFIER' and len(variableDeclarationLine) == 2:
            variableName = variableDeclarationLine[1].value
            if(variableName in self.registeredVariables.keys()):
                raise Exception("A variable with such name already exists")
                    
            # Store variable {'myTriangle': 'Triangle'}
            self.registeredVariables[variableName] = variableDeclarationLine[0].value
            return;

        if variableNameType == 'SHAPE_NAME' or variableNameType == 'METHOD_NAME':
            raise Exception('Variable name cannot be the same as a build in Method Name or Type')
        raise Exception('Invalid variable name. Rule for variable name : 1. Starts with a letter (small/capital), 2. Can contain only numbers and letters')
    
    def getMethodInvocationErrors(self, methodInvocationLine):
        if methodInvocationLine[0].value not in self.registeredVariables.keys():
            raise Exception("Variable '{variableName}' is not defined".format(variableName=methodInvocationLine[0].value))
        if methodInvocationLine[1].type != 'DOT':
            raise Exception('Dot operator fot method invocation is missing')
        if methodInvocationLine[2].type != 'METHOD_NAME':
            raise Exception("Method invocation was expected. Unknown method!")

        invokedMethodName = methodInvocationLine[2].value
        variableShapeType = self.registeredVariables[methodInvocationLine[0].value]
        if invokedMethodName not in SHAPE_METHODS[variableShapeType].keys():
            raise Exception("{methodName} method does not exist on variable type {variableType}".format(methodName=invokedMethodName, variableType=variableShapeType))
        if len(methodInvocationLine) < 4  or methodInvocationLine[3].type != 'OPEN_BRACKET':
            raise Exception("Method call was expected. Use '(<parameter_list>)' to call a method")

        tokenTypes = []
        for token in methodInvocationLine:
            tokenTypes.append(token.type)

        groupTokens = group_tokens_frequency(tokenTypes)
        if methodInvocationLine[-1].type != 'CLOSE_BRACKET' or groupTokens['METHOD_NAME'] > 1:
            raise Exception("Each statement should be written in a new line")

        invokedMethodParameterListGrammar = SHAPE_METHODS[variableShapeType][invokedMethodName]
        invokedMethodParameterList = methodInvocationLine[4 : len(methodInvocationLine) - 1]

        parameterListWithoutCommas = []
        #check if each argument in argument list is separated by comma
        for index in range(len(invokedMethodParameterList)):
            if index % 2 != 0:
                if invokedMethodParameterList[index].type != 'COMMA':
                    raise Exception("Each argument in argument list should be separated with comma")
            elif invokedMethodParameterList[index].type == 'COMMA':
                raise Exception("Two consecutive commas are not allowed")
            else:
                parameterListWithoutCommas.append(invokedMethodParameterList[index])
        if len(invokedMethodParameterListGrammar) != len(parameterListWithoutCommas):
            raise Exception("{numberOfArguments} arguments received but {expectedNumberOfArguments} arguments expected".format(numberOfArguments=len(parameterListWithoutCommas), expectedNumberOfArguments=len(invokedMethodParameterListGrammar)))

        for index in range(len(parameterListWithoutCommas) - 1):
            if parameterListWithoutCommas[index].type != invokedMethodParameterListGrammar[index]:
                raise Exception("Variable type mismatch in method argument list. {expectedType} was expected, but {actualType} was found".format(expectedType=invokedMethodParameterListGrammar[index], actualType=parameterListWithoutCommas[index].type))

    def getSemanticErrors(self):
        lexerTokens = self.lexer.getLexerTokens()
        for lineTokens in lexerTokens.values():
            if lineTokens[0].type == 'SHAPE_NAME':
                self.getVariableDeclarationErrors(lineTokens)
            elif lineTokens[0].type == 'IDENTIFIER':
                self.getMethodInvocationErrors(lineTokens)
            else:
                raise Exception("Unexpected Token")

   
def group_tokens_frequency(lst):
    return dict((el , lst.count(el)) for el in lst)
