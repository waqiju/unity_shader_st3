import os
import json
import unittest
from . import lexer
from . import preprocessor
from . import known_conflicts
from .lr import dfm
from .lr import inspector
from .lr import lr1
from .syntax_productions import productionList


def construct():
    edges, stateList, preStateIndex = lr1.construct(productionList, isDebug=True)

    with open(os.path.join(__file__, '../output/3_state_list.txt'), 'w') as f:
        inspector.printStateList(stateList, preStateIndex, f)
    with open(os.path.join(__file__, '../output/3_dfm_edges.txt'), 'w') as f:
        inspector.printEdges(edges, f)
    with open(os.path.join(__file__, '../output/3_edges.json'), 'w') as f:
        json.dump(edges, f, indent=4)


def analyze(tokens, edges = None):

    if edges is None:
        edges = loadEdges()

    ast = dfm.run(edges, productionList, tokens, isDebug=False)
    return ast


def loadEdges():

    def json2Edges(d):
        edges = {}
        for key in d:
            edges[int(key)] = d[key]
        return edges

    with open(os.path.join(__file__, '../output/3_edges.json')) as f:
        edges = json2Edges(json.load(f))

    # 消除已知的冲突
    edges = known_conflicts.applyTo(edges)

    return edges


def analyzeCodeText(codeText, edges=None):
    tokens = lexer.analyze(codeText, isEnding=True)
    tokens = preprocessor.analyze(tokens)
    ast = analyze(tokens, edges)
    return ast, tokens


class Test(unittest.TestCase):

    def DtestConstruct(self):
        construct()

    def DtestAnalyze(self):
        # 用shader进行验证
        with open(os.path.join(__file__, '../../test/combined_test/test.shader')) as f:
            inputText = f.read()

        ast = analyzeCodeText(inputText)

        outputFile = os.path.abspath(os.path.join(__file__, '../output/3_syntax_output.txt'))
        with open(outputFile, 'w') as f:
            json.dump(ast.toDict(), f, indent=4)

    def DtestFormatter(self):
        with open(os.path.join(__file__, '../../test/formatter_test/formatted.shader')) as f:
            inputText = f.read()
        ast, tokens = analyzeCodeText(inputText)

        from .extension.formatter import Formatter
        formatter = Formatter(tokens, ast)
        outputFile = os.path.abspath(os.path.join(__file__, '../output/4_formatted_code.shader'))
        with open(outputFile, 'w') as f:
            f.write(formatter.toCode())

        formatter.reset()
        self.maxDiff = None
        self.assertEqual(inputText, formatter.toCode())