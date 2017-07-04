import unittest
from .lex_token import Token
from .symbol_type import SymbolType


class NonterminalMeta(type):

    def __new__(cls, name, bases, attrs):
        if name != 'Nonterminal':
            attrs['kind'] = name if Nonterminal is bases[0] else bases[0].__qualname__
            attrs['leadingProductions'] = []
            attrs['production'] = None

        newCls = super().__new__(cls, name, bases, attrs)

        # register
        if name != 'Nonterminal':
            Nonterminal.registerClass(name, newCls)

        return newCls


class Nonterminal(metaclass=NonterminalMeta):

    classDict = {}

    @staticmethod
    def registerClass(name, cls):
        Nonterminal.classDict[name] = cls

    @staticmethod
    def getClass(name):
        cls = Nonterminal.classDict.get(name)
        if cls is not None:
            return cls
        else:
            print('Error, donot have the class, name = %s' % name)
            raise Exception

    @staticmethod
    def postInitialize(productionList):
        for p in productionList:
            # Production <--> Nonterminal
            levelOneName = p.left
            levelTwoName = p.left + '_' + p.name
            # eg: prog
            levelOneCls = Nonterminal.getClass(levelOneName)
            levelOneCls.leadingProductions.append(p)
            # eg: prog_p1
            levelTwoCls = Nonterminal.getClass(levelTwoName)
            levelTwoCls.production = p
            # 
            p.LeftNonterminalClass = levelTwoCls

            # add 'Shader' into TokenType
            stTuple = ()
            for elm in p.right:
                if elm not in SymbolType.TokenType and elm not in SymbolType.NonterminalType:
                    newSt = '-%s-' % str.lower(elm)
                    SymbolType.TokenType.add(newSt)
                    stTuple += (newSt,)
                else:
                    stTuple += (elm,)
            p.right = stTuple

    def __init__(self):
        pass
        # self.kind = None
        # self.leadingProductions = []

    def toDict(self):
        d = {}
        # d['kind'] = self.kind
        for k in dir(self):
            v = getattr(self, k)
            # token
            if isinstance(v, Token):
                d[k] = str(v)
            # nonterminal
            if isinstance(v, Nonterminal):
                d[k] = v.toDict()
        return d

    def toCode(self):
        raise Exception("should not go here! may you need to import syntax_tree_to_code.")


class Test(unittest.TestCase):

    class E(Nonterminal):

        kind = 'E'
        leadingProductions = []
        production = None

        def __init__(self, v):
            self.value = v

    def test(self):
        e = Test.E('x')
        print(e.toDict())
