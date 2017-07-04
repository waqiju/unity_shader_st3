# pp_if_stm         -> # 'if' binary_exp Enter
# ------
# pp_cmd            -> # pragma pragma_item_list Enter
# pragma_item_list  -> pragma_item
#                   -> pragma_item_list pragma_item
# pragma_item       -> ID
#                   -> Number
#                   -> ID : ID
# ------
# pp_cmd            -> # 'define' exp exp Enter


import unittest
from .lex_token import Token
from .lex_tokens import TokenType
from .lex_rules import FilterHangingSign


def analyze(tokens):
    filterTokens = []

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.kind == TokenType.Pound:
            filterTokens.append(token)
            i += 1
            # 去掉#和ID之间的空格
            while tokens[i].kind == TokenType.SpaceLike:
                i += 1
            # ^----token is #      v----- token is 'if'
            token = tokens[i]
            if token.text == 'if' or token.text == 'elif' or token.text == 'pragma' or token.text == 'define':
                filterTokens.append(token)
                i = eatPPToken(tokens, i + 1, filterTokens)
            else:
                filterTokens.append(token)
                i += 1
        else:
            filterTokens.append(token)
            i += 1

    # 去掉SpaceLike 去掉Comment
    filterTokens = list(filter(lambda token: token.kind != TokenType.SpaceLike, filterTokens))
    filterTokens = list(filter(lambda token: token.kind != TokenType.Comment, filterTokens))

    # 处理hanging的+-号
    filterTokens = FilterHangingSign(filterTokens)

    return filterTokens


def eatPPToken(inputTokens, nowIndex, filterTokens):
    ppToken = Token(TokenType.PPTokens, '')

    while True:
        if nowIndex >= len(inputTokens):
            break

        token = inputTokens[nowIndex]
        if token.kind == TokenType.SpaceLike and token.text.find('\n') >= 0:
            break

        ppToken.text += token.text
        ppToken.nextToken = token.nextToken
        nowIndex += 1

    ppToken.value = ppToken.text
    filterTokens.append(ppToken)
    nowIndex += 1
    return nowIndex


class Test(unittest.TestCase):

    def test(self):
        from . import lexer

        with open(r'C:\1_Workspace\beautify_unity_shader\test\preprocessor_test\test.shader') as f:
            inputText = f.read()

        tokens = lexer.analyze(inputText)
        for token in tokens:
            print(str(token), end=' ')
        print("")

        tokens = analyze(tokens)
        for token in tokens:
            print(str(token), end=' ')
