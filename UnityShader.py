import sublime
import sublime_plugin
import os
import json
from .generateSymbolList import Symbol

symbalMapFile = r"C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages\UnityShader\buildin_shader.symbol"

symbolMap = {}
def init():
    print("init start")
    symbolMap.clear()

    f = open(symbalMapFile, 'r')
    symbolList = json.load(f, object_hook=Symbol.json2Symbol)

    for i in symbolList:
        name = i.name
        if not symbolMap.get(name):
            symbolMap[name] = i

    print(len(symbolMap))

    print("init end")


def plugin_loaded():
    sublime.set_timeout(init, 300);

# shader_goto_definition
class ShaderGotoDefinitionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("run")
        selectText = self.view.substr(self.view.sel()[0])
        if len(selectText) == 0:
            selectText = self.view.substr(self.view.word(self.view.sel()[0]))

        print(selectText)

        if symbolMap.get(selectText):
            self.gotoDefinition(symbolMap[selectText])
        else:
            sublime.status_message("Can not find definition '%s'" % (selectText))

    def gotoDefinition(self, symbol):
        print("gotoDefinition")
        print(symbol.path)
        definitionView = self.view.window().open_file(symbol.path + ":" + str(symbol.pos[0]), sublime.ENCODED_POSITION)
        definitionView.set_read_only(True)