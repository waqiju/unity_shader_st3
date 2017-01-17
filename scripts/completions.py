import re
import os


class Record(object):
    def __init__(self, trigger = "", content = "", shortTrigger = ""):
        self.trigger = trigger
        self.content = content
        self.shortTrigger = shortTrigger

def readFile(path):
    f = open(path, 'r')
    buf = f.read()
    f.close()

    records = {}
    recordsIter = re.finditer(r'"trigger":\s"(.*)",\s"contents":\s"(.*)"', buf)
    for i in recordsIter:
        trigger = i.group(1)
        content = i.group(2)
        # print(trigger)
        regMatch = re.search(r"^(\w+)(\\t.*)?$", trigger)
        if regMatch:
            shortTrigger = regMatch.group(1)
        else:
            shortTrigger = trigger
        r = Record(trigger, content, shortTrigger)
        records[shortTrigger] = r
        # print(r.trigger, r.content)

    return records

def writeFile(records, path):
    f = open(path, 'w')
    f.write(r'''{
    "scope": "source.shader",
    "completions":
    [
''')

    recordList = list(records.items())
    recordList.sort()
    for k, v in recordList:
        line = '        { "trigger": "%s", "contents": "%s"},\n' % (v.trigger, v.content)
        f.write(line)
    f.write(r'''    ]
}
''')
    f.close()

def Sub(a, b):
    print("Before Sub, len(a) = %s len(b) = %s" % (len(a), len(b)))

    for k,v in b.items():
        if a.get(k):
            a.pop(k)
            # print("Del: ", k)

    print("After Sub, len(a) = %s len(b) = %s" % (len(a), len(b)))

def Add(a, b):
    print("Before Add, len(a) = %s len(b) = %s" % (len(a), len(b)))

    for k,v in b.items():
        if a.get(k):
            pass
        else:
            a[k] = v
            print("Add: ", k)

    print("After Add, len(a) = %s len(b) = %s" % (len(a), len(b)))

cg = readFile(r"C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\UnityShader\cg.sublime-completions")
builtin = readFile(r"C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\UnityShader\builtin.sublime-completions")
globalComletions = readFile(r"C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\UnityShader\global.sublime-completions")
# Add(cg, builtin)
Sub(globalComletions, builtin)
# writeFile(globalComletions, r"C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\UnityShader\global.sublime-completions")