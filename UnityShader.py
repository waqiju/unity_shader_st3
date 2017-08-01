import sublime
import sublime_plugin
import os
import json
import re
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


def loadSymbolList():
    symbolMap.clear()

    with open(symbalMapFile, 'r') as f:
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


# shader_auto_format
class ShaderAutoFormatCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        from .vendor.beautify_unity_shader.app import parser
        from .vendor.beautify_unity_shader.app.extension.formatter import Formatter

        region = sublime.Region(0, self.view.size())
        codeText = self.view.substr(region)
        try:
            ast, tokens = parser.analyzeCodeText(codeText)
        except Exception as error:
            sublime.message_dialog(
                "Sorry, format failed...  o_o\n\n"
                "Please make sure the code is grammatical correct. Or welcome to give feedback by issue (https://github.com/waqiju/unity_shader_st3/issues).")
            raise error

        formattedText = Formatter(tokens, ast).toCode()

        self.view.erase(edit, region)
        self.view.insert(edit, 0, formattedText)
        # Success Tips
        sublime.status_message('Format Success!')

    def is_enabled(self):
        filename = self.view.file_name()
        ext = os.path.splitext(filename)[1]
        return ext == ".shader"

    def is_visible(self):
        return self.is_enabled()


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
        # print(pluginRootPath, symbol.path)
        path = os.path.join(pluginRootPath, symbol.path +
                            ":" + str(symbol.pos[0]))
        definitionView = self.view.window().open_file(path, sublime.ENCODED_POSITION)
        definitionView.set_read_only(True)

    def is_enabled(self):
        filename = self.view.file_name()
        ext = os.path.splitext(filename)[1]
        return ext == ".shader" or ext == ".cginc"

    def is_visible(self):
        return self.is_enabled()


class CompletionInfo:

    def __init__(self, word, location):
        self.word = word
        self.location = location


class UnityShaderCompletionsQuerier(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        if not self.isShaderFile(view):
            return

        # Abandon use extract_completions(). Cause it get unexpect result in some case, such as 'var1*var2; #include'
        # Anohter reason is that it not introduce in lastest offical document @170726, maybe obsolete in futrue.
        # wordsInBuffer = view.extract_completions(prefix)
        # completionsInBuffer = [(word + '\tcontext', word) for word in wordsInBuffer]

        completionsInBuffer = self.extract_completions(view, prefix, locations)
        return (completionsInBuffer, sublime.INHIBIT_WORD_COMPLETIONS)

    @staticmethod
    def isShaderFile(view):
        return os.path.splitext(view.file_name())[1] == '.shader'

    @staticmethod
    def extract_completions(view, prefix, locations):
        # retrieve words and regions
        wordsInBuffer = []
        wordsRegions = view.find_all(r'\b' + re.escape(prefix) + r'\w+\b', 0, '$0', wordsInBuffer)

        # dump them to completionInfos
        completionInfos = []
        for i, word in enumerate(wordsInBuffer):
            location = (wordsRegions[i].a + wordsRegions[i].b) / 2
            completionInfos.append(CompletionInfo(word, location))

        # sort and deduplicate
        firstEditLocation = locations[0]
        completionInfos.sort(key=lambda info: abs(info.location - firstEditLocation))

        wordSet = set()
        def isDuplicate(info):
            if info.word not in wordSet:
                wordSet.add(info.word)
                return True
            else:
                return False
        completionInfos = list(filter(isDuplicate, completionInfos))

        completionsInBuffer = [(completionInfo.word + '\tcontext', completionInfo.word) for completionInfo in completionInfos]
        return completionsInBuffer
