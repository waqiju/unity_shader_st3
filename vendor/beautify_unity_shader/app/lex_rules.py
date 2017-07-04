import re
from . import error_message
from .lex_token import Token
from .lex_tokens import TokenType


def LexicalError(text):
    raise Exception('find a lexical error. The pending text : ' + text)
    # error_message.error('find a lexical error. The pending text : ' + text)
    return Token(TokenType.LexicalError, text)


# 过滤hanging状态的正负号。需要在lexer.analyze() -> filterSpaceLike -> filterComment之后调用。
def FilterHangingSign(tokens):
    newTokens = []

    i = 0
    while i < len(tokens):
        token = tokens[i]
        # 判断后置是否满足hanging条件
        if (token.kind == TokenType.Plus or token.kind == TokenType.Minus) and i+1 < len(tokens) and tokens[i+1].kind == TokenType.Number:
            # 判定前置是否满足hanging条件
            if i == 0 or ( tokens[i-1].kind != TokenType.ID and tokens[i-1].kind != TokenType.Number ):
                newTokens.append(Token(TokenType.Number, token.text + tokens[i+1].text))
                i+=2
                continue
                
        newTokens.append(token)
        i += 1

    return newTokens


# floatPattern = r'[-+]?((?<=[^\w\.])[\d]+[\.]?[\d]*|(?<=\W)[\.][\d]+)[fF]?'
# numberPattern = '%s(e%s)?' % (floatPattern+r'(?=[\We])', floatPattern+r'(?=[\W])')
# Number是否包含+/-是条件性的。假如前一个Token是ID或者Number，则应该被看作Operator。
floatPattern = r'((?<=[^\w\.])[\d]+[\.]?[\d]*|(?<=\W)[\.][\d]+)[fF]?'
numberPattern = '%s(e%s)?' % (floatPattern+r'(?=[\We])', r'[-+]?' + floatPattern + r'(?=[\W])')


rules = [
    # priority 1 行注释
    {'pattern': re.compile(r"//.*"),
     'action': lambda text: Token(TokenType.Comment, text)},
    # 块注释
    {'pattern': re.compile(r"/\*(.|\n)*?\*/"),
     'action': lambda text: Token(TokenType.Comment, text)},
    # 字符串
    {'pattern': re.compile(r'\"[^\"]*\"'),
     'action': lambda text: Token(TokenType.String, text, text)},
    # 保留字
    # {'pattern': re.compile(r'\b(Lighting|Cull|ZTest|ZWrite|Blend)\b'),
    #  'action': lambda text: Token(TokenType.ReservedWord, text, text)},

    # priority 2 ID，ID的前后一定要是\b。特别注意，2D应该被识别为ID。
    {'pattern': re.compile(numberPattern),
     'action': lambda text: Token(TokenType.Number, text, text)},
    {'pattern': re.compile(r"\b(pragma|define|(?<=#)if)\b"),
     'action': lambda text: Token(TokenType.ID, text, text)},
    {'pattern': re.compile(r"\b[a-zA-Z_]\w*\b"),
     'action': lambda text: Token(TokenType.ID, text, text)},
    {'pattern': re.compile(r"\b[0-9a-zA-Z_]\w*\b"),
     'action': lambda text: Token(TokenType.ID, text, text)},
    # 标点符号
    {'pattern': re.compile(r"->"),
     'action': lambda text: Token(TokenType.RightArrow, text)},
    {'pattern': re.compile(r"\*\s*="),
     'action': lambda text: Token(TokenType.AddAssign, text)},
    {'pattern': re.compile(r"/\s*="),
     'action': lambda text: Token(TokenType.SubAssign, text)},
    {'pattern': re.compile(r"%\s*="),
     'action': lambda text: Token(TokenType.MulAssign, text)},
    {'pattern': re.compile(r"\+\s*="),
     'action': lambda text: Token(TokenType.DivAssign, text)},
    {'pattern': re.compile(r"-\s*="),
     'action': lambda text: Token(TokenType.ModAssign, text)},
    {'pattern': re.compile(r"<<\s*="),
     'action': lambda text: Token(TokenType.LeftShiftAssign, text)},
    {'pattern': re.compile(r">>\s*="),
     'action': lambda text: Token(TokenType.RightShiftAssign, text)},
    {'pattern': re.compile(r"%\s*="),
     'action': lambda text: Token(TokenType.ModAssign, text)},
    {'pattern': re.compile(r"&\s*="),
     'action': lambda text: Token(TokenType.AndAssign, text)},
    {'pattern': re.compile(r"\^\s*="),
     'action': lambda text: Token(TokenType.XorAssign, text)},
    {'pattern': re.compile(r"\|\s*="),
     'action': lambda text: Token(TokenType.OrAssign, text)},
    {'pattern': re.compile(r"=="),
     'action': lambda text: Token(TokenType.EQ, text)},
    {'pattern': re.compile(r"!="),
     'action': lambda text: Token(TokenType.NEQ, text)},
    {'pattern': re.compile(r"<="),
     'action': lambda text: Token(TokenType.LE, text)},
    {'pattern': re.compile(r">="),
     'action': lambda text: Token(TokenType.GE, text)},
    {'pattern': re.compile(r"&&"),
     'action': lambda text: Token(TokenType.AND, text)},
    {'pattern': re.compile(r"\|\|"),
     'action': lambda text: Token(TokenType.OR, text)},
    {'pattern': re.compile(r"<<"),
     'action': lambda text: Token(TokenType.LeftShift, text)},
    {'pattern': re.compile(r">>"),
     'action': lambda text: Token(TokenType.RightShift, text)},
    {'pattern': re.compile(r"\+\+"),
     'action': lambda text: Token(TokenType.Increment, text)},
    {'pattern': re.compile(r"--"),
     'action': lambda text: Token(TokenType.Decrement, text)},
    # 单
    {'pattern': re.compile(r","),
     'action': lambda text: Token(TokenType.Comma, text)},
    {'pattern': re.compile(r":"),
     'action': lambda text: Token(TokenType.Colon, text)},
    {'pattern': re.compile(r";"),
     'action': lambda text: Token(TokenType.Semicolon, text)},
    {'pattern': re.compile(r"\("),
     'action': lambda text: Token(TokenType.LParen, text)},
    {'pattern': re.compile(r"\)"),
     'action': lambda text: Token(TokenType.RParen, text)},
    {'pattern': re.compile(r"\["),
     'action': lambda text: Token(TokenType.LBrack, text)},
    {'pattern': re.compile(r"\]"),
     'action': lambda text: Token(TokenType.RBrack, text)},
    {'pattern': re.compile(r"{"),
     'action': lambda text: Token(TokenType.LBrace, text)},
    {'pattern': re.compile(r"}"),
     'action': lambda text: Token(TokenType.RBrace, text)},
    {'pattern': re.compile(r"\."),
     'action': lambda text: Token(TokenType.Dot, text)},
    {'pattern': re.compile(r"\+"),
     'action': lambda text: Token(TokenType.Plus, text)},
    {'pattern': re.compile(r"-"),
     'action': lambda text: Token(TokenType.Minus, text)},
    {'pattern': re.compile(r"\*"),
     'action': lambda text: Token(TokenType.Times, text)},
    {'pattern': re.compile(r"/"),
     'action': lambda text: Token(TokenType.Divide, text)},
    {'pattern': re.compile(r"~"),
     'action': lambda text: Token(TokenType.Tilde, text)},
    {'pattern': re.compile(r"%"),
     'action': lambda text: Token(TokenType.Percent, text)},
    {'pattern': re.compile(r"&"),
     'action': lambda text: Token(TokenType.Ampersand, text)},
    {'pattern': re.compile(r"\^"),
     'action': lambda text: Token(TokenType.Caret, text)},
    {'pattern': re.compile(r"\|"),
     'action': lambda text: Token(TokenType.VerticalBar, text)},
    {'pattern': re.compile(r"="),
     'action': lambda text: Token(TokenType.Assign, text)},
    {'pattern': re.compile(r"#"),
     'action': lambda text: Token(TokenType.Pound, text)},
    {'pattern': re.compile(r"\?"),
     'action': lambda text: Token(TokenType.Question, text)},
    {'pattern': re.compile(r"!"),
     'action': lambda text: Token(TokenType.NOT, text)},
    {'pattern': re.compile(r"<"),
     'action': lambda text: Token(TokenType.LT, text)},
    {'pattern': re.compile(r">"),
     'action': lambda text: Token(TokenType.GT, text)},
    # { 'pattern' : re.compile(r"tab1"),
    #   'action' : lambda text: Token(TokenType.tab2, text)},
    # priority 3
    # switchable Enter
    {'pattern': re.compile(r"[ \t]+", re.DOTALL),
     'action': lambda text: Token(TokenType.SpaceLike, text)},
    {'pattern': re.compile(r"[\n]", re.DOTALL),
     'action': lambda text: Token(TokenType.SpaceLike, text)},
     # 'action': lambda text: Token(TokenType.SpaceLike, text)},
    {'pattern': re.compile(r".*"),
     'action': LexicalError},
    {'pattern': re.compile(r".", re.DOTALL),
     'action': lambda text: Token(TokenType.AnyString, text)},
]
