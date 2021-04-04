import re
import json

class Tokenizer(object):
    def __init__(self, programText):
      self.programText = programText

    def tokenize(self):
        tokensPerLine = {}
        i = 0
        for line in self.programText:
            lineTokens = []
            for word in line.strip().split():
                for token in re.split("(,)",word.strip()):
                    if token == '':
                        continue
                    if '"' in token:
                        openStringIndex = token.find('"')
                        stringValue = token[openStringIndex:token.find('"',openStringIndex)]
                    try:
                        float(token)
                        lineTokens.append(token)
                    except ValueError:
                        # Not a float
                        if '.' in token:
                            for dotSplit in re.split("(\.)", token.strip()):
                                if dotSplit == '':
                                    continue
                                splitByBrackets = self.splitStringByBrackets(dotSplit)
                                lineTokens.extend(splitByBrackets)
                        else:  
                            splitByBrackets = self.splitStringByBrackets(token)
                            lineTokens.extend(splitByBrackets)

            if len(lineTokens) == 0:
                continue

            tokensPerLine[i] = lineTokens
            i+=1
            
        return tokensPerLine

    def splitStringByBrackets(self, inputString):
        lineTokens = []
        if '(' in inputString or  ')' in inputString:
            if '(' in inputString:
                for bracketSplit in re.split("(\()",inputString.strip()):
                    if bracketSplit != '':
                        lineTokens.append(bracketSplit)
            elif ')' in inputString:
                for bracketSplit in re.split("(\))",inputString.strip()):
                    if bracketSplit != '':
                        lineTokens.append(bracketSplit)
        else:
            lineTokens.append(inputString)

        return lineTokens

