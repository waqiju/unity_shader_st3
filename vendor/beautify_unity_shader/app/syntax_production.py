
class Production:

    def __init__(self, raw, name, left, right):
        self.raw = raw
        self.name = name
        self.left = left
        self.right = right
        self.LeftNonterminalClass = None

    def __str__(self):
        # return self.raw + '\n\t' + str(self.left) + ' ' + str(self.right)
        return self.raw
