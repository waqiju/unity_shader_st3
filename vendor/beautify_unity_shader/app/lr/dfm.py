import unittest


class SymbolStack:

    def __init__(self):
        self.stack = []

    def push(self, symbol, stateId):
        self.stack.append((symbol, stateId))

    # return value is a list
    def pop(self, count=1):
        symbols = []
        for i in range(0, count):
            symbol = self.stack.pop()[0]
            symbols.insert(0, symbol)

        return symbols

    def getTopStateId(self):
        return self.stack[-1][1]


def reduce(production, symbols):
    cls = production.LeftNonterminalClass
    return cls(*symbols)


def run(edges, productions, tokens, isDebug=False):
    if productions[0] is not None:
        productions.insert(0, None)
    stack = SymbolStack()

    stack.push('__Begin', 0)
    stateId = 0
    index = 0
    while index < len(tokens):
        token = tokens[index]
        # notice, should try toLiteral() for TokenType.ID firstly
        actionStr = edges[stateId].get(token.toLiteral()) or edges[stateId].get(token.kind) 

        if actionStr is None:
            raise Exception('syntax error: stateId = %s, token = %s' % (stateId, token))
            break
        elif actionStr[0] == 's':
            stateId = int(actionStr[1:])
            stack.push(token, stateId)
            # debug
            if isDebug:
                print('shift: %s s%s' % (token, stateId))
        elif actionStr[0] == 'r':
            productionId = int(actionStr[1:])
            production = productions[productionId]
            topSymbols = stack.pop(len(production.right))
            topStateId = stack.getTopStateId()
            nonterminal = reduce(production, topSymbols)
            # debug
            if isDebug:
                print('reduce: %s , LookAheadST = %s %s' % (production, token, actionStr))

            actionStr = edges[topStateId].get(nonterminal.kind)
            if actionStr is None:
                raise Exception('syntax error: stateId = %s, symbol = %s' % (topStateId, nonterminal.kind))
                break
            stateId = int(actionStr[1:])
            stack.push(nonterminal, stateId)
            # debug
            if isDebug:
                print('  >>>shift: %s s%s' % (nonterminal.kind, stateId))

            continue
        elif actionStr == 'a':
            break
        else:
            print(token, actionStr)
            raise Exception('should not go here! maybe cause unsolved conflicts')

        index += 1

    # print(list(str(token) for token in stack.stack))
    return stack.pop()[0]


class Test(unittest.TestCase):

    def test(self):
        from . import lr1
        from test.lr1_test.productions import productionList
        edges = lr1.construct(productionList)

        from .. import lexer
        inputText = '*a = b'
        tokens = lexer.analyze(inputText, isKeepSpace=False, isEnding=True)

        beginSymbol = run(edges, productionList, tokens)
        print(beginSymbol)
        print(beginSymbol.toDict())

        import os
        outputFile = os.path.abspath(os.path.join(__file__, '../../../test/lr1_test/syntax_output.txt'))
        with open(outputFile, 'w') as f:
            import json
            json.dump(beginSymbol.toDict(), f, indent=4)