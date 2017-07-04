import unittest


# it should be redesign, some bad taste
class ObjectSet:

    def __init__(self, srcSet=None):
        self.set = {}
        self.setInSequence = []
        self.serialNumber = {}
        self.hashValue = None

        if srcSet:
            for i in srcSet:
                self.add(i)

    def add(self, obj):
        if self.has(obj):
            return

        key = obj if isinstance(obj, str) else obj.getHashValue()
        self.set[key] = obj
        self.setInSequence.append(obj)
        self.serialNumber[key] = len(self) - 1
        # self.updateHashValue()

    def has(self, obj):
        return self.set.get(obj if isinstance(obj, str) else obj.getHashValue()) is not None

    @staticmethod
    def unionReportDirty(lhs, rhs):
        newSet = ObjectSet(lhs)
        for i in rhs:
            newSet.add(i)

        if len(newSet) > len(lhs):
            return newSet, True
        else:
            return newSet, False

    @staticmethod
    def union(lhs, rhs):
        newSet = ObjectSet(lhs)
        for i in rhs:
            newSet.add(i)

        return newSet

    def __len__(self):
        return self.set.__len__()

    def __iter__(self):
        return (self.set[key] for key in self.set)

    def __str__(self):
        text = ''
        for obj in self:
            text = text + str(obj) + ', '
        return '(%s)' % text

    def __getitem__(self, key):
        return self.setInSequence[key]


    def updateHashValue(self):
        self.hashValue = ''
        for key in sorted(self.set.keys()):
            self.hashValue = self.hashValue + '__S_' + key

    def getHashValue(self):
        if self.hashValue is None:
            self.updateHashValue()
        return self.hashValue

    def getSerialNumber(self, obj):
        return self.serialNumber.get(obj.getHashValue())


class ItemLR0:

    def __init__(self, production, point=0):
        self.production = production
        self.point = point
        # may there is a better way
        self.hashValue = '__h_' + str(production) + '__p_' + str(point)

    def getHashValue(self):
        return self.hashValue

    def getNextSymbolType(self):
        if self.point < len(self.production.right):
            return self.production.right[self.point]
        else:
            return None

    def moveNext(self):
        return ItemLR0(self.production, self.point + 1)

    def __str__(self):
        # return 'Item<%s , %s>' % (str(self.production), self.point)

        # like E -> T + .E
        left = self.production.left
        text = '%s -> ' % (left.name if isinstance(left, Enum) else left)
        for index, symbolTypeOrString in enumerate(self.production.right):
            if self.point == index:
                text = text + '.'
            text = text + (symbolTypeOrString.name if isinstance(
                symbolTypeOrString, Enum) else symbolTypeOrString) + ' '
        if self.point == len(self.production.right):
            text = text[:-1] + '. '
        return text


class Item:

    def __init__(self, production, point, lookAheadST):
        self.production = production
        self.point = point
        self.lookAheadST = lookAheadST
        self.tailSTList = list(production.right[point+1:]) + [lookAheadST, ]
        # may there is a better way
        self.hashValue = '__h_' + str(production) + '__p_' + str(point) + '__l_' + str(lookAheadST)

    def getHashValue(self):
        return self.hashValue

    def getNextSymbolType(self):
        if self.point < len(self.production.right):
            return self.production.right[self.point]
        else:
            return None

    def moveNext(self):
        return Item(self.production, self.point + 1, self.lookAheadST)

    def getTailSTList(self):
        return self.tailSTList

    def getLookAheadST(self):
        return self.lookAheadST

    def __str__(self):
        # return 'Item<%s , %s>' % (str(self.production), self.point)

        # like E -> T + .E , $
        left = self.production.left
        text = '%s -> ' % (left.name if isinstance(left, Enum) else left)
        for index, symbolTypeOrString in enumerate(self.production.right):
            if self.point == index:
                text = text + '.'
            text = text + (symbolTypeOrString.name if isinstance(
                symbolTypeOrString, Enum) else symbolTypeOrString) + ' '
        if self.point == len(self.production.right):
            text = text[:-1] + '. '
        text = text + ' | ' + str(self.lookAheadST)
        return text


class Test(unittest.TestCase):

    def testLR0(self):
        item1 = ItemLR0('production', 1)
        item2 = ItemLR0('prod', 2)
        item3 = ItemLR0('prod', 3)

        s1 = ObjectSet()
        s1.add(item1)
        s1.add(item1)
        self.assertTrue(len(s1) == 1)

        s2 = ObjectSet()
        s2.add(item2)
        s2.add(item3)
        self.assertTrue(len(s2) == 2)

        s3, isDirty = ObjectSet.unionReportDirty(s1, s2)
        self.assertTrue(isDirty)
        self.assertTrue(len(s3) == 3)

    def test(self):
        from test.lr1_test.productions import productionList
        p = productionList[0]
        print(p)
        item = Item(p, 1, 'symbol')
        print(item)
        print(item.getTailSTList())
