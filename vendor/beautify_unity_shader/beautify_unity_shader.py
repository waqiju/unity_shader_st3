import sys
import json
from app import parser
from app.extension.formatter import Formatter


def formatFile(inputFilePath, outputFilePath):
    try:
        with open(inputFilePath) as f:
            inputText = f.read()
        ast, tokens = parser.analyzeCodeText(inputText)
        formatter = Formatter(tokens, ast)

        if outputFilePath != "":
            with open(outputFilePath, 'w') as f:
                f.write(formatter.toCode())
        else:
            print(formatter.toCode())
    except IOError:
        dealFilePathError()


def parseFile(inputFilePath, outputFilePath):
    try:
        with open(inputFilePath) as f:
            inputText = f.read()
        ast, tokens = parser.analyzeCodeText(inputText)

        if outputFilePath != "":
            with open(outputFilePath, 'w') as f:
                json.dump(ast.toDict(), f, indent=4)
        else:
            print(json.dumps(ast.toDict(), indent=4))
    except IOError:
        dealFilePathError()


def dealParameterError():
    print("Parameters Is Wrong! Eixt!")
    exit()


def dealFilePathError():
    print("File IO Error! Exit!")
    exit()


if __name__ == "__main__":
    inputFilePath = ""
    outputFilePath = ""
    action = ""

    index = 0
    while index < len(sys.argv):
        param = sys.argv[index]

        if index == 0:
            index += 1
            continue

        if param == '-w':
            if inputFilePath != "":
                outputFilePath = inputFilePath
            else:
                dealParameterError()
            index += 1
            continue
        elif param == '-o' and index + 1 < len(sys.argv):
            outputFilePath = sys.argv[index + 1]
            index += 2
            continue
        elif param == '--syntax' and index + 1 < len(sys.argv):
            action = 'parse'
            inputFilePath = sys.argv[index + 1]
            index += 2
            continue
        elif param[0] != '-' and inputFilePath == "":
            inputFilePath = sys.argv[index]
            index += 1
            continue
        else:
            dealParameterError()

    if inputFilePath == "":
        dealParameterError()

    if action == "":
        formatFile(inputFilePath, outputFilePath)
    elif action == "parse":
        parseFile(inputFilePath, outputFilePath)
    else:
        dealParameterError()
