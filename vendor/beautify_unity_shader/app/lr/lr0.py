from ..syntax_production import Production
from .base_types import ObjectSet, ItemLR0
from .base_algorithms import calcClosureLR0, gotoLR0
import unittest


beginningNonterminal = '__Begin'
endingTerminal = '__End'


def construct(productionList):
    # 加入S -> XX $
    firstNonterminalType = productionList[0].left
    beginningProduction = Production(
        '%s -> %s %s' % (beginningNonterminal,
                         firstNonterminalType.name, endingTerminal),
        'p0',
        beginningNonterminal,
        (firstNonterminalType, endingTerminal),
    )
    productionList.insert(0, beginningProduction)
    beginningItemSet = ObjectSet()
    beginningItemSet.add(ItemLR0(beginningProduction))

    # 初始化stateSet
    beginningState = calcClosureLR0(productionList, beginningItemSet)
    stateSet = ObjectSet()
    stateSet.add(beginningState)
    stateList = []
    stateList.append(beginningState)
    # 初始化edges
    edges = {}
    # 初始化symbolType
    from test.lr0_test.tokens import TokenType
    from test.lr0_test.nonterminals import NonterminalType
    SymbolType = [ty for ty in TokenType] + [ty for ty in NonterminalType]

    stateIndex = 0
    while (stateIndex < len(stateList)):
        state = stateList[stateIndex]
        edges[stateIndex] = {}

        # 放置Reduce
        for item in state:
            if item.getNextSymbolType() is None:
                productionNo = item.production.name[1:]
                for ty in TokenType:
                    _addEdge(edges, stateIndex, ty.name, 'r' + productionNo)
                    # edges[stateIndex][ty.name] = 'r' + productionNo

        # 放置Shift
        for ty in SymbolType:
            newState = gotoLR0(productionList, state, ty)
            if len(newState) == 0:
                continue

            if not stateSet.has(newState):
                stateSet.add(newState)
                stateList.append(newState)

            _addEdge(edges, stateIndex, ty.name, 's%s' % stateSet.getSerialNumber(newState))
            # edges[stateIndex][ty.name] = 's%s' % stateSet.getSerialNumber(newState)

        stateIndex = stateIndex + 1

    for i, state in enumerate(stateList):
        print(i, state)

    print('---------------------------')
    for ty in SymbolType:
        print(ty.name + '\t', end='')
    print('')

    for i, state in enumerate(stateList):
        for ty in SymbolType:
            actionStr = str(edges[i][ty.name] if edges[i].get(ty.name) else '\t') + '\t'
            print(actionStr, end='')
        print('')


def _addEdge(edges, key1, key2, action):
    oldValue = edges[key1].get(key2)
    if oldValue is None:
        edges[key1][key2] = action
    elif isinstance(oldValue, str):
        edges[key1][key2] = [oldValue, action]
    elif isinstance(oldValue, list):
        edges[key1][key2].append(action)
    else:
        print('should not go here!')


class Test(unittest.TestCase):

    def test(self):
        from test.lr0_test.productions import productionList
        dfmEdges = construct(productionList)

    # 测试s0和s1
    def DDtest2(self):
        from test.lr0_test.productions import productionList
        # 加入S -> XX $
        firstNonterminalType = productionList[0].left
        beginningProduction = Production(
            '%s -> %s %s' % (beginningNonterminal,
                             firstNonterminalType.name, endingTerminal),
            'p0',
            beginningNonterminal,
            (firstNonterminalType, endingTerminal),
        )
        productionList.insert(0, beginningProduction)
        beginningItemSet = ObjectSet()
        beginningItemSet.add(ItemLR0(beginningProduction))

        stateSet = ObjectSet()
        s = calcClosureLR0(productionList, beginningItemSet)
        print(s)

        from ..lex_tokens import TokenType
        s1 = gotoLR0(productionList, s, TokenType.ID)
        print(s1)
