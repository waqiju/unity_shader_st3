import unittest
from .lex_rules import rules, FilterHangingSign
from . import error_message
from .symbol_type import SymbolType
from .lex_token import Token
from .lex_tokens import TokenType


def analyze(inputText, isKeepSpace=True, isKeepComment=True, isEnding=False):
    pos = 0
    tokens = []
    error_message.reset()

    while pos < len(inputText):
        for rule in rules:
            match = rule['pattern'].match(inputText, pos)
            if match:
                matchText = match.group()
                tokens.append(rule['action'](matchText))
                error_message.forward(matchText)
                pos = match.end()
                break


    # 建立源文件中的token顺序链表，包括SpaceLike和Comment
    for i in range(0, len(tokens)-1):
        tokens[i].nextToken = tokens[i+1]

    if not isKeepSpace:
        tokens = list(filter(lambda token: token.kind != TokenType.SpaceLike, tokens))
        tokens = FilterHangingSign(tokens)
    if not isKeepComment:
        tokens = list(filter(lambda token: token.kind != TokenType.Comment, tokens))

    if isEnding:
        tokens.append(Token(SymbolType.EndingTerminal))

    return tokens


class Test(unittest.TestCase):

    def _writeTokens(tokens):
        import os
        outputFile = os.path.abspath( os.path.join(__file__, r"../../test/lex_output.txt") )
        with open(outputFile, 'w') as f:
            for token in tokens:
                f.write(str(token))
                f.write('\n')


    def test(self):
        import os
        testFile = os.path.abspath( os.path.join(__file__, r"../../test/test.shader") )

        with open(testFile) as f:
            buf = f.read()
            tokens = analyze(buf, False, True)
            Test._writeTokens(tokens)

