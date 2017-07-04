import sys


_cellOffset = 0


def _printCell(text):
    global _cellOffset
    if text == '\n':
        print('')
        _cellOffset = 0

        return

    if _cellOffset > 0:
        text = ' ' + text
    for i in range(len(text), 15 - _cellOffset):
        text = text + ' '
    mayShortedLen = 15 - len(text)
    _cellOffset -= mayShortedLen
    if _cellOffset < 0:
        _cellOffset = 0

    print(text, end='')


def printProductionList(productionList):
    print('-------ProductionList-----------')
    for p in productionList:
        print(p)
    print('--------------------------------')


def printStateList(stateList, preStateIndex, file=None):
    if file is not None:
        oldStdout = sys.stdout
        sys.stdout = file
    else:
        print('-----------StateList------------')

    for i, state in enumerate(stateList):
        print(i, '<-', preStateIndex[i], state)

    if file is not None:
        sys.stdout = oldStdout
    else:
        print('--------------------------------')


def printEdges(edges, file=None):
    from ..symbol_type import SymbolType

    if file is not None:
        oldStdout = sys.stdout
        sys.stdout = file
    else:
        print('------------Edges---------------')

    _printCell('')
    for ty in SymbolType:
        _printCell(ty)
    _printCell('\n')

    for i, _ in enumerate(edges):
        _printCell(str(i))
        for ty in SymbolType:
            actionStr = str(edges[i][ty] if edges[i].get(ty) else '')
            _printCell(actionStr)
        _printCell('\n')

    print('unsolved conflicts:')
    for i, _ in enumerate(edges):
        for ty in SymbolType:
            if isinstance(edges[i].get(ty), list):
                print('%s x %s : %s' % (i, ty, edges[i].get(ty)))

    if file is not None:
        sys.stdout = oldStdout
    else:
        print('--------------------------------')
