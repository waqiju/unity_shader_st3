import unittest


class Token:

    def __init__(self, kind, text=None, value=None):
        self.kind = kind
        self.text = text
        self.value = value
        self.nextToken = None  # 按照是源文件的顺序，不受lexer中filter的影响

    def __str__(self):
        # return 'kind = %s, text = %s, value = %s' % (self.kind, self.text, self.value)
        if self.value:
            return '%s(%s)' % (self.kind, self.value)
        else:
            return str(self.kind)

    def toLiteral(self):
        if self.kind == "ID":
            return '-%s-' % str.lower(self.value) # 该死的Unity Shader并不严格区分关键字的大小写。eg: SubShader和Subshader。


class Test(unittest.TestCase):

    def test(self):
        from .lex_tokens import TokenType
        print(Token(TokenType.ID, 'Shader', 'Shader'))
