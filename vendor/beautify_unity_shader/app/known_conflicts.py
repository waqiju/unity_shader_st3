

rules = (
    ['r301', 's1559'],
    ['r301', 's1576'],
)


def applyTo(edges):
    from .symbol_type import SymbolType

    for i, _ in enumerate(edges):
        for ty in SymbolType:
            action = edges[i].get(ty)

            if isinstance(action, list):
                edges[i][ty] = _solveConflicts(action)

    return edges


def _solveConflicts(actions):
    for rule in rules:
        for action in actions:
            if action not in rule:
                break

        return rule[0]

    return actions