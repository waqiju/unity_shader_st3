import os
import re
import json

root = r"C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\UnityShader\builtin_shaders-5.3.4f1\CGIncludes"
pluginRootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class Symbol(object):
    def __init__(self, name = "", type = "", path = "", pos = (0,0)):
        self.name = name
        self.type = type;
        self.path = path
        self.pos = pos

    @staticmethod
    def json2Symbol(d):
        return Symbol(d['name'], d['type'], d['path'], d['pos'])

def generateSymbolList():
    symbolList = []
    generateFunctionList(symbolList)
    generateDefineList(symbolList)

    f = open(r'../builtin_shader.symbol', 'w')
    # json.dump(symbolList, f, default=lambda obj: obj.__dict__)
    json.dump(symbolList, f, default=lambda obj: obj.__dict__, indent = 4)
    f.close()

def generateFunctionList(symbolList):
    for path, folders, files in os.walk(root):
        for filename in files:
            f = open(os.path.join(root, filename))
            buf = f.read()
            f.close()

            functionIter = re.finditer(r"^(inline[ \t]+)?[ \t]*[\w]+[ \t]+(\w+)[ \t]*\((([ \t]*(\w+[ \t]+)?\w+[ \t]+\w)|([ \t]*\n)|([ \t]*\)))",
                buf, re.M)
            for i in functionIter:
                # todo, path截短
                name = i.group(2)
                path = os.path.join(root, filename)
                path = path.replace(pluginRootPath+"\\", "")
                lineNo = len(re.findall(r".*\n", buf[0:i.start()])) + 1
                columnNo = re.search(i.group(2), i.group(0)).start()
                pos = (lineNo, columnNo)
                symbolList.append(Symbol(name, "builtin-function", path, pos))


def generateDefineList(symbolList):
    for path, folders, files in os.walk(root):
        for filename in files:

            if filename == "HLSLSupport.cginc":
                continue

            f = open(os.path.join(root, filename))
            buf = f.read()
            f.close()

            functionIter = re.finditer(r"^[\s]*#define[\s]+(\w+)\b(?!\s*\n)", buf, re.M)
            for i in functionIter:
                name = i.group(1)
                path = os.path.join(root, filename)
                path = path.replace(pluginRootPath+"\\", "")
                lineNo = len(re.findall(r".*\n", buf[0:i.start()])) + 1
                columnNo = re.search(i.group(1), i.group(0)).start()
                pos = (lineNo, columnNo)
                symbolList.append(Symbol(name, "builtin-marco", path, pos))


def printSymbolList():
    f = open(r'../builtin_shader.symbol', 'r')
    symbolList = json.load(f, object_hook=Symbol.json2Symbol)
    f.close()

    f = open(r'C:\Users\Administrator\Desktop\Tmp\symbolList.txt', 'w')
    for i in symbolList:
        f.write("%s,\t%s,\t%s,\t%s\n" % (i.name, i.type, i.path, i.pos))
    f.close()

def generateCompletesFile():
    f = open(r'../builtin_shader.symbol', 'r')
    symbolList = json.load(f, object_hook=Symbol.json2Symbol)
    f.close()

    f = open('builtin.sublime-completions', 'w')
    f.write(r'''{
    "scope": "source.shader",
    "completions":
    [
''')
    
    isExists = set()
    for i in symbolList:
        if i.name in isExists:
            continue
        else:
            isExists.add(i.name)

        if i.type == "builtin-function":
            line = '        { "trigger": "%s\\tbuiltin-function", "contents": "%s($0)"},\n' % (i.name, i.name)
        elif i.type == "builtin-marco":
            line = '        { "trigger": "%s\\tbuiltin-marco", "contents": "%s"},\n' % (i.name, i.name)
        else:
            line = '        { "trigger": "%s", "contents": "%s"},\n' % (i.name, i.name)


        f.write(line)
    
    f.write(r'''    ]
}
''')

    f.close()

if __name__ == "__main__":
    generateSymbolList()
    # generateCompletesFile()
