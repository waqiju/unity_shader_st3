

_lineNo = 1
_columnNo = 1


def reset():
    global _lineNo, _columnNo
    _lineNo = 1
    _columnNo = 1


def forward(text):
    global _lineNo, _columnNo
    for ch in text:
        if ch == '\n':
            _lineNo = _lineNo + 1
            _columnNo = 1
        else:
            _columnNo = _columnNo + 1


def error(message):
    text = 'Error: (%s , %s) ' % (_lineNo, _columnNo)
    text = text + message
    print(text)
