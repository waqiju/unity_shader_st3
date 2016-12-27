import os
import re

root = r"C:\Users\Administrator\Desktop\Tmp\Unity-Shader-master\Unity5"

class Record(object):
    def __init__(self, trigger = "", content = ""):
        self.trigger = trigger
        self.content = content

records = []
for path, dirs, files in os.walk(root):
    for filename in files:

        f = open(os.path.join(path, filename), 'r', encoding='utf')
        buf = f.read()
        f.close()

        triggers = re.findall(r"<tabTrigger>(.*)</tabTrigger>", buf)
        contents = re.findall(r"<content><!\[CDATA\[(.*)]]></content>", buf)
        if (len(contents) > 0):
            records.append(Record(triggers[0], contents[0]))
        else:
            print(filename)


f = open(r"C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\Unity3DShader\Unity5.sublime-completions", 'w')
f.write(r'''{
    "scope": "source.shader",
    "completions":
    [
''')
for i in records:
    line = '        { "trigger": "%s", "contents": "%s"},\n' % (i.trigger, i.content)
    f.write(line)
f.write(r'''    ]
}
''')
f.close()
