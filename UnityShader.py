import sublime
import sublime_plugin
import os
import json
from .scripts.generateSymbolList import Symbol

pluginRootPath = os.path.abspath(os.path.dirname(__file__))
symbalMapFile = os.path.join( pluginRootPath, "builtin_shader.symbol" )

symbolMap = {}
def init():
    symbolMap.clear()

    f = open(symbalMapFile, 'r')
    symbolList = json.load(f, object_hook=Symbol.json2Symbol)

    for i in symbolList:
        name = i.name
        if not symbolMap.get(name):
            symbolMap[name] = i


def plugin_loaded():
    sublime.set_timeout(init, 300);

# shader_goto_definition
class ShaderGotoDefinitionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selectText = self.view.substr(self.view.sel()[0])
        if len(selectText) == 0:
            selectText = self.view.substr(self.view.word(self.view.sel()[0]))

        if symbolMap.get(selectText):
            self.gotoDefinition(symbolMap[selectText])
        else:
            sublime.status_message("Can not find definition '%s'" % (selectText))

    def gotoDefinition(self, symbol):
        print(pluginRootPath, symbol.path)
        path = os.path.join(pluginRootPath, symbol.path + ":" + str(symbol.pos[0]))
        print(path)
        definitionView = self.view.window().open_file(path, sublime.ENCODED_POSITION)
        definitionView.set_read_only(True)

    def is_enabled(self):
        filename = self.view.file_name()
        ext = os.path.splitext(filename)[1][1:]
        return ext == "shader" or ext == "cginc"

    def is_visible(self):
        return self.is_enabled()