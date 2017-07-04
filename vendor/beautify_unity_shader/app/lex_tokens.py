import unittest
from .symbol_type import SymbolType

class TokenType(SymbolType):

    # 变量
    ID = "ID"
    String = "String"
    Int = "NumberInt"
    Number = "Number"  # Int Float
    Comment = "Comment"
    SpaceLike = "SpaceLike"
    Enter = "Enter" # 偶尔需要这个，比如C语言的pragma
    # 双符号标点
    RightArrow = "RightArrow"
    AddAssign = "AddAssign"
    SubAssign = "SubAssign"
    MulAssign = "MulAssign"
    DivAssign = "DivAssign"
    ModAssign = "ModAssign"
    LeftShiftAssign = "LeftShiftAssign"
    RightShiftAssign = "RightShiftAssign"
    ModAssign = "ModAssign"
    AndAssign = "AndAssign"
    XorAssign = "XorAssign"
    OrAssign = "OrAssign"
    LeftShift = "LeftShift"
    RightShift = "RightShift"
    Increment = "Increment"
    Decrement = "Decrement"
    # 单符号标点
    Comma = "Comma"
    Colon = "Colon"
    Semicolon = "Semicolon"
    LParen = "LParen"
    RParen = "RParen"
    LBrack = "LBrack"
    RBrack = "RBrack"
    LBrace = "LBrace"
    RBrace = "RBrace"
    Dot = "Dot"
    Plus = "Plus"
    Minus = "Minus"
    Times = "Times"
    Divide = "Divide"
    Tilde = "Tilde"
    Percent = "Percent"
    Ampersand = "Ampersand"
    Caret = "Caret"
    VerticalBar = "VerticalBar"

    EQ = "EQ"
    NEQ = "NEQ"
    LT = "LT"
    LE = "LE"
    GT = "GT"
    GE = "GE"
    NOT = "NOT"
    AND = "AND"
    OR = "OR"
    Assign = "Assign"
    Pound = "Pound"
    Question = "Question"

    # C语言的宏变量
    C_MARCO_VARIABLE = "C_MARCO_VARIABLE"
    PPTokens = "PPTokens"

    # Debug
    ReservedWord = "ReservedWord"
    LexicalError = "LexicalError"
    # NULL = 'NULL'
    AnyString = "AnyString"

    def isNonterminal(self):
        return False


class Test(unittest.TestCase):

    def test(self):
        print('hi')
        print(TokenType.if_)
