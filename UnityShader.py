import sublime
import sublime_plugin
import os
import json
from .scripts import config
from .scripts import symbol_list
from .scripts.symbol_list import Symbol
from .scripts.common import pluginRootPath
from .scripts.settings_listener import SettingsListener

symbalMapFile = os.path.join(pluginRootPath, "builtin_shader.symbol")
symbolMap = {}


def init():
    settings = sublime.load_settings("UnityShader.sublime-settings")
    listener = SettingsListener(settings)
    listener.add("unity_version", onUnityVersionChanged)
    settings.add_on_change("on_settings_changed", listener.onChanged)

    if not _isUnityVersionConsistent():
        _generateSymbolAndCompletions()
    loadSymbolList()


def onUnityVersionChanged():
    if not _isUnityVersionConsistent():
        _generateSymbolAndCompletions()
        loadSymbolList()


def plugin_loaded():
    sublime.set_timeout(init, 300)


def plugin_unloaded():
    settings = sublime.load_settings("UnityShader.sublime-settings")
    settings.clear_on_change("on_settings_changed")


# shader_goto_definition
class ShaderGotoDefinitionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selectText = self.view.substr(self.view.sel()[0])
        if len(selectText) == 0:
            selectText = self.view.substr(self.view.word(self.view.sel()[0]))

        if symbolMap.get(selectText):
            self.gotoDefinition(symbolMap[selectText])
        else:
            sublime.status_message(
                "Can not find definition '%s'" % (selectText))

    def gotoDefinition(self, symbol):
        print(pluginRootPath, symbol.path)
        path = os.path.join(pluginRootPath, symbol.path +
                            ":" + str(symbol.pos[0]))
        print(path)
        definitionView = self.view.window().open_file(path, sublime.ENCODED_POSITION)
        definitionView.set_read_only(True)

    def is_enabled(self):
        filename = self.view.file_name()
        ext = os.path.splitext(filename)[1][1:]
        return ext == "shader" or ext == "cginc"

    def is_visible(self):
        return self.is_enabled()


def loadSymbolList():
    symbolMap.clear()

    f = open(symbalMapFile, 'r')
    symbolList = json.load(f, object_hook=Symbol.json2Symbol)

    for i in symbolList:
        name = i.name
        if not symbolMap.get(name):
            symbolMap[name] = i


def _isUnityVersionConsistent():
    settings = sublime.load_settings("UnityShader.sublime-settings")
    targetVersion = settings.get("unity_version", "0.0.0")
    workingVersion = config.get().get("unity_version", "0.0.0")
    return targetVersion == workingVersion


def _generateSymbolAndCompletions():
    settings = sublime.load_settings("UnityShader.sublime-settings")
    targetVersion = settings.get("unity_version", "0.0.0")
    candidates = list(filter(lambda x: targetVersion in x,
                             os.listdir(pluginRootPath)))
    if len(candidates) <= 0:
        sublime.error_message("UnityShader: unity version setting is wrong!")
        return

    builtinShaderFolderPath = os.path.join(
        pluginRootPath, candidates[0], "CGIncludes")
    symbol_list.generateSymbolList(builtinShaderFolderPath)
    symbol_list.generateCompletesFile()

    _modifyLocalConfigVersion(targetVersion)
    sublime.message_dialog(
        "UnityShader: toggle unity version success :-)\nWorking version is %s" % targetVersion)


def _modifyLocalConfigVersion(version):
    d = config.get()
    d["unity_version"] = version
    config.save(d)
